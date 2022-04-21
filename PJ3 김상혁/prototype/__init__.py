from crypt import methods
import os
import numpy as np 
from flask import Flask, render_template, request 
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import KFold, GridSearchCV
from lightgbm import LGBMClassifier
import joblib

app = Flask(__name__)
model=joblib.load('prototype/knn_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    int_features=[int(x) for x  in request.form.values()]
    print(int_features)
    final_features=[np.array(int_features)]
    print(final_features)
    prediction=model.predict(final_features)
    
    if prediction == 1:
        output='걱정하지 않아도 됩니다.'
    else:
        output='위험합니다.'
    
    
    return render_template('index.html', prediction_text='당뇨진단 {}'.format(output))

# if __name__ == "__main__":
#     app.run(debug=True)