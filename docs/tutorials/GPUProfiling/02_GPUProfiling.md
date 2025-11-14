---
title: GPU profiling
description: Avec Pix
---

# Profiling GPU – PIX (1h)

## Introduction

Le profiling GPU permet de comprendre les goulots d’étranglement d’un GPU en fonction de ses cycles matériels.  
Plusieurs types de bottlenecks peuvent être identifiés dans un shader : la bande passante mémoire, l’utilisation des ALU (arithmetic logic units), le sampling, ou encore le débit d’instructions.  
Il est donc essentiel de comprendre les limitations techniques du GPU que l’on utilise.

## Les outils

Il existe de nombreux outils de profiling GPU selon les fabricants d’API ou d’hardware :

| Plateforme / Système                     | Outil de Profilage / Debug GPU                                    | Remarques |
|------------------------------------------|-------------------------------------------------------------------|-----------|
| **DirectX (PC Windows)**                 | PIX                                                               |           |
| **Metal (macOS / iOS)**                  | Instruments / Xcode GPU Frame Capture                             |           |
| **AMD**                                  | AMD Radeon™ GPU Profiler                                          |           |
| **NVIDIA (PC, Laptop, Workstation)**     | Nsight                                                            |           |
| **Nintendo Switch**                      | NX Graphics Debugger                                              | Disponible uniquement pour développeurs agréés |
| **Android (OpenGL / Vulkan / GPU)**      | Adreno Profiler, ARM Mali GPU Profiler                            | Selon le GPU du device |
| **PlayStation 5**                        | PS5 GPU Profiler                                                  | Disponible uniquement pour développeurs enregistrés |
| **Xbox Series X|S**                      | Xbox Developer Kit GPU Profiler                                   | Disponible uniquement pour développeurs enregistrés |

### Quelques exemples

Xcode possède d’excellents outils de profiling CPU / mémoire / GPU, ainsi que du shader profiling :  
[Documentation Xcode Shader Tools](https://developer.apple.com/documentation/xcode/inspecting-shaders)

**Overview**  
![XcodeGPU1](assets/XcodeGPU1.png)

**GPU profiling**  
![XcodeGPU2](assets/XcodeGPU2.png)

**Shader profiling**  
![XcodeGPU3](assets/XcodeGPU3.png)

**Mali Offline Compiler** :  
[Vidéo explicative](https://www.youtube.com/watch?v=zEybNlwd7SI)

![Mali offline compiler](<assets/Mali Offline Compiler.png>)

## TP

Pour ce TP, nous allons utiliser PIX, version [2509](https://download.microsoft.com/download/6af3c4fa-0513-4e0e-a781-1126df3211a1/PIX-2509.25-Installer-x64.exe).

Nous allons analyser une frame de mon PFE sous DirectX 12 sur PC.  
Gardez en tête que ce projet est conçu pour tourner sur Nintendo Switch :  
le test sera donc biaisé par le matériel utilisé, mais ce biais reste acceptable pour comprendre le profiling GPU.

Ajoutez l’onglet **Pipeline** à côté de l’onglet **Warning** et sélectionnez-le.  
Sélectionnez **RTV 0** et explorez le champ **Visualization**.

Déployez ensuite la fenêtre **Execution Duration** dans la timeline.

---

## Comprendre le contexte du jeu

??? question
    Décrivez rapidement les grandes étapes de rendu du jeu.  
    Le jeu tourne normalement à 60 FPS sur Switch. Pourquoi tourne-t-il légèrement au-dessus de 60 FPS sur PC ?

---

## Comprendre le système de terrain

Nous allons commencer par étudier le terrain.

??? question
    Estimez rapidement le temps nécessaire pour calculer le terrain.  
    Comprenez-vous comment il est rendu ?  
    Connaissez-vous le nom de cette technique ?  
    Quels en sont les avantages ?  
    Quels sont ses plus gros désavantages ?  
    Quelles optimisations proposeriez-vous ?

![switchGPU](assets/switchGPU.png)  
![TerrainSampling](assets/TerrainSampling.png)

---

## Les robots

??? question
    Combien de temps faut-il pour rendre les robots ?  
    Comment sont-ils rendus, et avec quelle technique ?  
    Cette technique a-t-elle un impact sur le GPU selon vous ?

Dans la fenêtre **Tools > Dr PIX**, sélectionnez **Primitive & Rasterization**.  
Choisissez l’event du draw des robots, lancez un test et notez la valeur de **Quad Efficiency**.  
Faites le même test avec un terrain.

??? question
    Que remarquez-vous ?  
    Pourquoi cette valeur n’est-elle pas de 100% pour le terrain ?

Je vous recommande cette vidéo pour comprendre l’importance de ce phénomène :  
[When Optimisations Work, But for the Wrong Reasons – SimonDev](https://www.youtube.com/watch?v=hf27qsQPRLQ)

---

## Comprendre les unités du GPU

Pour analyser un shader en profondeur, il est important de connaître les unités impliquées :

- **Varying (Interpolation)**  
- **ALU**  
  (plusieurs types selon le GPU ; certaines unités sont spécialisées en FP16 ou FP32, d’autres dans les FMA, etc.)
- **Texture load / read / sampler**
- **Autres unités spécialisées…**

---

## Ressources

Pistes de profiling simples :

- Texture atlas  
- VAT  
- Instancing  
- Merger les props  
- Traquer les micro-triangles  

Liens utiles :

- Démonstration sur les `if` dans les shaders :  
  [ShaderToy – Branching](https://www.shadertoy.com/view/wlsGDl)

- Vidéo GDC démystifiant les croyances sur les shaders :  
  [Investigating and Dispelling Shader Myths](https://gdcvault.com/play/1028185/Investigating-and-Dispelling-Shader-Myths)

- Documentation sur le *tile-based rendering* mobile :  
  [Samsung – GPU framebuffer](https://developer.samsung.com/galaxy-gamedev/resources/articles/gpu-framebuffer.html)
