import pandas as pd



def encode_OneHot(df,column):
    """Get dummies function"""
    dummies = pd.get_dummies(df[column])
    df = pd.concat([df,dummies], axis=1)
    df = df.drop(column, axis=1)
    return df