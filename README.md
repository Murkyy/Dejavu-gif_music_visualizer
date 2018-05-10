# dejavu + gif_visualizer

Voici le code de notre projet de 2ème année CPBx.
Il réutilise les travaux suivants : https://github.com/worldveil/dejavu et https://github.com/basti2342/gif-music-visualizer

Une partie de l'explication du code de Dejavu est disponible dans notre mémoire sur les algorithmes de reconnaissance musicale.



Explication rapide des différentes parties:

Les fonctions servant pour Dejavu sont dans le dossier Dejavu.

Le dossier dejavu_test_results permet de stocker les diagrammes obtenus avec Dejavu.

Le dossier frames contient les gifs décomposés sous forme d'images numérotées.

example.py permet d'enregistrer des empreintes de musiques à la base de données, ou de lancer la reconnaissance.

dejavu.py contient la classe Dejavu et toutes les fonctions qui lui sont propre.

Projet artistique.py permet de reconnaitre une musique et de lancer un des visualiseurs selon son genre.

recorder.py sert au visualiseur.

run_tests.py permet de creer des diagrammes dans le dossier dejavu_test_results à partir de musiques qui seront découpées en morceaux de 1, 2, 3, 4 et 5 secondes.

visualizer_Classique.py ; visualizer_Electro.py ; visualizer_Metal.py ; visualizer_Reggae.py et visualizer_Rock.py sont appelées par Projet artistique.py
