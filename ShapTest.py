#https://towardsdatascience.com/lime-vs-shap-which-is-better-for-explaining-machine-learning-models-d68d8290bb16

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

#wine = pd.read_csv('winequality-red.csv')
diabetes = pd.read_csv('diabetes.csv')

#data_URL = "https://raw.githubusercontent.com/txt2vz/pythonAI/main/diabetes.csv"
#diabetes = pd.read_csv(data_URL)


print(diabetes.head())
#print(wine.head)

from sklearn.model_selection import train_test_split

#X = wine.drop('quality', axis=1)
#y = wine['quality']
# Separate Features and Target Variables
X = diabetes.drop(columns='Outcome')
y = diabetes['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"xtraing shapte {X_train.shape}  ytrain shape {y_train.shape}")

from xgboost import XGBClassifier
seed = 42
#np.random.seed(seed)
rf = RandomForestClassifier()

rf.fit(X_train, y_train)


from xgboost import XGBClassifier

model = XGBClassifier()
model.fit(X_train, y_train)

test_1 = X_test.iloc[1]
print(f"test_1 {test_1}")

import lime 
from lime import lime_tabular

lime_explainer = lime_tabular.LimeTabularExplainer(
    training_data=np.array(X_train),
    feature_names=X_train.columns,
    class_names=['bad', 'good'],
    mode='classification'
)


lime_exp = lime_explainer.explain_instance(
    data_row=test_1,
    predict_fn=model.predict_proba
)
lime_exp.show_in_notebook(show_table=True)