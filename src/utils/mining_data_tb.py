import pandas as pd
import os
import sys
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)

def dropping_columns(df,columns):
    for i in columns:
        df = df.drop([i],axis=1)
    return df

def dropping_rows(df,column,rows):
    for i in rows:
        df.drop(df[df[column] == i].index,inplace=True)
    return df

def adding_columns(df,column1,column2,new_column_name):
    df_nuevo = pd.DataFrame([df[column1],df[column2]]).transpose()
    df_nuevo[new_column_name] = df_nuevo.sum(axis=1)
    df[new_column_name] = df_nuevo[new_column_name]
    df = df.drop([column1,column2],axis=1)
    return df

def currency_to_numeric(df,column):
    #Transforming Income column (string) to float
    df[column] = df[column].str.replace('$', '')
    df[column] = df[column].str.replace(',', '')
    df[column] = df[column].astype("float")
    return df
