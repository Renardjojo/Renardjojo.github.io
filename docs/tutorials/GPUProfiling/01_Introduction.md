# Profiling GPU – Introduction (30min)

![Tutorial Cover](assets/profiling_gpu_intro.png)

## Introduction

Dans ce tuto, nous allons voir les méthodes permettant de comprendre et profiler le pipeline de rendu d'une frame d'un jeu. 

Une optimisation dois faire suite à une observation fidèle au risque d'entrainer une perte de temps, de générer des bugs ou d'entrainer une mauvaise compréhension de la frame. 

Pour comprendre une frame il est important de définir dans un premier temps le contexte dans lequel on souhaite la regarder:
- Platform et architecture de la platform étudiée
- Setting graphique
- Contexte en jeu 
- Mode de rendu (API graphique, tile based rendering, forward/gbuffer/autre...)
- Mode de build

Ce contexte va avoir une forte incidence sur le choix des outils à utiliser car chaque outils à ses propres limitations.

De la même façon, il est important d'avoir une bonne connaissance du jeu pour proposer des optimisation contextuel. 
- La camera se déplace t'elle ? 
- A t'on un jeu dynamique ou plutot statique ? 
- Le lighting est il statique ou dynamique ? 
- A quel distance voit on le jeu ?
- Etc...

Ce tutorial est étudié pour être fait sous la forme d'un TP a partir de cas pratique vous permettant ainsi de pratiquer et comprendre par vous même.

Toutes les ressources sont ici: https://drive.google.com/drive/folders/1emHViHZ-Bs3GvlMa7zS9jhXrCJMlaTae?usp=sharing

## Resources
- Game optimization series from Ben Cloward: https://www.youtube.com/watch?v=jt8b0cpjUVk&list=PL78XDi0TS4lG4wvgfyGECmB8XiJLCgfFD