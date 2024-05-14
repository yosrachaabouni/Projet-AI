
    title: Projet Géneration de variation d'images via un prompt
    authors:
        - Mohamed Aziz NABI
        - Yosra CHAABOUNI
        - Ahlem ELAYEB
    date: 2024-05-14
    geometry:
        - top=20mm
        - left=20mm
        - right=10mm
        - bottom=10mm
        - heightrounded
    bibliography: [biblio.bib]

![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)



## Sujet

On souhaite créer un programme qui est capable de génerer une variation d'une image. On lui fournit une `image d'origine`, un `prompt` de modification et l'IA fournis un prompt de sortie et l'image associée.Le but est la modification de style, la recontextualisation de personnages et d'objets.On est limité par les coûts à l'utilisation, et on peut uniquement utiliser `Azure` et `Open AI` (avec parcimonie).

## Etat de l'art

##### Objectif

Le projet vise à créer un programme capable de générer des variations d'images en fonction d'un prompt de modification, en utilisant les services Azure et OpenAI.

##### Contexte

Ce programme sera utilisé principalement pour la modification de style d'images, ainsi que la recontextualisation de personnages et d'objets. Par exemple, il pourrait être utilisé pour transformer une photo en un style artistique spécifique ou pour ajouter ou modifier des éléments dans une scène.

##### Contraintes

Nous devons tenir compte des coûts d'utilisation des services Azure et OpenAI, en nous assurant de les utiliser de manière efficiente. De plus, notre solution doit exclusivement utiliser les fonctionnalités fournies par ces deux plateformes.

## Architechture

L'architecture du programme peut être structurée comme suit :
##### Prétraitement de l'image :
- Redimensionnement et normalisation de l'image.
- Conversion de l'image dans un format compatible avec les API Azure et OpenAI.

##### Génération de Prompts :
- Analyse des besoins de l'utilisateur pour définir les modifications à apporter.
- Formulation de prompts précis adaptés aux modèles d'IA.

##### Utilisation de Modèles d'IA :

- Sélection des modèles appropriés en fonction des besoins spécifiques de modification d'image.
- Envoi des prompts et des images prétraitées aux modèles sélectionnés.

##### Traitement des Réponses des Modèles :
- Récupération et interprétation des résultats générés par les modèles d'IA.

##### Post-traitement des Résultats :
- Sélection de la meilleure variation en fonction des résultats des modèles et du prompt initial.
- Optimisation de l'image sélectionnée si nécessaire.

## Test

Lorem ipsum. `foobar` asdasdfasdfasdfasdsfasdf

Paragraph

> "Quand la vie nous donne des citrons..." -- Johnson

``` python
import tensorflow as tf
```

![Server Room](mra.jpg "Woman")