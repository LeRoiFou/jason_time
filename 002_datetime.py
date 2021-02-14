"""
Chapitre 27 : gestion dates avec le module datetime
Lien : https://www.youtube.com/watch?v=SXgyLoGA_mY&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=27

Contrairement au module time, le module datetime permet d'effectuer des comparaisons, des calculs entre plusieurs temps

Éditeur : Laurent REYNAUD
Date : 27-10-2020
"""

import datetime

"""La fonction datetime est utilisée pour l'année, le mois, le jour, l'heure et les minutes : cette fonction hérite de 
la fonction date qui est expliquée ci-après"""
d1 = datetime.datetime(2020, 10, 27, 8, 15)  # année, mois, jour, heure, minute
print(d1)  # résultat : 2020-10-27 08:15:00

d2 = datetime.datetime(2020, 10, 25, 8, 15)  # changement de jour
print(d2)  # résultat : 2020-10-25 08:15:00

if d1 < d2:
    print(f'{d1} est plus ancien que {d2}')
else:
    print(f'{d1} est plus récent que {d2}')

"""La fonction date est utilisée pour l'année, le mois et le jour"""
d3 = datetime.date(2020, 10, 27)  # année, mois, jour
print(d3)  # résultat : 2020-10-27

d4 = datetime.date(2020, 10, 31)  # changement de jour
print(d4)  # résultat : 2020-10-31

if d3 < d4:
    print(f'{d3} est plus ancien que {d4}')
else:
    print(f'{d4} est plus récent que {d3}')

"""Fonctions year, month et day présents dans la fonction date"""
print(d3.year)  # résultat : 2020
print(d3.month)  # résultat : 10
print(d3.day)  # résultat : 27

"""Fonction time dans la fonction datetime"""
t1 = datetime.time(8, 28, 50)  # heure, minutes, secondes
print(t1)  # résultat : 08:28:50

"""Fonction now dans datetime : permet d'afficher le temps actuel avec l'heure, minutes et secondes alors que la 
fonction today dans date n'affiche pas l'heure, les minutes et les secondes"""
now = datetime.datetime.now()
print(now)  # résultat : 2020-10-27 08:31:52.228964

today = datetime.date.today()
print(today)  # résultat : 2020-10-27

birth = datetime.date(1977, 1, 12)
print(f"Age actuel : {today.year - birth.year} ans")  # résultat : Age actuel : 43 ans
