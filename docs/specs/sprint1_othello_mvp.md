Jeu d'Othello, MVP
==================

Spécification fonctionnelle
---------------------------

# Propriétés du document

|               |                 |
| :------------ | :-------------: |
| Auteur        |    Sillynius    |
| Version       |       1.0       |
| Date          |    2025-12-18   |

# Historique des versions

|    Version    |      Date       |
| :-----------: | :-------------: |
|      1.0      |    2025-12-18   |

# Objet

Produire un MVP pour le jeu d'Othello qui servira à tester notre approche de TDD hybride.

Il consiste en une version terminal (pas de rendu graphique, juste du texte) du jeu. Donc à produire la logique pure d'une partie entre deux joueurs : l'utilisateur et une IA non stupide mais pouvant être battue par un joueur débutant.

Note : c'est une spec rédigée avec légèreté, pas de diagramme, fusion de certaines parties normalement séparées comme la liste des cas d'utilisation et leur spécification...

# Acteurs

* Le joueur humain (noté HU par la suite)
* L'IA (notée IA)

# Cas d'utilisations

## C1 - Lancer le jeu

HU doit appeler l'exécutable dans un terminal de type PowerShell sur Windows, ou Bash sur Linux.

**Nom de l'exécutable dans ce MVP** : othello
**Arguments de lancement** : aucun

```bash
./othello
```

## C2 - Lancer une première partie

La partie est lancée automatiquement au début de l'exécution.

## C3 - Tour de HU

* Les tours impairs (1er tour, 3e...) sont ceux de HU.
* HU entre la coordonnée du pion à poser, comme 'A1' (sans les guillemets)
* Il y a préalablement été invité par le texte 'à toi : ' et suivi d'aucun saut de ligne (pour économiser de l'espace dans une fenêtre de terminal limitée en caractères)
* Valider comme usuellement par la touche Entrée soumet la réponse
* Si poser le pion à la coordonnée désirée par HU est impossible (déjà un pion posé, ou placement invalide selon la règle du jeu d'Othello) alors le texte suivant est affiché à la ligne, invitant à donner de nouvelles coordonnées, autant de fois que nécessaire : 'Coup invalide, à toi : ', toujours sans saut de ligne suffixe.
* Si le coup est valide, le pion est visuellement placé et c'est au tout de IA

## C4 - Tour de IA

* Les tours pairs (2d tour, 4e...) sont ceux de IA.
* IA joue directement un coup, évidemment valide

## C5 - Remporter la partie

* Lorsque l'un des joueurs à retourné tous ceux de son adversaire, la partie est finie, et ce joueur gagne
* Lorsque plus aucun coup n'est possible, le joueur qui a le plus de pions de sa couleur gagne
* Est alors affiché, pour tout type de fin de partie :
> Victoire de XXX, YYY à ZZZ
Avec :
* XXX le nom du gagnant, une de ces deux valeurs : 'IA' si IA, 'Joueur' si HU
* YYY le score du gagnant (nombre de pions de sa couleur)
* ZZZ le score du perdant (nombre de pions de sa couleur)

## C6 - Relancer une partie

* En fin de partie, une nouvelle est automatiquement lancée
* Pas de texte introducteur

# Visualisation du plateau

## Dimensions

8x8

## Un case

* **une lettre de A à H** correspond à la coordonnée verticale d'un case se trouvant en-dessous
* **un chiffre de 1 à 8** correspond à la coordonnée horizontale d'un case se trouvant à sa droite
* **le caractère '.'** représente une case vide
* **le caractère 'O'** représente un pion de HU
* **le caractère 'X'** représente un pion de IA
* les cases sont espacées par le caractère ' ' horizontalement, header compris
* pas d'espacement horizontal

## Exemple de plateau : le plateau en début de partie

```
\ A B C D E F G H
1 . . . . . . . .
2 . . . . . . . .
3 . . . . . . . .
4 . . . O X . . .
5 . . . X O . . .
6 . . . . . . . .
7 . . . . . . . .
8 . . . . . . . .
```