import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
import pickle
# from preprocess import *
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np


# data = encode_raw('dataset.csv', 'feature_table.bin')
data = pd.read_csv('dataset.csv')
data = data.fillna(0)
data[np.isinf(data)]=0
X = data[['f'+str(i) for i in range(1,77)]]
Y = data['f77']

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=7)
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)

# fit model no training datafr
model = XGBClassifier()
eval_set = [(X_test, y_test)]
model.fit(X_train, y_train, eval_metric="error", eval_set=eval_set, verbose=False)
# make predictions for test data
y_pred = model.predict(X_test.values)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)

print("Accuracy: %.2f%%" % (accuracy * 100.0))

print("Precision: %.2f%%" % (precision * 100.0))

print("Recall: %.2f%%" % (recall * 100.0))

#count precision
cm=confusion_matrix(y_test,y_pred)
TNR=cm[0][0]+cm[0][1]
TNR=float(cm[0][0])/float(TNR)
TPR=cm[1][0]+cm[1][1]
TPR=float(cm[1][1])/float(TPR)
print("TPR: %.2f%%" % (TPR * 100.0))
print("TNR: %.2f%%" % (TNR * 100.0))

model.save_model("malicious.bin")
sns.heatmap(cm,square= True, annot=True, cbar= False)
plt.xlabel("predicted value")
plt.ylabel("true value")
plt.show()

# data = pd.read_csv('dataset_atk.csv')
# data = encode_by_table(data, 'feature_table')

# X = data[['f'+str(i) for i in range(1,48)]]
# Y = data['f49']

# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=7)

# model = XGBClassifier()
# model.load_model('malicious.bin')

# y_pred = model.predict(X)
# print(y_pred)
# predictions = [round(value) for value in y_pred]
# for i in range(len(predictions)):
#     print(X[i], end="\t, ")
#     print("prediction: %d" % predictions[i])