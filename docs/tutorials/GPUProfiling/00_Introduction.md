---
title: 00 Introduction
---

# Profiling GPU – Introduction (30 min)

![Tutorial Cover](assets/profiling_gpu_intro.png)

## Introduction

Dans ce tutoriel, nous allons explorer les méthodes permettant de comprendre et de profiler le pipeline de rendu d'une frame de jeu.

Une optimisation doit toujours découler d’une observation précise. Sans cela, on risque de perdre du temps, de générer des bugs ou d’aboutir à une mauvaise compréhension du comportement de la frame.

Pour analyser une frame, il est essentiel de définir le contexte dans lequel on souhaite l’étudier :
- Platform et architecture matérielle  
- Settings graphiques  
- Contexte in-game  
- Mode de rendu (API graphique, tile-based rendering, forward, gbuffer, autres)  
- Mode de build  

Ce contexte influence fortement le choix des outils, chacun ayant ses propres limitations.

De la même manière, une bonne connaissance du jeu est indispensable pour proposer des optimisations contextuelles :
- La caméra se déplace-t-elle ?  
- Le jeu est-il dynamique ou plutôt statique ?  
- Le lighting est-il statique ou dynamique ?  
- À quelle distance observe-t-on la scène ?  
- Etc.  

Ce tutoriel est conçu sous la forme d’un TP basé sur des cas pratiques afin de vous permettre de manipuler les outils et de comprendre par vous-même.

Toutes les ressources sont disponibles ici :  
[https://drive.google.com/drive/folders/1emHViHZ-Bs3GvlMa7zS9jhXrCJMlaTae?usp=sharing](https://drive.google.com/drive/folders/1emHViHZ-Bs3GvlMa7zS9jhXrCJMlaTae?usp=sharing)

## Resources

- Game Optimization Series by Ben Cloward :  
  [https://www.youtube.com/watch?v=jt8b0cpjUVk&list=PL78XDi0TS4lG4wvgfyGECmB8XiJLCgfFD](https://www.youtube.com/watch?v=jt8b0cpjUVk&list=PL78XDi0TS4lG4wvgfyGECmB8XiJLCgfFD)
