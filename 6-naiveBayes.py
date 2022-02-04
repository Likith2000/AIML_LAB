from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pandas as pd
data = pd.read_csv('6-naiveBayesData.csv')
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

model = GaussianNB()
model.fit(xtrain, ytrain)
predicted = model.predict(xtest)

print("Confusion : ", metrics.confusion_matrix(predicted, ytest))
print("Report : ", metrics.classification_report(predicted, ytest))
print("Accuracy : ", metrics.accuracy_score(predicted, ytest))
