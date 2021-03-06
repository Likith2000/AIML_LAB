import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
dataset = pd.read_csv("8-dataset.csv", names=names)
X = dataset.iloc[:, :-1]
Y = dataset.iloc[:, -1]
print(X.head())
Xtrain, Xtest, ytrain, ytest = train_test_split(X, Y, test_size=0.10)
classifier = KNeighborsClassifier(n_neighbors=5).fit(Xtrain, ytrain)
ypred = classifier.predict(Xtest)

i = 0
print("\n------------------------------------------------------------------")
print('%-25s %-25s %-25s' %
      ('Original Label', 'Predicted Label', 'Correct/Wrong'))
print("------------------------------------------------------------------")
for label in ytest:
    if (label == ypred[i]):
        print('%-25s %-25s %-25s' % (label, ypred[i], 'Correct'))
    else:
        print('%-25s %-25s %-25s' % (label, ypred[i], 'Wrong'))
    i = i + 1

# print("\nConfusion Matrix:\n", metrics.confusion_matrix(ytest, ypred))
# print("\nClassification Report:\n", metrics.classification_report(ytest, ypred))
print('\nAccuracy of the classifier is %0.2f' %
      metrics.accuracy_score(ytest, ypred))
