---
title: GPU profiling
description: Avec Pix
---

# Profiling GPU - Pix (1h)

## Intro
Le profiling GPU permet de comprendre les goulots d’étranglement d’un GPU en fonction de ses cycles matériels. Plusieurs types de bottlenecks peuvent être identifiés dans un shader, tels que : la bande passante mémoire, l’utilisation d'ALU (arithmetic logic units
), le sampling, ou encore le débit d’instructions. Il est donc essentiel de comprendre les limitations techniques du GPU que l’on utilise.

## Les outils
Il existe de nombreux outils pour faire du profiling GPU en fonction des fabriquant d'api ou d'harware:

| Plateforme / Système                     | Outil de Profilage / Debug GPU                                    | Remarques |
|------------------------------------------|-------------------------------------------------------------------|------------|
| **DirectX (PC Windows)**                 | PIX                                                               |            |
| **Metal (macOS / iOS)**                  | Instruments / Xcode GPU Frame Capture                             |            |
| **AMD**                                  | AMD Radeon™ GPU Profiler                                          |            |
| **NVIDIA (PC, Laptop, Workstation)**     | Nsight                                                            |            |
| **Nintendo Switch**                      | NX Graphics Debugger                                              | Disponible uniquement pour développeurs agréés |
| **Android (OpenGL / Vulkan / GPU)**      | Adreno Profiler, ARM Mali GPU Profiler                            | Selon le GPU du device |
| **PlayStation 5**                        | PS5 GPU Profiler                                                  | Disponible uniquement pour développeurs enregistrés |
| **Xbox Series X|S**                      | Xbox Developer Kit GPU Profiler                                   | Disponible uniquement pour développeurs enregistrés |

Quelque example:
XCode possède de très bon outils de profiling CPU/Memoire/GPU et profiling de shader : [link](https://developer.apple.com/documentation/xcode/inspecting-shaders)

Overview;
![XcodeGPU1](assets/XcodeGPU1.png)

GPU profiling
![XcodeGPU2](assets/XcodeGPU2.png)

Shader profiling
![XcodeGPU3](assets/XcodeGPU3.png)
Mali Offline Compiler: [video](https://www.youtube.com/watch?v=zEybNlwd7SI)
![Mali offline compiler](<assets/Mali Offline Compiler.png>)

## TP
Pour ce TP nous allons utiliser PIX sous la version [2509](https://download.microsoft.com/download/6af3c4fa-0513-4e0e-a781-1126df3211a1/PIX-2509.25-Installer-x64.exe)

Nous allons étudier une frame de mon PFE sous DX12 sur PC. Il est important de garder en tête que ce projet est fait pour tourner sur Switch. Le teste que nous allons donc faire est biaisé par le materiel que nous utilisons mais ce biai est acceptable pour comprendre la lecture GPU.

Rajouter l'onglet "Pipeline" a côté de l'onglet warning et selectionner le. Selctionnez RTV 0 et jouez avec le champ "visualization". 

Déployer la fenetre "execution duration" dans timeline

??? Comprendre le contexte du jeu
Décrivez rapidement les grande étape de rendu du jeu
Le jeu tourne normalement sur switch à 60 FPS. Essayer de comprendre pourquoi celui ci tourne à un peu plus de 60 FPS sur PC ? 

Nous allons etudier le terrain pour commencer. 
??? Comprendre le systeme de terrain
Estimez rapidement le temps nécéssaire pour calculer le terrain.
Comprenndez vous comment est il rendu ? 
Connaissez vous le noms de cette technique ? 
Quelles sont les avantages de cette technique ?
Qu'elles sont ces plus gros désavantage ? 
Que pourriez vous proposer comme optimisation ?

![switchGPU](assets/switchGPU.png)
![TerrainSampling](assets/TerrainSampling.png)

??? Les robots
Combien de temps faut il pour rendre les robots ? 
Comment sont il rendu et avec quelle technique ? 
Pensez vous que cette technique ai un impact sur GPU ?

Allez dans la fenetre "Tools" -> Dr Pix et selectionnez "Primitive & Rasterization". Selectionnez l'event de draw des robots et lancer un teste et noter la valeur de Quad efficiency. Testez ensuite avec un terrain. Que remarquez vous ? Pourquoi cette valeur n'est pas de 100% pour le terrain ?

Je souhaiterais vous recommander cette vidéo pour comprendre l'important de celà: 
[When Optimisations Work, But for the Wrong Reasons - SimonDev](https://www.youtube.com/watch?v=hf27qsQPRLQ)

Pour rentrer ensuite dans le détail, il est important de connaitre les unité du GPU utilisés:
- Varying (Interpolation) 
- ALU (Beaucoup de type différent en fonction du GPU. Certaine unité peuvent être spécialiser sur des calcules de type différent (float 16, 32), d'autre dans certaine instruction comme les FMA)
- Texture load/read/sampler
- autre...


## Ressources
Piste de profiling simple:
- Texture atlas
- VAT
- Instancing
- Merger les props
- Traquer les micro triangles

Debunk d'IQ sur les if dans les shaders: [link](https://www.shadertoy.com/view/wlsGDl) 
Super video pour démistifier certain préjugé: [link](https://gdcvault.com/play/1028185/Investigating-and-Dispelling-Shader-Myths)
Doc concernant le tile based rendering sur mobile: [link](https://developer.samsung.com/galaxy-gamedev/resources/articles/gpu-framebuffer.html)  
