from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('car_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        year = int(request.form['Year'])
        present_price = float(request.form['Present_Price'])
        kms_driven = int(request.form['Kms_Driven'])
        fuel_type = int(request.form['Fuel_Type'])
        seller_type = int(request.form['Seller_Type'])
        transmission = int(request.form['Transmission'])
        owner = int(request.form['Owner'])

        # Process input data
        input_data = np.array([[year, present_price, kms_driven, fuel_type, seller_type, transmission, owner]])
        prediction = model.predict(input_data)[0]

        return render_template('index.html', prediction=f"Estimated Car Price: {prediction:.2f} Lakhs")

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
