import numpy as np
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
msg = pd.read_csv('lab6.txt', names=['message', 'label'])

print('The dimensions of the dataset', msg.shape)
msg['labelnum'] = msg.label.map({'pos': 1, 'neg': 0})
X = msg.message
y = msg.labelnum
print(X)
print(y)
xtrain, xtest, ytrain, ytest = train_test_split(X, y)
print(xtest.shape)
print(xtrain.shape)
print(ytest.shape)
print(ytrain.shape)
count_vect = CountVectorizer()
xtrain_dtm = count_vect.fit_transform(xtrain)
xtest_dtm = count_vect.transform(xtest)
print("Uniqu Labels")
print(count_vect.get_feature_names())
df = pd.DataFrame(xtrain_dtm.toarray(), columns=count_vect.get_feature_names())
print(df)
clf = MultinomialNB().fit(xtrain_dtm, ytrain)
predicted = clf.predict(xtest_dtm)
print("ytest")
print(ytest)
print("predicted")
print(predicted)
print('Accuracy metrics')
print('Accuracy of the classifer is', metrics.accuracy_score(ytest, predicted))
print('Confusion matrix')
labels = np.unique(ytest)  # Assign concept labels
a = metrics.confusion_matrix(ytest, predicted, labels=labels)
cm = pd.DataFrame(a, index=labels, columns=labels)
print(cm)
print('Recall and Precison ')
print('Recall', metrics.recall_score(ytest, predicted))
print('Precison', metrics.precision_score(ytest, predicted))
