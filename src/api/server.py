from flask import Flask,request,jsonify,render_template
import json
import os, sys
import pandas as pd
import numpy as np

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)

from src.utils.apis_tb import cambios_input_datos

app = Flask(__name__)

@app.route("/")
def home():
    EducationList = ["2n_Cycle","Basic","Graduation","Master","PhD"]
    MaritalList = ['Divorced', 'Single', 'Married', 'Together', 'Widow']
    return render_template("upload.html", EducationList=EducationList,MaritalList=MaritalList) 
    


with open(root_path + "\\data\\diction_Education_1.json") as f: 
    data_Educ = json.load(f)
with open(root_path + "\\data\\dicc_Marital_1.json") as f1:
  data_Marital = json.load(f1)



@app.route("/upload_form", methods = ['POST', 'GET'])
def upload_form():
    array_final = []
    if request.method == 'POST':
        Year = request.form['Year_Birth_text']

        x = request.form['Ed_level_resp'] 
        array_Education = np.array(data_Educ[x]) 
        x1 = request.form['Marital_resp']
        array_Marital = np.array(data_Marital[x1])

        income = request.form['Income_text']
        wines = request.form['wines_text']
        fruits = request.form['Fruits_text']
        meat = request.form['Meat_text']
        Fish = request.form['Fish_text']
        Sweets = request.form['Sweets_text']
        DiscountPurchases = request.form['DiscountPurchases_text']
        WebPurchases = request.form['WebPurchases_text']
        SalesAgentPurchases = request.form['SalesAgentPurchases_text']
        StorePurchases = request.form['StorePurchases_text']
        WebVisitsMonth = request.form['WebVisitsMonth_text']
        Campaign1 = request.form['Campaign1_text']
        Campaign2 = request.form['Campaign2_text']
        KidsHome = request.form['KidsHome_text']

        array_creado = [int(Year),float(income),int(wines),int(fruits),int(meat),int(Fish),int(Sweets),
        int(DiscountPurchases),int(WebPurchases),int(SalesAgentPurchases),int(StorePurchases),int(WebVisitsMonth),
        int(Campaign1),int(Campaign2),int(KidsHome)]

        array_final = np.concatenate((array_creado, array_Education, array_Marital), axis=None)
        X = array_final.reshape(1,-1)
        prediccion = cambios_input_datos(X)
        print("tipo de prediccion = ", type(prediccion[0]))
        condicion = prediccion[0]
        if condicion == 0:
            return "Prediccion = " + str(condicion) + "  ---------  El modelo a predicho que el cliente NO va a aceptar la campaña 3"
        else:
            return "Prediccion = " + str(condicion) + "  ---------  El modelo a predicho que el cliente SI va a aceptar la campaña 3"
                
    


@app.route("/token_id", methods=['GET']) 
def token_id():
    S = "K78700616"
    contrasenia = request.args["password"] 
    if (contrasenia == S):
        #json_b_group = n_d_averages_json()
        return "Go to: http://localhost:6060/upload"
    else:
        return "CONTRASEÑA INCORRECTA"


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=6060) 