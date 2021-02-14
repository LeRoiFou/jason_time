"""
Chapitre 26 : gestion temps avec le module time et la traduction en français avec le module locale
Lien : https://www.youtube.com/watch?v=C0LmHQkJUs4&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=26

Éditeur : Laurent REYNAUD
Date : 27-10-2020
"""
import time
import locale

"""Fonction mettant en pause un programme"""
print('le premier texte')
time.sleep(2)  # pause de 2 secondes
print('le second texte')

"""Secondes écoulées depuis le 01-01-1970 à 00h00 (timestamp)"""
print(time.time())  # affichage des secondes écoulées
begin = time.time()
time.sleep(2)  # pause de 2 secondes
end = time.time()
print(
    f"Temps écoulé : {end - begin} secondes")  # affichage du temps écoulé qui ne sera pratiquement pas de 2 secondes...

"""Affichage du temps actuel avec tm_wday = n° jour de la semaine en partant de 0 pour lundi, 1 pour mardi...,  
tm_yday = nbre de jours écoulés depuis le 01-01-n, et tm_isdst = décalage horaire (heure d'hiver = 0) 
                                    localtime() 
Timestamp                   -------------------------->             Structure de temps 
                            <-------------------------- 
                                    mktime() 
"""
tps = time.localtime()
print(tps)  # affichage du temps actuel (structure de temps)
tps = time.mktime(tps)
print(tps)  # retour à l'affichage des secondes écoulées depuis le 01-01-1970 (timestamp)

""" 
La fonction strftime permet d'affichage le jour, le mois, l'année... 
%S = secondes (00 à 59) 
%I = minutes (00 à 59) 
%H = heures (00 à 24) 
%p = matin / après-midi (AM / PM) 
%d = jour (01 à 31) 
%a = jour de la semaine en abrégé 
%A = jour de la semaine 
%m = mois (01 à 12) 
%b = mois en abrégé 
%B = mois en toutes lettres 
%y = année avec 2 chiffres (ex : 20) 
%Y = année avec 4 chiffres (ex : 2020) 
%Z = fuseau horaire (ex: Paris, Madrid) 
"""
print(time.strftime('%d %A %B %Y'))  # affichage jour mois année en anglais
locale.setlocale(locale.LC_TIME, 'FR')  # traduction de toutes les données affichées du module time en français
print(time.strftime('%A %d %B %Y %Z'))  # affichage jour mois année en français avec le fuseau horaire
