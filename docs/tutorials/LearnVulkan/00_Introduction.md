---
title: 00 Introduction
---

# Context

## Un peu d'histoire

- Avant OpenGL
- OpenGL Legacy (1.x, 2.x)
- Modern OpenGL
- Modern Graphics APIs : Vulkan, Metal, DirectX 12

## Les atouts principaux des API modernes, et spécifiquement de Vulkan

- **Pipeline State Object (PSO)** : regroupe les états du pipeline graphique dans un objet unique, préparé en amont.
- **Command Buffers** : permet d'enregistrer des commandes à l'avance et de les soumettre efficacement au GPU.
- **Flexibilité et performances** : permet un meilleur contrôle du matériel, notamment pour les architectures Tile-Based Rendering (TBR).
- **Extensions** : permettent d'exploiter des fonctionnalités spécifiques aux GPU et aux constructeurs sans alourdir le cœur de l'API.
- **Cross-platform** : Vulkan est disponible sur de nombreuses plateformes et architectures matérielles.
- **Open source et gouvernance ouverte** : Vulkan est développé par le consortium Khronos Group.
- **Compatibilité et évolution** : le cœur de Vulkan reste volontairement minimal. Les nouvelles fonctionnalités sont généralement ajoutées via des extensions, puis éventuellement intégrées au cœur de l'API. Les anciennes fonctionnalités restent disponibles pour préserver la compatibilité.
- **Moins de hacks** : les API modernes exposent directement des fonctionnalités auparavant contournées par des solutions spécifiques. Par exemple, OpenGL nécessitait traditionnellement un contexte graphique associé à une fenêtre, même pour certains usages hors écran.
- **Synchronisation et parallélisme explicites** : le développeur contrôle plus précisément la synchronisation CPU/GPU et l'exécution des commandes sur plusieurs queues.
- **Compilation des shaders** : Vulkan utilise SPIR-V, un format intermédiaire standardisé. La compilation et la validation sont mieux définies, avec moins de dépendance à l'interprétation du code source par les drivers.

## Quelle différence de philosophie entre les API graphiques modernes (Vulkan, Metal, DirectX 12) ?

Elles partagent globalement la même philosophie :
- Réduire les coûts et les responsabilités du driver en donnant davantage de contrôle au développeur.
- Rendre explicites la synchronisation, la gestion des ressources et l'organisation des commandes.
- Exploiter plus efficacement le parallélisme CPU/GPU.

Leurs principales différences concernent :
- **Les écosystèmes ciblés** : Vulkan est cross-platform, Metal est intégré à l'écosystème Apple et DirectX 12 à celui de Microsoft.
- **Les fonctionnalités spécifiques** : chaque API expose des fonctionnalités adaptées à son écosystème et à son matériel.
- **Le coût du driver** : chaque API adopte des choix différents pour limiter les surcoûts et s'intégrer à son environnement natif.
