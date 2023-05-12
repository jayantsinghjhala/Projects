from flask import Flask,render_template,request,url_for
import jsonify
import requests
import pickle
import numpy as np
import sklearn


from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('file.pkl','rb'))

@app.route('/',methods=['GET'])
def Home(): 
  return render_template('index.html')  

standard_to = StandardScaler()

@app.route('/predict',methods = ['POST'])
def predict():
    Fuel_Type_Diesel =0
    if request.method == 'POST':
        year = int(request.form['year'])
        new_price = float(request.form['new_price'])
        kmdriven = int(request.form['kmdriven'])
        fueltype = request.form['fuel']
        transmissiontype = request.form['transmissiontype']
        enginecc=int(request.form['enginecc'])
        mileage=float(request.form['mileage'])
        if(fueltype == 'Petrol'):
            fuel = 0
        if(fueltype == 'Diesel'):
            fuel = 1
        else:
            fuel = 2

        if(transmissiontype == 'Manual'):
            transmissiontype = 0
        else:
            transmissiontype = 1

        prediction = model.predict([[new_price,year,fuel,transmissiontype,mileage,enginecc,kmdriven]])
        output = round(prediction[0],2)
        
        if output<0:
            return render_template('index.html',prediction_text='Sorry! You cannot sell this car')
        else:
            return render_template('index.html', prediction_text='You can sell this car at Rs.{} lakhs'.format(output))
        
    else:
        return render_template('index.html')
    
    
    
if __name__ == '__main__':
    app.run(debug=True)