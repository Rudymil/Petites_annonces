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

for row in reader_services:
    #print(row)
    ligne_services = ";".join(row)
    #print(ligne_services)
    tableau_services = ligne_services.split(";")
    print(tableau_services)

for row in reader_annonces:
    #print(row)
    ligne_annonces = ",".join(row)
    #print(ligne_annonces)
    tableau_annonces = ligne_annonces.split(";")
    #print(tableau_annonces)
    print("['"+tableau_annonces[0]+"', '"+tableau_annonces[2]+"', '"+tableau_annonces[6]+"', '"+tableau_annonces[12]+"', '"+tableau_annonces[13]+"', '"+tableau_annonces[14]+"']")