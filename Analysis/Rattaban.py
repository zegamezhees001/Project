import re
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from pythainlp.tokenize import word_tokenize as wt
import matplotlib.pyplot as plt
import firebase_admin
from firebase_admin import credentials, db

filepath = (r"C:\Users\User\Desktop\ProjectPycharm\CollectData\CleanDataPracharat.csv")
df = pd.read_csv(filepath)


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
print('Pos :',pos)
print('Neg :',neg)
print('Neu:',neu)


ypred = nb.predict(x_test)

accuracy = accuracy_score(ypred, y_test)
print("%.2f" % accuracy)


# firebase add data
cred = credentials.Certificate(r"C:\Users\User\Desktop\ProjectPycharm\sentimentanalysis-d39db-firebase-adminsdk-m0vr4-414c7cc0dd.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://sentimentanalysis-d39db.firebaseio.com/'

})
ref = db.reference('Sentiment')
ref_child = ref.child('พลังประชารัฐ')
ref_child.update({
    'pos':pos,
    'neg':neg,
    'neu':neu
})
