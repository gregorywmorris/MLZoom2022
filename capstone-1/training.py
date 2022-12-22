
import bentoml
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from catboost import CatBoostClassifier
import numpy as np
import pandas as pd

# model Selection
model = XGBClassifier(random_state=10)

# Preprocessing
df_train = pd.read_csv('lc_clean.csv')

df_full_train, df_test_small = train_test_split(df, test_size=0.1, random_state=1)

# df_test_small see lc_test.csv
df_full_train = df_full_train.reset_index(drop=True)

y_full_train = df_full_train.loan_status.values

del df_full_train['loan_status']

train_full_dict = df_full_train.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
x_full_train = dv.fit_transform(train_full_dict)

# train model
model.fit(x_full_train, y_full_train)


# save model with bentoml
bentoml.sklearn.save_model('loan_approval', final_model, 
                           custom_objects={
                               'dicVectorizer': dv
                           },
                           signatures = {"predict_proba": {"batchable": False}}
                           )
