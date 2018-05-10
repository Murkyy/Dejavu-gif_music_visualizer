# dejavu + gif_visualizer

Voici le code de notre projet de 2ème année CPBx.
Il réutilise les travaux suivants :https://github.com/worldveil/dejavu et https://github.com/basti2342/gif-music-visualizer

Une partie de l'explication du code de Dejavu est disponible dans notre mémoire.



Explication rapide des différentes parties:

Les fonctions servant pour Dejavu sont dans le dossier Dejavu

example.py permet d'enregistrer des empreintes de musiques à la base de données, ou de lancer la reconnaissance

dejavu.py contient la classe Dejavu et toutes les fonctions qui lui sont propre

Projet artistique.py permet de reconnaitre une musique et de lancer un des visualiseurs selon son genre.

recorder.py sert au visualiseur

visualizer_Classique.py ; visualizer_Electro.py ; visualizer_Metal.py ; visualizer_Reggae.py et visualizer_Rock.py sont appelées par Projet artistique.py
