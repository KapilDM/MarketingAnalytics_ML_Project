import pandas as pd
import os
import sys
import numpy as np
import json

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)

from src.utils.models import encode_OneHot
from pickle import load
from sklearn.linear_model import LogisticRegression

def cambios_input_datos(df):
    """leemos csv, get dummies etc. y hacer la prediccion"""
    loaded_model2 = load(open(root_path +"\\models\\best_model.sav", "rb"))
    prediction = loaded_model2.predict(df)
    #print("Prediction======",type(prediction))
    # diccionario = {}
    # diccionario["prediction"] = prediction[-1][0]
    # prediction_df = pd.DataFrame(prediction)
    # prediction_df = prediction_df.to_json()
    return prediction #diccionario#prediction #diccionario#data #prediction


