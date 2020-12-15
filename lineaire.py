# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 2020

@author: Florentin Bodjona

Sript demandé pour la question 4 du test de Braincube pour le stage de recherche

On réalise ici des prédictions (utilisant la regression linéaire) des depenses en fonction :
    1. des salaires
    2. de l'âge et des salaires
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Stockage des données dans la DataFrame donnees

donnees = pd.read_csv("depenses.csv")

# Le modèle de regression linéaire

model = LinearRegression()

# Prédiction des dépenses à partir du salaire

# Sélection de l'entrée
# Redimensionnement pour avoir un tableau numpy 2D

entrees = np.array(donnees.iloc[:,3]).reshape(-1,1)

# Ajustement du modèle

model.fit(entrees, donnees.iloc[:,4])

# Prédiction et stockage dans donnees

donnees['prediction_depenses'] = model.predict(entrees)

# Stockage dans un csv

donnees.iloc[:,[3,4,5]].to_csv( 'predictions_1.csv', index = False)

# Prédiction des dépenses à partir de l'âge et du salaire

# Sélection des entrées

entrees = donnees.loc[:,['age','salaire']]

# Ajustement du modèle

model.fit(entrees, donnees.iloc[:,4])

# Prédiction et stockage dans donnees

donnees['prediction2_depenses'] = model.predict(entrees)

# Stockage dans un csv

donnees.iloc[:,[0,1,2,3,4,6]].to_csv( 'predictions_2.csv', index = False)