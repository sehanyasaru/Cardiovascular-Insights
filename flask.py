from flask import Flask, request, jsonify
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
app = Flask(__name__)

with open("C:\Users\User\Desktop\ML Assignement( Group 15)\Svc_Model.pkl", 'rb') as model_file:
    Svc = pickle.load(model_file)

def Std_Scalar(data):
    scaler = StandardScaler()
    return scaler.fit_transform(data)

def process(user_data):
    cd = {
        "ag": 0,
        "wg": 0,
        "ac": 0,
        "wc": 0
    }

    user_data["Gender"] = 1 if user_data["Gender"].lower() == "male" else 0
    user_data["Smoking"] = 1 if user_data["Smoking"].lower() in ["yes", "y", "1"] else 0
    user_data["Alcohol Consumption"] = 1 if user_data["Alcohol Consumption"].lower() in ["yes", "y", "1"] else 0
    user_data["Physical Activity"] = 1 if user_data["Physical Activity"].lower() in ["regular", "yes", "y", "1"] else 0

    cholesterol = float(user_data["Cholesterol"])
    glucose = float(user_data["Glucose"])
    bmi = float(user_data["Weight"]) / ((float(user_data["Height"]) / 100) ** 2)

    test_val = np.array([int(user_data["Age"]), bmi, float(user_data["Systolic Blood Pressure"]), float(user_data["Diastolic Blood Pressure"])])
    test_val = test_val.reshape(1, -1)
    
    mod = Std_Scalar(test_val)
    mod = mod.reshape(1, -1)

    if cholesterol < 200:
        user_data["Cholesterol"] = 1
    elif 200 <= cholesterol <= 239:
        cd["ag"] = 1
    else:
        cd["wg"] = 1

    if glucose < 100:
        user_data["Glucose"] = 1
    elif 100 <= glucose <= 125:
        cd["ac"] = 1
    else:
        cd["wc"] = 1

    post1 = np.array([user_data["Gender"], cd["ag"], cd["wg"], cd["ac"]])
    post2 = np.array([cd["wc"], user_data["Smoking"], user_data["Alcohol Consumption"], user_data["Physical Activity"]])
    
    post1 = post1.reshape(1, -1)
    post2 = post2.reshape(1, -1)
    
    prol = np.concatenate((mod, post1.astype(int), post2.astype(int)), axis=1)
    return prol

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        required_fields = ["Age", "Gender", "Height", "Weight", 
                           "Systolic Blood Pressure", "Diastolic Blood Pressure",
                           "Cholesterol", "Glucose", 
                           "Smoking", "Alcohol Consumption", 
                           "Physical Activity"]
        
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        processed_data = process(data)
        
        prediction = Svc.predict(processed_data)
        
        return jsonify({"prediction": prediction[0]})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
