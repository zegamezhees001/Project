import re
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from pythainlp.tokenize import word_tokenize as wt

filepath = (r"C:\Users\User\Desktop\ProjectPycharm\CollectData\CleanDataRattaban.csv")
df = pd.read_csv(filepath)



x = pd.read_csv('MergeText.csv')
X_train = x['X']
Y_train = x['Y']

pipeLine = Pipeline([('vect', CountVectorizer(analyzer=lambda df: wt(df))),
                     ('tfidf', TfidfTransformer()),])
vec_ter_x = pipeLine.fit_transform(X_train)

smoteData = SMOTE(random_state=42)
train_x, train_y = smoteData.fit_sample(vec_ter_x, Y_train)
nb = MultinomialNB()
nb.fit(train_x, train_y)


a = nb.predict(pipeLine.transform(df['text']))
gg = np.array(a)
listDATA = gg.tolist()
# print(listDATA)
pos = 0
neg = 0

for i in listDATA:
    if i == 'pos':
        pos +=1
    else:
        neg +=1
print(pos)
print(neg)