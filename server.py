from flask import Flask, request, render_template,flash,redirect,session,abort
from models import Model
from writeCsv import write_to_csv
from datetime import datetime
import os
import pandas as pd

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'user1' and request.form['username'] == 'user1':
        session['logged_in'] = True
        return render_template('index.html')
    elif request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return displayrecords()
    else :
        return render_template('loginerror.html')

@app.route('/displayrecords',methods=['GET'])
def displayrecords():
    df = pd.read_csv('dataset/records.csv')
    return render_template('displayrecords.html', tables=[df.to_html(classes='data', header="true")])


@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return root()


@app.route('/predict', methods=["POST"])
def predict():
    age = int(request.form['age'])
    bp = int(request.form['bp'])
    sugar = int(request.form['sugar'])
    pc = int(request.form['pc'])
    pcc = int(request.form['pcc'])
    sodium = int(request.form['sodium'])
    hemo = float(request.form['hemo'])
    htn = int(request.form['htn'])
    db = int(request.form['db'])

    values = [age, bp, sugar, pc, pcc, sodium, hemo, htn,db]
    print(values)
    model = Model()
    classifier = model.randomforest_classifier()
    prediction = classifier.predict([values])
    print(f"Kidney disease = {prediction[0]}")

    time = datetime.now().strftime("%m/%d/%Y (%H:%M:%S)")
    write_to_csv(time,age, bp, sugar, pc, pcc, sodium, hemo, htn,db,prediction[0])
    return render_template("result.html", result=prediction[0])

app.secret_key = os.urandom(12)
app.run(port=5000, host='0.0.0.0', debug=True)