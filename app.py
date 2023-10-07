from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open("Model.pkl","rb"))
app = Flask(__name__)

@app.route('/')
def trial():
    return render_template("index.html")

@app.route('/predict',methods = ['POST'])
def Predict_insurance():
    AGE = int(request.form.get("AGE"))
    EMPLOYEMENT_TYPE = int(request.form.get("EMPLOYEMENT TYPE"))
    GRADUATE_OR_NOTGRADUATE = int(request.form.get("GRADUATE OR NOTGRADUATE"))
    ANNUAL_INCOME = int(request.form.get("ANNUAL INCOME"))
    FAMILY_MEMBERS = int(request.form.get("FAMILY MEMBERS"))
    FREQUENT_FLYER = int(request.form.get("FREQUENT FLYER"))
    EVER_TRAVELLED_ABROAD = int(request.form.get("EVER TRAVELLED ABROAD"))

    result = model.predict(np.array([AGE,EMPLOYEMENT_TYPE,GRADUATE_OR_NOTGRADUATE,ANNUAL_INCOME,FAMILY_MEMBERS,FREQUENT_FLYER,EVER_TRAVELLED_ABROAD]).reshape(1,7))
    if result[0] == 1:
        result = 'INSURANCE TAKEN'
    else:
        result = 'INSURANCE NOT TAKEN'

    return render_template('index.html',result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 8080 )