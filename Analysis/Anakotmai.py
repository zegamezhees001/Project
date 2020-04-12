import itertools
import re
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix ,  log_loss
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from pythainlp.tokenize import word_tokenize as wt
import  matplotlib.pyplot as plt
import firebase_admin
from firebase_admin import credentials, db

filepath = (r"C:\Users\User\Desktop\ProjectPycharm\CollectData\CleanDataAnakotmai.csv")
df = pd.read_csv(filepath)



# x = pd.read_csv('MergeText.csv')
x = pd.read_csv(r"C:\Users\User\Desktop\ProjectPycharm\MergeTextNewFile1.csv")
X_train = x['X']
Y_train = x['Y']

pipeLine = Pipeline([('vect', CountVectorizer(analyzer=lambda df: wt(df))),
                     ('tfidf', TfidfTransformer()),])
vec_ter_x = pipeLine.fit_transform(X_train)



smoteData = SMOTE(random_state=42)
xtrain , x_test , ytrain , y_test = train_test_split(vec_ter_x , Y_train ,test_size= 0.1 , random_state=2)
train_x_val , train_y_val =smoteData.fit_sample(xtrain,ytrain)
nb = MultinomialNB()
nb.fit(train_x_val , train_y_val)



a = nb.predict(pipeLine.transform(df['text']))
gg = np.array(a)
listDATA = gg.tolist()
# print(listDATA)
pos = 0
neg = 0
neu = 0

for i in listDATA:
    if i == 'pos':
        pos +=1
    elif i == 'neu':
        neu +=1
    else:
        neg +=1



ypred = nb.predict(x_test)
print(classification_report(y_test, ypred))
accuracy = accuracy_score(y_test, ypred)

print("Accuracy score = %.2f" % accuracy)
error_rate = 1-accuracy
print("Error rate = %.2f" % error_rate)

confusion_mat = confusion_matrix(y_test,ypred)
print(confusion_mat)

def plot_confusion_matrix(cm,target_names,title='Confusion matrix',cmap=None,normalize=True):
    accuracy = np.trace(cm)/float(np.sum(cm))
    misclass = 1 - accuracy
    if cmap is None:
        cmap = plt.get_cmap('OrRd')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()


    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float')/cm.sum(axis=1)[:, np.newaxis]
    thresh = cm.max()/1.5 if normalize else cm.max()/2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.show()
plot_confusion_matrix(cm=confusion_mat,
                      normalize=False,
                      target_names=['Negative','Neutral','Positive'],
                      title="Confusion Matrix"
                      )






