import csv
import pandas as pd
import xgboost as xgb
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from xgboost import plot_importance
import matplotlib.pyplot  as plt
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import confusion_matrix
import os
import numpy as np
import time
import sys
def plot_confusion_matrix(cm, savename, title='Confusion Matrix'):

    plt.figure(figsize=(12, 8), dpi=100)
    np.set_printoptions(precision=2)

    # 在混淆矩阵中每格的概率值
    ind_array = np.arange(len(classes))
    x, y = np.meshgrid(ind_array, ind_array)
    for x_val, y_val in zip(x.flatten(), y.flatten()):
        c = cm[y_val][x_val]
        if c > 0.001:
            plt.text(x_val, y_val, "%0.2f" % (c,), color='red', fontsize=15, va='center', ha='center')

    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.binary)
    plt.title(title)
    plt.colorbar()
    xlocations = np.array(range(len(classes)))
    plt.xticks(xlocations, classes, rotation=90)
    plt.yticks(xlocations, classes)
    plt.ylabel('Actual label')
    plt.xlabel('Predict label')

    # offset the tick
    tick_marks = np.array(range(len(classes))) + 0.5
    plt.gca().set_xticks(tick_marks, minor=True)
    plt.gca().set_yticks(tick_marks, minor=True)
    plt.gca().xaxis.set_ticks_position('none')
    plt.gca().yaxis.set_ticks_position('none')
    plt.grid(True, which='minor', linestyle='-')
    plt.gcf().subplots_adjust(bottom=0.15)

    # show confusion matrix
    plt.savefig(savename, format='png')
    plt.show()
start = time.time()
#os.environ["PATH"] += os.pathsep + 'D:/graphviz/bin'

data = pd.read_csv(sys.argv[1])
data2 = pd.read_csv(sys.argv[2])



#X = pd.DataFrame(data[:])
#y = pd.Series(data2[:])

classes =[1,2,3,4,5,6,7,8,9,10,11,12]

X_train, X_test, y_train, y_test = train_test_split(data, data2,test_size=0.5,train_size=0.5)
# knn = KNeighborsClassifier(n_neighbors=10)

dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)
 #p_test = xgb.DMatrix(create_data_dum,label=y_test)
watchlist = [(dtrain, 'train'), (dtest, 'test')]
xgb_pars = { 'eta': 0.03,
        'max_depth': 10,  'booster' : 'gbtree',  'eval_metric': 'mlogloss', 'objective': 'multi:softmax','num_class': 13}
model = xgb.train(xgb_pars, dtrain, 1 ,watchlist, early_stopping_rounds=2, maximize=False, verbose_eval=1)
ans = model.predict(dtest)
model.save_model('test_model')

print(X_test)
X_test.to_csv('D:\dataset\\xgb_classfity\\x_test.csv')

print(ans)

print(ans.shape)
print(y_test)
cm = confusion_matrix(y_test,ans)
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

print("Accuracy : %.4g" % metrics.accuracy_score(y_test, ans))
print("precision: %.4g" % metrics.precision_score(y_test,ans,average='macro'))
print("recall: %.4g" % metrics.recall_score(y_test,ans,average='macro'))

#fig = plt.figure(figsize=(10, 10))
#ax = fig.subplots()
#xgb.plot_tree(model, num_trees=1, ax=ax)
# plt.show()

end = time.time()
plot_confusion_matrix(cm_normalized, 'confusion_matrix.png', title='confusion matrix')
print("執行時間: %f秒" % (end-start))