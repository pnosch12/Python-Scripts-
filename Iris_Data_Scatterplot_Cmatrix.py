import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import numpy as np 
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
from sklearn.svm import LinearSVC
from sklearn.linear_model import Perceptron


#Reading File

df = pd.read_csv("iris.data", header = None)
df.head()
print(df)
print(df.describe())

#Plotting Data

plt.figure()
plt.subplot(2,1,1)
plt.xlabel("Sepal length (cm)")
plt.ylabel("Sepal width (cm)")
color = ["red", "orange", "blue"]
species = ["setosa", "veriscolor", "virginica"]
species_df = df[df.iloc[0:150,4] == "Iris-setosa"]
X1 = species_df.iloc[0:150, 0].values
X2 = species_df.iloc[0:150, 1].values
plt.scatter(X1, X2, color="red", label="setosa")

species_df = df[df.iloc[0:150,4] == "Iris-versicolor"]
X1 = species_df.iloc[0:150, 0].values
X2 = species_df.iloc[0:150, 1].values
plt.scatter(X1, X2, color="orange", label="versicolor")

species_df = df[df.iloc[0:150,4] == "Iris-virginica"]
X1 = species_df.iloc[0:150, 0].values
X2 = species_df.iloc[0:150, 1].values
plt.scatter(X1, X2, color="blue", label="virginica")
plt.legend(loc = 'lower right')

plt.subplot(2,1,2)
plt.xlabel("Petal length (cm)")
plt.ylabel("Petal width (cm)")
color = ["red", "orange", "blue"]
species = ["setosa", "veriscolor", "virginica"]
species_df = df[df.iloc[0:150,4] == "Iris-setosa"]
X1 = species_df.iloc[0:150, 2].values
X2 = species_df.iloc[0:150, 3].values
plt.scatter(X1, X2, color="red", label="setosa")

species_df = df[df.iloc[0:150,4] == "Iris-versicolor"]
X1 = species_df.iloc[0:150, 2].values
X2 = species_df.iloc[0:150, 3].values
plt.scatter(X1, X2, color="orange", label="versicolor")

species_df = df[df.iloc[0:150,4] == "Iris-virginica"]
X1 = species_df.iloc[0:150, 2].values
X2 = species_df.iloc[0:150, 3].values
plt.scatter(X1, X2, color="blue", label="virginica")
plt.legend(loc = 'lower right')

plt.show()


#SVM Matrix

X = df.drop([4], axis=1)
y = df[4]
  
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

svm = LinearSVC()
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


#Descision Tree Matrix


X = df.drop([4], axis=1)
y = df[4]


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


Descision_Tree = DecisionTreeClassifier()
Descision_Tree.fit(X_train, y_train)
y_pred = Descision_Tree.predict(X_test)


print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


#Perceptron


X = df.drop([4], axis=1)
y = df[4]


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


Perceptrons = Perceptron()
Perceptrons.fit(X_train, y_train)
y_pred = Perceptrons.predict(X_test)


print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))