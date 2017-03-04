# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:43:50 2017

@author: Rudolf MILLET
"""

import nltk
import csv

#services = open("../src/services.csv",encoding="utf8")
annonces = open("../src/annonces.csv",encoding="utf8")

#reader_services = csv.reader(services)
reader_annonces = csv.reader(annonces)

#liste_services = []
liste_annonces = []

counter_titre = []
counter_description = []

liste_titre = []
liste_description = []

dico_services = {'cours': 'Autres cours', 'Saxophone': 'Musique & Chant', 'physique': 'Sciences', 'chimie': 'Sciences', 'maths': 'Mathématiques', 'français': 'Français', 'dessin': 'Arts', 'Beaux-Arts': 'Arts', 'électronique': 'Informatique', 'informatique': 'Informatique', 'voiture': 'Bricolage & Entretien', 'Droit': 'Économie & Gestion', 'Maths': 'Mathématiques', 'scolaire': 'Autres cours', 'langue': 'Langue', 'Physique': 'Sciences', 'Anglais': 'Langue', 'collège': 'Autres cours', 'lycée': 'Autres cours', 'Allemand': 'Langue', 'histoire-géo': 'Histoire-Géographie', 'arts': 'Arts', 'bureautique': 'Économie & Gestion', 'grec': 'Langue', 'chant': 'Musique & Chant', 'danse': 'Danse', 'Gestion': 'Économie & Gestion', 'comptabilité': 'Économie & Gestion', 'PHYSIQUE': 'Sciences', 'MATHS': 'Mathématiques', 'CHIMIE': 'Sciences', 'SVT': 'Sciences', 'Italien': 'Langue'}

#for row_services in reader_services:
    #print(row_services)
    #ligne_services = ";".join(row_services)
    #print(ligne_services)
    #tableau_services = ligne_services.split(";")
    #print(tableau_services)
    #liste_services.append(tableau_services)

#print(liste_services)

for row_annonces in reader_annonces:
    #print(row_annonces)
    ligne_annonces = ",".join(row_annonces)
    #print(ligne_annonces)
    tableau_annonces = ligne_annonces.split(";")
    #print(tableau_annonces)
    #print("['"+tableau_annonces[0]+"', '"+tableau_annonces[2]+"', '"+tableau_annonces[6]+"', '"+tableau_annonces[12]+"', '"+tableau_annonces[13]+"', '"+tableau_annonces[14]+"']")
    counter_titre = nltk.FreqDist(tableau_annonces[6].split(" "))
    #print(counter_titre)
    liste_titre.append(counter_titre)
    #print(liste_titre)
    counter_description = nltk.FreqDist(tableau_annonces[7].split(" "))
    #print(counter_description)
    liste_description.append(counter_description)
    #print(liste_description)
    occ = 0 # nombre occurence du mot
    for cle in dico_services.keys():
        #print(cle)
        #print(occ)
        if cle in tableau_annonces[6] or cle in tableau_annonces[7]:
            #print(cle)
            if counter_titre[cle] + counter_description[cle] > occ:
                #print(counter_titre[cle] + counter_description[cle])
                occ = counter_titre[cle] + counter_description[cle]
                #print(occ)
                if len(tableau_annonces) == 17: # si pas de categorie
                    tableau_annonces.append(dico_services.get(cle))
                    #print(dico_services.get(cle))
                elif len(tableau_annonces) == 18 and dico_services.get(cle) != "Autres cours": # si deja une categorie
                    tableau_annonces[17] = dico_services.get(cle)
                    #print(dico_services.get(cle))
    liste_annonces.append(tableau_annonces)
    #print(tableau_annonces)

#print(liste_titre)
#print(liste_description)
#print(liste_annonces)