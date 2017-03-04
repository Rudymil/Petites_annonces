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

dico_services = {'Cours': 'Autres cours', 'devoirs': 'Autres cours', 'BREVET': 'Autres cours', 'COURS': 'Autres cours', 'Enseignante': 'Autres cours', 'Saxophone': 'Musique & Chant', 'maths': 'Mathématiques', 'physique': 'Sciences', 'chimie': 'Sciences', 'sciences': 'Sciences', 'SCOLAIRE': 'Autres cours', 'français': 'Français', 'Mercatique': 'Économie & Gestion', 'Economie': 'Économie & Gestion', 'Droit': 'Autres services de travaux', 'dessin': 'Arts', 'Beaux-Arts': 'Arts', 'langue': 'Langue', 'électronique': 'Informatique', 'informatique': 'Informatique', 'voiture': 'Dépannage & Réparation', 'Maths': 'Mathématiques', 'Physique': 'Sciences', 'Anglais': 'Langue', 'collège': 'Autres cours', 'lycée': 'Autres cours', 'Allemand': 'Langue', 'CP': 'Autres cours', 'CM2': 'Autres cours', 'Collège': 'Autres cours', 'Lycée': 'Autres cours', 'philosophie': 'Autres cours', 'arts': 'Arts', 'MATHS': 'Mathématiques', 'PRIMAIRE': 'Autres cours', 'anglais': 'Langue', 'littérature': 'Autres cours', 'Professeur': 'Autres cours', 'italien': 'Langue', 'grec': 'Langue', 'Grec': 'Langue', 'ANGLAIS': 'Langue', 'chant': 'Musique & Chant', 'danse': 'Danse', 'Gestion': 'Économie & Gestion', 'comptable': 'Économie & Gestion', 'comptabilité': 'Économie & Gestion', 'finance': 'Économie & Gestion', 'gestion': 'Économie & Gestion', 'piano': 'Musique & Chant', 'PHYSIQUE': 'Sciences', 'CHIMIE': 'Sciences', 'SVT': 'Sciences', 'Anglais': 'Langue', 'Italien': 'Langue', 'Economiques': 'Économie & Gestion', 'Sociologie': 'Autres cours', 'Mathématiques': 'Mathématiques', 'FRANÇAIS': 'Français', 'PHILOSOPHIE': 'Autres cours', 'Scolaire': 'Autres cours', 'scolaire': 'Autres cours', 'cours': 'Autres cours', 'espagnol': 'Langue', 'Primaire': 'Autres cours', 'secondaire': 'Autres cours', 'élève': 'Autres cours', 'saxophone': 'Musique & Chant', 'BTS': 'Autres cours', 'FLE': 'Langue', 'espagnol': 'Langue', 'DUT': 'Autres cours', 'littérature': 'Autres cours', 'CHIMIE': 'Sciences', 'TOEFL': 'Langue', 'TOEIC': 'Langue', 'Electronique': 'Informatique', 'Electrotechnique': 'Informatique', 'Mécanique': 'Bricolage', 'Comptabilité': 'Économie & Gestion', 'arabe': 'Langue', 'SES': 'Économie & Gestion', 'histoire': 'Histoire-Géographie', 'géographie': 'Histoire-Géographie', 'MATHÉMATIQUES': 'Mathématiques', 'mathématiques': 'Mathématiques', 'Arabe': 'Langue', 'PHYSIQUES': 'Sciences', 'Plat': 'Plats faits maison & Traiteurs', 'espagnol': 'Langue', 'flûte': 'Musique & Chant', 'PHP': 'Informatique', 'MySQL': 'Informatique', 'HTML': 'Informatique', 'CSS': 'Informatique', 'NTIC': 'Informatique', 'bureautique': 'Informatique', 'internet': 'Informatique', 'économie ': 'Économie & Gestion', 'Informatique': 'Informatique', 'ITALIEN': 'Langue', 'musique': 'Musique & Chant', 'ECJS': 'Autres cours', 'ALLEMAND': 'Langue', 'BIOLOGIE': 'Sciences', 'GEOLOGIE': 'Sciences', 'FRANCAIS': 'Français', 'hébreu': 'Langue', 'PROGRAMMATION': 'Informatique', 'SAXOPHONE': 'Musique & Chant', 'FLÛTE': 'Musique & Chant', 'électricité': 'Informatique', 'salsa': 'Danse', 'bachata': 'Danse', 'chachacha': 'Danse', 'CHINOIS': 'Langue', 'Chant': 'Musique & Chant', 'Piano': 'Musique & Chant', 'chinois': 'Langue', 'CAO': 'Informatique', 'DAO': 'Informatique', 'Graphisme': 'Autres cours', 'MECANIQUE': 'Bricolage', 'solfège': 'Musique & Chant', 'Chinois': 'Langue', 'Economie': 'Économie & Gestion', 'Professeur': 'Autres cours', 'PROFESSEUR': 'Autres cours', 'Géo': 'Histoire-Géographie', 'Histoire': 'Histoire-Géographie', 'CHANT': 'Musique & Chant', 'concours': 'Autres cours', 'CPGE': 'Autres cours', 'guitare': 'Musique & Chant', 'info': 'Informatique', 'Installation': 'Autres services aux entreprises', 'Conseils': 'Autres services aux entreprises', 'Récupération': 'Autres services de travaux', 'latin': 'Langues anciennes', 'Latin': 'Langues anciennes', 'Traductions': 'Autres services aux entreprises', 'ESPAGNOL': 'Langue', 'CHIEN': 'Vie quotidienne-Autres', 'gîte': 'Gîtes', 'ITALIEN': 'Langue', 'CV': 'Autres services aux entreprises', 'Télésecrétaire': 'Autres services aux entreprises', 'service': 'Autres services aux entreprises', 'Service': 'Autres services aux entreprises', 'russe': 'Langue', 'English': 'Langue', 'MATH': 'Mathématiques', 'CONCOURS': 'Autres cours', 'installation': 'Autres services aux entreprises', 'dépannage': 'Dépannage & Réparation', 'investir': 'Investissement & Levée de fond', 'immobilier': 'Autres services de travaux', 'Assistante': 'Autres services aux entreprises', 'Voiture': 'Autres services de travaux', 'location': 'Vie quotidienne-Autres', 'GEOPOLITIQUE': 'Autres cours', 'ECONOMIE': 'Économie & Gestion', 'COMMERCE': 'Économie & Gestion', 'MANAGEMENT': 'Économie & Gestion', 'COLLÈGE': 'Autres cours', 'LYCEE': 'Autres cours', 'Programmeur': 'Informatique', 'INFORMATIQUE': 'Informatique', 'Nettoyage': 'Nettoyage & Entretien', 'Formation': 'Autres cours', 'ordinateur': 'Informatique', 'Webmaster': 'Autres services aux entreprises', 'Conseil': 'Autres services aux entreprises', 'DESSIN': 'Autres cours'}

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