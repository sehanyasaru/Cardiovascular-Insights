# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# ------------------------------------------------------
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND
# THIS IS A DUMMY FLASK BACKEND FOR TESTING THE FRONTEND


from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

def calculate_bmi(height, weight):
    # Convert height to meters
    height_m = height / 100
    return weight / (height_m * height_m)

def predict_cardiovascular_disease(features):
    # Simple rule-based prediction for demonstration
    # In a real application, you would load and use your trained ML model here
    
    age = float(features['age'])
    bmi = calculate_bmi(float(features['height']), float(features['weight']))
    systolic = float(features['ap_hi'])
    diastolic = float(features['ap_lo'])
    cholesterol = int(features['cholesterol'])
    glucose = int(features['glucose'])
    
    # Simple risk factors count
    risk_factors = 0
    
    # Age risk
    if age > 50:
        risk_factors += 1
    
    # BMI risk
    if bmi > 25:
        risk_factors += 1
    
    # Blood pressure risk
    if systolic > 140 or diastolic > 90:
        risk_factors += 1
    
    # Cholesterol risk
    if cholesterol > 1:
        risk_factors += 1
    
    # Glucose risk
    if glucose > 1:
        risk_factors += 1
    
    # Lifestyle risks
    if features['smoking'] == '1':
        risk_factors += 1
    if features['alcohol'] == '1':
        risk_factors += 1
    if features['physical_activity'] == '0':
        risk_factors += 1
    
    # Predict high risk if 3 or more risk factors are present
    return 1 if risk_factors >= 3 else 0

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        prediction = predict_cardiovascular_disease(data)
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)