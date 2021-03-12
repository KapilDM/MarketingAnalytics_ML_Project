import pandas as pd

#Get dummies de Education y Marital_status: Esta es la funcion para ponerlo al final
def encode_OneHot(df,column):
    dummies = pd.get_dummies(df[column])
    df = pd.concat([df,dummies], axis=1)
    df = df.drop(column, axis=1)
    return df