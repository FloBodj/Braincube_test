# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 2020

@author: Florentin Bodjona

Sript demandé pour la question 3 du test de Braincube pour le stage de recherche

On réalise ici l'anonymisation des données nominales nom et ville en affectant à chaque valeur un entier 
"""

import pandas as pd
import os 

# Stockage des données dans la DataFrame donnees

donnees = pd.read_csv("depenses.csv")

# Initialisation des dictionnaires devant contenir les clés

id_noms = dict()
id_villes = dict()

# Remplissage des dictionnaires avec les clés et les entiers asscociés
# Le premier nom reçoit la valeur 1, ainsi de suite de sorte qu'il n'y ait pas de répétition

id_noms = {cle : id for id,cle in enumerate(donnees['nom']) 
           if cle not in id_noms.keys()}

# Toutes les villes reçoivent des valeurs entieres distinctes
# Les entiers ici ne débutent pas par 0 (??)

id_villes = {cle : id for id,cle in enumerate(donnees['ville']) 
           if cle not in id_villes.keys()}

# On remplace dans les colonnes nom et ville chaque valeur par l'entier qui y correspond

donnees['nom'] = donnees['nom'].apply(lambda x : id_noms[x])
donnees['ville'] = donnees['ville'].apply(lambda x : id_villes[x])


# Centrage et réduction des données ordinales age, salaire et dépenses

for i in range(2,5):
    # Calcul de la moyenne
    
    moyenne = donnees.iloc[:,i].mean()
    
    # Calcul de l'écart-type
    
    ecart_type = donnees.iloc[:,i].std()
    
    # Remplacement de chaque valeur par sa valeur centrée-réduite dans le tableau
    
    donnees.iloc[:,i] = donnees.iloc[:,i].apply(lambda x: (x - moyenne)/ecart_type)
    
# Stockage du résultat dans un fichier csv

donnees.to_csv('depenses_anonymes.csv', index = False)