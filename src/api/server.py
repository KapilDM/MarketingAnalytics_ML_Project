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
    #Voy a upload.html y cojo la respuesta, al pinchar en submit, me lleva directamente a /upload_form ya 
    #que lo pone en html


with open(root_path + "\\data\\diction_Education_1.json") as f: #Intentando que funcione lo anterior
    data_Educ = json.load(f)
with open(root_path + "\\data\\dicc_Marital_1.json") as f1:
  data_Marital = json.load(f1)



@app.route("/upload_form", methods = ['POST', 'GET'])
def upload_form():
    array_final = []
    if request.method == 'POST':
        Year = request.form['Year_Birth_text']

        x = request.form['Ed_level_resp'] #x es el valor que yo le meto en el desplegable (str)
        array_Education = np.array(data_Educ[x]) # accedo al json de x (opcion elegida por mi) = [1, 0, 0, 0, 0]
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
        Campaign4 = request.form['Campaign4_text']
        Campaign5 = request.form['Campaign5_text']
        KidsHome = request.form['KidsHome_text']

        array_creado = [int(Year),float(income),int(wines),int(fruits),int(meat),int(Fish),int(Sweets),
        int(DiscountPurchases),int(WebPurchases),int(SalesAgentPurchases),int(StorePurchases),int(WebVisitsMonth),
        int(Campaign4),int(Campaign5),int(KidsHome)]

        array_final = np.concatenate((array_creado, array_Education, array_Marital), axis=None)
        X = array_final.reshape(1,-1)
        prediccionnn = cambios_input_datos(X)
        print("prediccionnnn == ",prediccionnn)

    return "prediction = " + str(prediccionnn)


@app.route("/token_id", methods=['GET']) #Habria que poner despues de /token_id?password=K78700616
def token_id():
    S = "K78700616"
    contrasenia = request.args["password"] 
    if (contrasenia == S):
        #json_b_group = n_d_averages_json()
        return "Go to: http://localhost:6060/upload"#json_b_group #open_json(path_json) #Devolver Json con la predicción
    else:
        return "CONTRASEÑA INCORRECTA"

"""
@app.route('/upload', methods=['GET', 'POST']) #Me permite introducir archivos json o csv (en web)
def upload():
    if request.method == 'POST':
        try:
            df = pd.read_csv(request.files.get('file'))
            df.to_csv('output.csv', index=False, header=None)
        except:
            df = pd.read_json(request.files.get('file'))
            df.to_json('output_json.csv', index=False, header=None)
        return render_template('upload.html', shape=cambios_input_datos(df)) 
    return render_template('upload.html')
"""

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=6060) 