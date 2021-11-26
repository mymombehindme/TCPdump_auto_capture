import pandas as pd
from xgboost import XGBClassifier
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
import pickle
import matplotlib.pyplot as plt
import seaborn as sns 
import time
import numpy as np
import sys
try:
    b = sys.stdin.readline()

    data = pd.read_csv(b)
    # data = data.fillna(0)
    # data[np.isinf(data)]=0
    X = data.iloc[:,0:77]
    print(X)
except:
    exit()
# Y = data['Label']


# split data into train and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, Y,test_size=0.5,train_size=0.5)
model=XGBClassifier()
model.load_model('malicious.bin')
start_time = time.time()
y_pred = model.predict(X)
# predictions = [round(value) for value in y_pred]
end_time = time.time()
print(y_pred)
# print("predict: %d" % predictions[0])
# print("true value: %d" % y_test.values[0])
print("--- %s seconds ---" % (end_time - start_time))
# evaluate predictions
# accuracy = accuracy_score(y_test, predictions)
# precision = precision_score(y_test, predictions)
# recall = recall_score(y_test, predictions)
