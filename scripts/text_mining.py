# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:43:50 2017

@author: Rudolf MILLET
"""

import nltk
import csv

services = open("../src/services.csv",encoding="utf8")
annonces = open("../src/annonces.csv",encoding="utf8")

reader_services = csv.reader(services)
reader_annonces = csv.reader(annonces)

liste_services = []
liste_annonces = []

annonces_titre = []
annonces_description = []

counter_titre = []
counter_description = []

for row_services in reader_services:
    #print(row_services)
    ligne_services = ";".join(row_services)
    #print(ligne_services)
    tableau_services = ligne_services.split(";")
    #print(tableau_services)
    liste_services.append(tableau_services)
    
#print(liste_services)

for row_annonces in reader_annonces:
    #print(row_annonces)
    ligne_annonces = ",".join(row_annonces)
    #print(ligne_annonces)
    tableau_annonces = ligne_annonces.split(";")
    #print(tableau_annonces)
    #print("['"+tableau_annonces[0]+"', '"+tableau_annonces[2]+"', '"+tableau_annonces[6]+"', '"+tableau_annonces[12]+"', '"+tableau_annonces[13]+"', '"+tableau_annonces[14]+"']")
    liste_annonces.append(tableau_annonces)
    #print(tableau_annonces)
    counter_titre = nltk.FreqDist(tableau_annonces[6].split(" "))
    #print(counter_titre)
    annonces_titre.append(counter_titre)
    #print(annonces_titre)
    counter_description = nltk.FreqDist(tableau_annonces[7].split(" "))
    #print(counter_description)
    annonces_description.append(counter_description)
    #print(annonces_description)

#print(liste_annonces)
#print(annonces_titre)
#print(annonces_description)