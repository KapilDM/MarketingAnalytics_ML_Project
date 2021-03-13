import pandas as pd
import os
import sys
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)


def checking_outliers(df,columns):
    lista = ['Year_Birth','Income','Wines','Fruits','Meat','Fish','Sweets','DiscountPurchases','WebPurchases','SalesAgentPurchases','StorePurchases','WebVisitsMonth']
    acum = 0
    f, axs = plt.subplots(3,4,figsize=(12,11))
    for i in range(3):
        for j in range(4):
            df[lista[acum]].plot(kind='box', ax=axs[i,j])
            acum = acum +1    
        f.tight_layout()
    plt.show()

def year_range(df):
    """Visualizing year range"""
    df_visualization = df.copy()
    df_visualization["Year_Birth_Range"] = pd.cut(df_visualization["Year_Birth"],4,  precision=0)
    g_bin=df_visualization.groupby(df_visualization["Year_Birth_Range"]).count()
    ax = plt.figure()
    sns.set_style("whitegrid")
    ax = sns.barplot(x=g_bin.index, y=g_bin["Year_Birth"],palette="rocket")
    plt.title("Company´s Client Birth Ranges", fontdict={"fontweight":"bold"},fontsize="large")
    plt.xlabel("Year Birth Range")
    plt.ylabel("Total Clients")
    plt.xticks(fontweight="bold")
    plt.savefig(root_path + "\\reports\\year_range.png")
    plt.show()

def income_range(df):
    """Visualizing income range"""
    df_visualization = df.copy()
    df_visualization["Income_rangos"] = pd.cut(df_visualization["Income"],4,  precision=0)
    g_bin=df_visualization.groupby(df_visualization["Income_rangos"]).count()
    ax = plt.figure()
    sns.set_style("whitegrid")
    ax = sns.barplot(x=g_bin.index, y=g_bin["Income"],palette="rocket")
    plt.title("Company´s Client Income Ranges", fontdict={"fontweight":"bold"},fontsize="large")
    plt.xlabel("Income Range")
    plt.ylabel("Total Clients")
    plt.xticks(rotation="90",fontweight="bold",fontsize="medium")
    plt.savefig(root_path + "\\reports\\income_range.png")
    plt.show()


def function_unique_plots(df,columns):
    """Automatically visualizing few unique value plots"""
    sns.set_theme(style="darkgrid")
    fig, ax = plt.subplots(nrows=(int(len(columns) / 2)), ncols=2 , figsize = (8, 8))
    ax = ax.flatten()
    for pos, val in enumerate(columns):
        sns.countplot(x = val, data = df, ax = ax[pos],palette="rocket") 
    plt.savefig(root_path + "\\reports\\unique_plots.png")
    fig.tight_layout()

def media_columnas(data,cols):
    """Calculates mean value of a column"""
    lista = []
    for pos,val in enumerate(cols):
        lista.append(data[val].mean())
    return lista

def suma_total_columnas(data,cols):
    lista1 = []
    for pos,val in enumerate(cols):
        lista1.append(data[val].sum())
    return lista1


def mean_amount_spent(df,cols):
    datos = df.copy()
    lista = media_columnas(data=datos,cols=cols)
    list_of_tuples = list(zip(cols, lista))   
    df_MntProducts = pd.DataFrame(list_of_tuples, columns = ['Products', 'MeanAmountSpent'])  
    df_MntProducts = df_MntProducts.sort_values(by='MeanAmountSpent',ascending=False)
    ax = plt.figure(figsize=(7,3))
    ax = sns.barplot(x=df_MntProducts["Products"], y=df_MntProducts["MeanAmountSpent"],palette="rocket")
    plt.title("Mean amount spent per product", fontdict={"fontweight":"bold"})
    plt.xlabel("Products", fontdict={"fontweight":"bold"})
    plt.ylabel("Amount Spent", fontdict={"fontweight":"bold"})
    plt.savefig(root_path + "\\reports\\mean_amount_spent.png")
    plt.show()


def ways_purchase(df,cols):
    datos1 = df.copy()
    lista1 = suma_total_columnas(data=datos1,cols=cols)
    #Creating dataframe to plot values
    list_of_tuples1 = list(zip(cols, lista1))   
    df_purchases = pd.DataFrame(list_of_tuples1, columns = ['Purchase_Type', 'TotalPurchase'])  
    df_purchases = df_purchases.sort_values("TotalPurchase",ascending=False)
    #Grafica
    colors = ["#3F0245","#7A2D81", "#A56AAB", "#C197C6", "#E9D9EB"]
    plt.pie(df_purchases["TotalPurchase"], labels= df_purchases["Purchase_Type"],colors=colors, autopct="%.1f %%")  
    plt.title("Time needed for each project step")
    plt.savefig(root_path + "\\reports\\ways_purchases.png")
    plt.show()


def campaigns_accepted(df,cols):
    datos = df.copy()
    lista = media_columnas(data=datos,cols=cols)
    #Creating dataframe to plot values
    list_of_tuples = list(zip(cols, lista))   
    df_MntProducts = pd.DataFrame(list_of_tuples, columns = ['Campaigns', 'Total_Campign_Acceptance'])  
    df_MntProducts
    ax = plt.figure(figsize=(7,3))
    ax = sns.barplot(x=df_MntProducts['Campaigns'], y=df_MntProducts['Total_Campign_Acceptance'],palette="rocket")
    plt.title("Campaign Analysis", fontdict={"fontweight":"bold"})
    plt.xlabel("Year Campaigns", fontdict={"fontweight":"bold"})#},fontsize="large")
    plt.ylabel("Campaign Acceptance/Purchases", fontdict={"fontweight":"bold"})
    plt.savefig(root_path + "\\reports\\campaigns_accepted.png")
    plt.show()

def project_step_time():
    "Pie chart to show the time spent on each step of the project"
    Research = 10
    Data_Wrangling = 10
    Data_Mining = 35
    Visualization = 20
    Machine_learning = 35
    labels = ["Research", "Data Wrangling", "Data Mining","Visualization","Machine Learning"]
    colors = ["#A56AAB","#C197C6", "#A56AAB", "#E9D9EB", "#C197C6"]
    plt.pie([Research,Data_Wrangling, Data_Mining, Visualization,Machine_learning], labels= labels,colors=colors, autopct="%.1f %%")    
    plt.title("Time needed for each project step")
    #plt.savefig(root_path + "\\resources\\project_step_time.png")
    plt.show()