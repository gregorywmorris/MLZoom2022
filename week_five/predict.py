"""## Load the model"""

print("start")

import pickle
from flask import Flask
from flask import request, jsonify

model_file = "model_C=1.0.bin" # file location

with open(model_file, "rb") as f_in: # rb = read bin
    dv, model = pickle.load(f_in) 
# dv is needed so you can transform input, otherwise the model will not be able to proccess the imput

app = Flask("churn")


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    
    # this code should be in it's own production in real life
    X = dv.transform([customer])  ## apply the one-hot encoding feature to the customer data 
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5
    
    # make sure return value tells the requester what they need to do with the information
    result = {
        'churn_probability' : float(y_pred),
        'churn' : bool(churn)
        }
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=8080)