from flask import Flask, render_template, request
import numpy as np
#import weather as W
import pickle
app = Flask(__name__)
model = pickle.load(open('Logistic_Reg_DCC.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/", methods = ['POST'])
def weather():
    if request.method == "POST":
        prec =float(request.form['precp'])
        maxT = float(request.form['maxT'])
        minT =  float(request.form['minT'])
        wind = float(request.form['wind'])

        L = [[prec,maxT, minT, wind]]
        print(L)
        w_pred = model.predict(L)
        print(w_pred[0])
    
    return render_template("./index.html", n = w_pred[0])


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
