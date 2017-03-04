# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:39:34 2017

@author: Rudolf MILLET
"""

import csv

services = open("../src/services.csv",encoding="utf8")
annonces = open("../src/annonces.csv",encoding="utf8")

reader_services = csv.reader(services)
reader_annonces = csv.reader(annonces)

liste_services = []
liste_annonces = []

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

#print(annonces_description)