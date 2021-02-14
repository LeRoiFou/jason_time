"""
Chapitre 28 : programmation asynchrone avec le module threading
Lien : https://www.youtube.com/watch?v=vdjZvxAI5d4&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=28

Utilisation de threads pour exécuter des tâches en parallèle dans un programme.

Exemple : affichage des données sous la forme d'un tableau tout en faisant en parallèle un tri des données au lieu que
le programme affiche d'abord les données sous la forme d'un tableau PUIS tri des données.

Autre exemple : dans un jeu vidéo la musique s'exécute en même temps que l'animation du personnage du jeu : il n'est pas
cohérent qu'on lance la musique puis dès que la musique s'arrête, l'animation du personnage du jeu s'exécute...

Par principe une fonction n'exécute qu'une seule tâche et les threads permettent justement d'exécuter plusieurs tâches
en même temps

Éditeur : Laurent REYNAUD
Date : 27-10-2020
"""
import time
import threading


def process_one():
    i = 0
    while i < 3:
        print('o' * 10)
        time.sleep(0.3)
        i += 1


def process_two():
    i = 0
    while i < 3:
        print('x' * 10)
        time.sleep(0.3)
        i += 1


"""Instructions pour exécuter des threads"""
th1 = threading.Thread(target=process_one)  # création d'un thread
th2 = threading.Thread(target=process_two)
th1.start()  # démarrage
th2.start()
th1.join()  # attente de l'un par rapport à l'autre
th2.join()
print('Fin des threads')
