"""## Load the model"""

print('start')

import pickle

input_file = 'model_C=1.0.bin' # file location

with open(input_file, 'rb') as f_in: # rb = read bin
    dv, model = pickle.load(f_in) 
# dv is needed so you can transform input, otherwise the model will not be able to proccess the imput

model

customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}
# new customer to test model

X = dv.transform([customer])

y_pred = model.predict_proba(X)[0, 1]

print(" ")
print('input:', customer)
print(" ")
print('output:', y_pred)