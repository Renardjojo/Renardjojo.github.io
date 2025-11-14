import yaml
from pathlib import Path
import re

# -------------------------
# Paths
# -------------------------
MKDOCS_FILE = Path("mkdocs.yml")
INDEX_FILE = Path("docs/index.md")


# -------------------------
# Custom YAML loader that ignores unknown tags
# -------------------------
class IgnoreUnknownTagsLoader(yaml.SafeLoader):
    pass

def unknown_tag_constructor(loader, node):
    """
    Ignore unsupported Python-specific YAML tags (like !!python/name)
    """
    return None

IgnoreUnknownTagsLoader.add_constructor(None, unknown_tag_constructor)


# -------------------------
# Read title and description from Markdown front matter
# -------------------------
def read_md_info(file_path):
    """
    Reads title and description from YAML front matter if present.
    If front matter is missing, returns the filename as title and empty description.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        return file_path.stem.replace("_", " ").title(), ""

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if match:
        front_matter = yaml.safe_load(match.group(1))
        title = front_matter.get("title", file_path.stem.replace("_", " ").title())
        desc = front_matter.get("description", "")
    else:
        title = file_path.stem.replace("_", " ").title()
        desc = ""

    return title, desc


# -------------------------
# Recursively parse nav items
# -------------------------
def parse_nav_item(item, level=0):
    """
    Recursively parses mkdocs 'nav' items to generate a Markdown list.
    Returns a list of strings.
    """
    md = []
    # Headings use ### for top-level, #### for next level, etc.
    heading_prefix = "#" * (level + 3)

    if isinstance(item, dict):
        for title, content in item.items():
            if isinstance(content, str):
                t, desc = read_md_info(f"docs/{content}")
                line = f"- [{t}]({content})"
                if desc:
                    line += f" — {desc}"
                md.append(line)
            elif isinstance(content, list):
                # Section header
                md.append(f"\n{heading_prefix} {title}\n")
                for sub in content:
                    md.extend(parse_nav_item(sub, level + 1))
    elif isinstance(item, str):
        t, desc = read_md_info(f"docs/{item}")
        line = f"- [{t}]({item})"
        if desc:
            line += f" — {desc}"
        md.append(line)

    return md


# -------------------------
# Generate summary from mkdocs.yml nav
# -------------------------
def generate_summary():
    """
    Generates full Markdown summary from mkdocs.yml nav section.
    """
    with open(MKDOCS_FILE, "r", encoding="utf-8") as f:
        config = yaml.load(f, Loader=IgnoreUnknownTagsLoader)

    nav = config.get("nav", [])
    lines = ["## Contents", ""]
    for item in nav:
        lines.extend(parse_nav_item(item))
        lines.append("")
    return "\n".join(lines)


# -------------------------
# Insert summary into index.md
# -------------------------
def insert_summary():
    """
    Inserts the generated summary into index.md at [AUTO_SUMMARY] placeholder.
    """
    if not INDEX_FILE.exists():
        print("❌ docs/index.md not found.")
        return

    content = INDEX_FILE.read_text(encoding="utf-8")
    summary = generate_summary()

    # Replace [AUTO_SUMMARY] placeholder (case-insensitive)
    new_content = re.sub(r"\[AUTO_SUMMARY\]", summary, content, flags=re.IGNORECASE)
    INDEX_FILE.write_text(new_content, encoding="utf-8")
    print(f"✅ Summary inserted into {INDEX_FILE}")


if __name__ == "__main__":
    insert_summary()
