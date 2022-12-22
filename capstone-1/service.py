
import bentoml
from bentoml.io import JSON
import numpy as np

model_ref = bentoml.sklearn.get('loan_approval:latest')
dv = model_ref.custom_objects['dicVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service('loan_approval', runners=[model_runner])

@svc.api(input= JSON.from_sample({
        "sub_grade":  "G1",
        "emp_length": "10+ years",
        "home_ownership": "MORTGAGE",
        "annual_inc":  120000.0,
        "verification_status":  "Verified",
        "loan_status":  1,
        "purpose":  "house",
        "dti":  24.0,
        "delinq_2yrs":  0.0,
        "inq_last_6mths": 0.0,
        "mths_since_last_delinq": 59.,
        "open_acc": 14.0,
        "pub_rec":  0.0,
        "revol_bal":  18199.0,
        "revol_util": 71.4,
        "total_acc":  35.0,
        "recoveries": 0.0,
        "pub_rec_bankruptcies": 0.0,
        "income_level": "100-150000k"
        }), 
        output= JSON())
def classify(application_data):
    vector = dv.transform(application_data)
    prediction = model_runner.predict_proba.run(vector)
    # np.format_float_positional returns a string
    round_predict = float(np.format_float_positional(prediction[:,1], precision=2))

    if round_predict < 0.50:
        return 'Decline: Credit Risk High'
    elif (round_predict > 80):
        return 'Approved: Credit Risk Low'
    else:
        return 'Approved: Credit Risk Moderate'
