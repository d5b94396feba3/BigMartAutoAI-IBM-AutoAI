
# Load libraries
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

import time


# load dataset
data=pd.read_csv('src/RF/dataset.csv')
data.head()
# print(data.shape,'\n')


values = ['Gender', 'Age', 'Depression', 'Sleep_disturbance', 'Unexplained_weight', 'Heat_intolerance', 'Fatigue', 'Hoarse_voice', 'Constipation', 'Tremor',
                          'Heart_palpitation', 'Sweating', 'Forgetfulness', 'Hair_disorders', 'Muscle_disorders', 'Irregular_heartbeat', 'Gland_enlarged', 'Vision_irritations', 'Appetite', 'Skin_thinning']

for column in values:
    data[column] = data[column].replace(-1, np.NaN)
    mean = int(data[column].mean(skipna=True))
    data[column] = data[column].replace(np.NaN, mean)


X = data.drop('level', axis=1)
y = data['level']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1)  # 70% training and 30% test


clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

clf = clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
random_forest = RandomForestClassifier(n_estimators=20)
random_forest.fit(X_train, y_train)

y_pred = random_forest.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
