# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:43:50 2017

@author: Rudolf MILLET
"""

import csv
import nltk
import pymongo
#import json
import itertools

# My Simple implementation of Levenshtein distance
def levenshtein_distance(string1, string2):
    """
    >>> levenshtein_distance('AATZ', 'AAAZ')
    1
    >>> levenshtein_distance('AATZZZ', 'AAAZ')
    3
    """
    distance = 0
    if len(string1) < len(string2):
        string1, string2 = string2, string1
    for i, v in itertools.zip_longest(string1, string2, fillvalue='-'):
        if i != v:
            distance += 1
    return distance
# from http://stackoverflow.com/questions/4173579/implementing-levenshtein-distance-in-python

"""
Declarations
"""

services = open("../src/services.csv",encoding="utf8")
annonces = open("../src/annonces.csv",encoding="utf8")

reader_services = csv.reader(services)
reader_annonces = csv.reader(annonces)

liste_services = []
liste_annonces = []

counter_titre = []
counter_description = []

liste_titre = []
liste_description = []

dico_services = {'Cours': 'Autres cours', 'devoirs': 'Autres cours', 'BREVET': 'Autres cours', 'COURS': 'Autres cours', 'Enseignante': 'Autres cours', 'Saxophone': 'Musique & Chant', 'maths': 'Mathématiques', 'physique': 'Sciences', 'chimie': 'Sciences', 'sciences': 'Sciences', 'SCOLAIRE': 'Autres cours', 'français': 'Français', 'Mercatique': 'Économie & Gestion', 'Economie': 'Économie & Gestion', 'Droit': 'Autres services de travaux', 'dessin': 'Arts', 'Beaux-Arts': 'Arts', 'langue': 'Langue', 'électronique': 'Informatique', 'informatique': 'Informatique', 'voiture': 'Dépannage & Réparation', 'Maths': 'Mathématiques', 'Physique': 'Sciences', 'Anglais': 'Langue', 'collège': 'Autres cours', 'lycée': 'Autres cours', 'Allemand': 'Langue', 'CP': 'Autres cours', 'CM2': 'Autres cours', 'Collège': 'Autres cours', 'Lycée': 'Autres cours', 'philosophie': 'Autres cours', 'arts': 'Arts', 'MATHS': 'Mathématiques', 'PRIMAIRE': 'Autres cours', 'anglais': 'Langue', 'littérature': 'Autres cours', 'Professeur': 'Autres cours', 'italien': 'Langue', 'grec': 'Langue', 'Grec': 'Langue', 'ANGLAIS': 'Langue', 'chant': 'Musique & Chant', 'danse': 'Danse', 'Gestion': 'Économie & Gestion', 'comptable': 'Économie & Gestion', 'comptabilité': 'Économie & Gestion', 'finance': 'Économie & Gestion', 'gestion': 'Économie & Gestion', 'piano': 'Musique & Chant', 'PHYSIQUE': 'Sciences', 'CHIMIE': 'Sciences', 'SVT': 'Sciences', 'Anglais': 'Langue', 'Italien': 'Langue', 'Economiques': 'Économie & Gestion', 'Sociologie': 'Autres cours', 'Mathématiques': 'Mathématiques', 'FRANÇAIS': 'Français', 'PHILOSOPHIE': 'Autres cours', 'Scolaire': 'Autres cours', 'scolaire': 'Autres cours', 'cours': 'Autres cours', 'espagnol': 'Langue', 'Primaire': 'Autres cours', 'secondaire': 'Autres cours', 'élève': 'Autres cours', 'saxophone': 'Musique & Chant', 'BTS': 'Autres cours', 'FLE': 'Langue', 'espagnol': 'Langue', 'DUT': 'Autres cours', 'littérature': 'Autres cours', 'CHIMIE': 'Sciences', 'TOEFL': 'Langue', 'TOEIC': 'Langue', 'Electronique': 'Informatique', 'Electrotechnique': 'Informatique', 'Mécanique': 'Bricolage', 'Comptabilité': 'Économie & Gestion', 'arabe': 'Langue', 'SES': 'Économie & Gestion', 'histoire': 'Histoire-Géographie', 'géographie': 'Histoire-Géographie', 'MATHÉMATIQUES': 'Mathématiques', 'mathématiques': 'Mathématiques', 'Arabe': 'Langue', 'PHYSIQUES': 'Sciences', 'Plat': 'Plats faits maison & Traiteurs', 'espagnol': 'Langue', 'flûte': 'Musique & Chant', 'PHP': 'Informatique', 'MySQL': 'Informatique', 'HTML': 'Informatique', 'CSS': 'Informatique', 'NTIC': 'Informatique', 'bureautique': 'Informatique', 'internet': 'Informatique', 'économie ': 'Économie & Gestion', 'Informatique': 'Informatique', 'ITALIEN': 'Langue', 'musique': 'Musique & Chant', 'ECJS': 'Autres cours', 'ALLEMAND': 'Langue', 'BIOLOGIE': 'Sciences', 'GEOLOGIE': 'Sciences', 'FRANCAIS': 'Français', 'hébreu': 'Langue', 'PROGRAMMATION': 'Informatique', 'SAXOPHONE': 'Musique & Chant', 'FLÛTE': 'Musique & Chant', 'électricité': 'Informatique', 'salsa': 'Danse', 'bachata': 'Danse', 'chachacha': 'Danse', 'CHINOIS': 'Langue', 'Chant': 'Musique & Chant', 'Piano': 'Musique & Chant', 'chinois': 'Langue', 'CAO': 'Informatique', 'DAO': 'Informatique', 'Graphisme': 'Autres cours', 'MECANIQUE': 'Bricolage', 'solfège': 'Musique & Chant', 'Chinois': 'Langue', 'Economie': 'Économie & Gestion', 'Professeur': 'Autres cours', 'PROFESSEUR': 'Autres cours', 'Géo': 'Histoire-Géographie', 'Histoire': 'Histoire-Géographie', 'CHANT': 'Musique & Chant', 'concours': 'Autres cours', 'CPGE': 'Autres cours', 'guitare': 'Musique & Chant', 'info': 'Informatique', 'Installation': 'Autres services aux entreprises', 'Conseils': 'Autres services aux entreprises', 'Récupération': 'Autres services de travaux', 'latin': 'Langues anciennes', 'Latin': 'Langues anciennes', 'Traductions': 'Autres services aux entreprises', 'ESPAGNOL': 'Langue', 'CHIEN': 'Vie quotidienne-Autres', 'gîte': 'Gîtes', 'ITALIEN': 'Langue', 'CV': 'Autres services aux entreprises', 'Télésecrétaire': 'Autres services aux entreprises', 'service': 'Autres services aux entreprises', 'Service': 'Autres services aux entreprises', 'russe': 'Langue', 'English': 'Langue', 'MATH': 'Mathématiques', 'CONCOURS': 'Autres cours', 'installation': 'Autres services aux entreprises', 'dépannage': 'Dépannage & Réparation', 'investir': 'Investissement & Levée de fond', 'immobilier': 'Autres services de travaux', 'Assistante': 'Autres services aux entreprises', 'Voiture': 'Autres services de travaux', 'location': 'Vie quotidienne-Autres', 'GEOPOLITIQUE': 'Autres cours', 'ECONOMIE': 'Économie & Gestion', 'COMMERCE': 'Économie & Gestion', 'MANAGEMENT': 'Économie & Gestion', 'COLLÈGE': 'Autres cours', 'LYCEE': 'Autres cours', 'Programmeur': 'Informatique', 'INFORMATIQUE': 'Informatique', 'Nettoyage': 'Nettoyage & Entretien', 'Formation': 'Autres cours', 'ordinateur': 'Informatique', 'Webmaster': 'Autres services aux entreprises', 'Conseil': 'Autres services aux entreprises', 'DESSIN': 'Autres cours'}
dico_data = {}

annonce_intermediaire = []
k = 0 # min annonce_intermediaire
l = -1 # max annonce_intermediaire
categorie_intermediaire = []
i = 0 # min categorie_intermediaire
j = -1 # max categorie_intermediaire
change = False

"""
Algorithms
"""

for row_services in reader_services: # lecture des services
    #print(row_services)
    ligne_services = ";".join(row_services) # concatenation
    #print(ligne_services)
    tableau_services = ligne_services.split(";") # split
    #print(tableau_services)
    liste_services.append(tableau_services)

#print(liste_services)

for row_annonces in reader_annonces: # lecture des annonces
    #print(row_annonces)
    ligne_annonces = ",".join(row_annonces)
    #print(ligne_annonces)
    tableau_annonces = ligne_annonces.split(";")
    #print(tableau_annonces)
    #print("['"+tableau_annonces[0]+"', '"+tableau_annonces[2]+"', '"+tableau_annonces[6]+"', '"+tableau_annonces[12]+"', '"+tableau_annonces[13]+"', '"+tableau_annonces[14]+"']")
    counter_titre = nltk.FreqDist(tableau_annonces[6].split(" ")) # compte le nombre d occurence de chaque mot
    #print(counter_titre)
    liste_titre.append(counter_titre)
    #print(liste_titre)
    counter_description = nltk.FreqDist(tableau_annonces[7].split(" ")) # compte le nombre d occurence de chaque mot
    #print(counter_description)
    liste_description.append(counter_description)
    #print(liste_description)
    occ = 0 # nombre occurence du mot
    for cle in dico_services.keys(): # pour chaque key du dictionnaire
        #print(cle)
        #print(occ)
        if cle in tableau_annonces[6] or cle in tableau_annonces[7]: # si la key est dans le titre ou la description
            #print(cle)l
            if counter_titre[cle] + counter_description[cle] > occ: # si l occurence de la key est la plus elevee
                #print(counter_titre[cle] + counter_description[cle])
                occ = counter_titre[cle] + counter_description[cle] # MAJ occurence
                #print(occ)
                if len(tableau_annonces) == 17: # si pas de categorie
                    tableau_annonces.append(dico_services.get(cle)) # rentre le service
                    #print(dico_services.get(cle))
                elif len(tableau_annonces) == 18 and dico_services.get(cle) != "Autres cours": # si deja une categorie
                    tableau_annonces[17] = dico_services.get(cle) # rentre le service
                    #print(dico_services.get(cle))
        else : # si la key n est pas dans le titre ou la description
            for word in tableau_annonces[6]: # pour chaque mot du titre
                if levenshtein_distance(cle, word) < 3: # distance de levenshtein
                    if counter_titre[cle] > occ: # si l occurence de la key est la plus elevee
                        #print(counter_titre[cle])
                        occ = counter_titre[cle] # MAJ occurence
                        #print(occ)
                        if len(tableau_annonces) == 17: # si pas de categorie
                            tableau_annonces.append(dico_services.get(cle)) # rentre le service
                            #print(dico_services.get(cle))
                        elif len(tableau_annonces) == 18 and dico_services.get(cle) != "Autres cours": # si deja une categorie
                            tableau_annonces[17] = dico_services.get(cle) # rentre le service
                            #print(dico_services.get(cle))
            for word in tableau_annonces[7]: # pour chaque mot de la description
                if levenshtein_distance(cle, word) < 3: # distance de levenshtein
                    if counter_description[cle] > occ: # si l occurence de la key est la plus elevee
                        #print(counter_description[cle])
                        occ = counter_description[cle] # MAJ occurence
                        #print(occ)
                        if len(tableau_annonces) == 17: # si pas de categorie
                            tableau_annonces.append(dico_services.get(cle)) # rentre le service
                            #print(dico_services.get(cle))
                        elif len(tableau_annonces) == 18 and dico_services.get(cle) != "Autres cours": # si deja une categorie
                            tableau_annonces[17] = dico_services.get(cle) # rentre le service
                            #print(dico_services.get(cle))
    if len(tableau_annonces) == 17: # si pas de categorie
        tableau_annonces.append('null') # pas de categorie
    liste_annonces.append(tableau_annonces)
    #print(tableau_annonces)

#print(liste_titre)
#print(liste_description)
#print(liste_annonces)

for service in liste_services: # redaction du dico/JSON
    #print(service[4])
    for annonce in liste_annonces:
        #print(annonce)
        if service[4] == annonce[17]: # match            
            #print(annonce[17])
            annonce_intermediaire.append(annonce[0]) # id
            #print(annonce[0])
            annonce_intermediaire.append(annonce[2]) # pseudo
            #print(annonce[2])
            annonce_intermediaire.append(annonce[6]) # titre
            #print(annonce[6])
            annonce_intermediaire.append(annonce[7]) # description
            #print(annonce[7])
            annonce_intermediaire.append(annonce[8]+" € "+annonce[9]) # tarif
            #print(annonce[8]+" € "+annonce[9])
            annonce_intermediaire.append(annonce[11]) # date
            #print(annonce[11])
            annonce_intermediaire.append(annonce[12]) # lat
            #print(annonce[12])
            annonce_intermediaire.append(annonce[13]) # long
            #print(annonce[13])
            annonce_intermediaire.append(annonce[14]) # libelle
            #print(annonce[14])
            #print(annonce_intermediaire)
            l += 9 # augmentation intervalle fin 9 en 9
            #print(l)
            categorie_intermediaire.append(annonce_intermediaire[k:l+1])
            #print(annonce_intermediaire[k:l+1])
            j += 1 # augmentation intervalle fin 1 en 1
            #print(j)
            k = l + 1 # augmentation intervalle debut
            #print(k)
            change = True # ajout
        #print(categorie_intermediaire)
    if change: # si ajout
        dico_data[service[4]] = categorie_intermediaire[i:j+1]
        #print(categorie_intermediaire[i:j+1])
        i = j + 1 # augmentation intervalle debut
        #print(i)
        change = False # reinitialisation

#print(dico_data)

#json_data = json.dumps(dico_data) # JSON
#print(json_data)

#client = pymongo.MongoClient('212.194.0.132',27117) # raspi1
client = pymongo.MongoClient('127.0.0.1',27017) # localhost
print(client)
db = client.services # database
print(db)
result = db.annonces.delete_many({})
print("Suppression ", result)
post_id = db.annonces.insert_one(dico_data).inserted_id # collection : annonces
print("Identifiant ", post_id)
client.close()