
# Multi model traing done in notebook.

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from imblearn.over_sampling import SMOTE

df = pd.read_csv('healthcare-dataset-stroke-data.csv') # .csv must be in same directory

df_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

df_train = df_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)


y_train = df_train.stroke.values
y_test = df_test.stroke.values

del df_train['stroke']
del df_test['stroke']

# x_train
train_dict = df_train.to_dict(orient='records')

dv = DictVectorizer(sparse=False)
x_train = dv.fit_transform(train_dict)

# x_test
test_dict = df_test.to_dict(orient='records')
x_test = dv.transform(test_dict)

# ONLY APPLY SMOTE TO TRAIN!
def training_smote(x,y):
    smt = SMOTE(random_state=1)
    x_train, y_train = smt.fit_resample(x, y)
    return x_train, y_train

# SMOTE
x_train, y_train = training_smote(x_train, y_train)
len(x_train), len(y_train)

# Train model
log_model = LogisticRegression(max_iter=1000, random_state=1,C=100,penalty='l2',solver='lbfgs')

log_model.fit(x_train, y_train)
