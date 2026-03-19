---
title: 00 Introduction
---

# TP rendering Unity (4-8h)

## Introduction

Dans ce TP, nous allons réfléchir sur un cahier des charges rendu de production et implémenter les solutions trouvées.
Ce cahier des charges est issu d’un véritable cas que vous pourrez retrouver dans le jeu Might and Magic Fates.
Cherchez à incarner un programmeur rendu seul dans une équipe, qui doit prendre la responsabilité de ce sujet en début de production.

### Cahier des charges :
- Afficher un board par faction  
- Chaque board possède son lighting  
- Il existe un lighting commun entre ces deux boards  
- Le projet doit tourner sur mobile sur des low-end très bas (S7, iPhone 6S)  
- Le rendu des boards doit être réaliste, mais certains éléments peuvent être stylisés (cast shadow teinté)  
- La configuration des boards sera faite par les artistes  
- Certains éléments du board doivent être en PBR (héros) mais interagir avec le lighting  
- Il faut pouvoir jouer un day/night à la fin de la partie. Le day/night doit pouvoir modifier l’ensemble du rendu du jeu  
- Bonus : gérer un système de météo  

### Contexte :
- La caméra est toujours en top-down et ne bouge presque pas (screen shake au maximum)  
- Les boards ne sont pas l’élément central du jeu et ne doivent donc pas monopoliser les performances du jeu  

## Déroulement du TP
Avant de commencer à explorer le sujet, formez des groupes de 2 ou 3.  
Vous allez brainstormer pendant 15/30 minutes afin d’évoquer toutes les pistes possibles.  
Faite une estimation de vos taches pour le producer  
Après ce brainstorming, vous passerez 5 minutes pour proposer les solutions proposées.  

### Ce que vous devez définir :
- Quel pipeline de rendu utiliser
- Quelle technique utiliser pour rendre les boards
- Quel va être le flow de création d’assets des artistes
- Comment implémenter le day/night system
- Comment rendre le tout optimisé

Nous discuterons ensuite de vos propositions et je vous montrerai la solution retenue pour Might and Magic Fates, en vous montrant quelques images publiques du jeu.  

À vous de jouer. Implémentez la solution que vous souhaiteriez dans un prototype.  
En fin de journée, nous prendrons 1h pour showcase votre travail, pour ceux qui le souhaitent, et nous donner un retour d’expérience sur le sujet.  

### IA
Comme dans un véritable contexte de production, vous aurez le droit à l’IA. Néanmoins, vous devrez maîtriser l’ensemble du code qu’elle vous fournit pour ne pas entraîner de dette technique dont l’impact serait lourd pour le projet. Ainsi, je pourrai faire des reviews de votre code et vous poser des questions concernant votre logique. Assurez-vous de toujours la maîtriser et de savoir ce que vous faites.
Conseil : utilisez-la comme un mentor ou pour générer des morceaux de code spécifiques.

## Sujet bonus :  
Réfléchissez maintenant à comment gérer, de façon simple et efficace, un système de graphic settings.
Rajoutez des effets sur les terrains : cloud shadow, végétation, vent, vent interactif, fog interactif, eau, eau interactive.
(Par interactif, j’entends qu’il doit se passer quelque chose lors du clic.)