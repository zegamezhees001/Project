import random
import  pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from pythainlp.tokenize import word_tokenize as wt



filepath = (r"C:\Users\User\Desktop\ProjectPycharm\CollectData\CleanDataPhueathai.csv")
df = pd.read_csv(filepath)

listdf = list(df)

sample_word = random.sample(listdf,200)

x = pd.read_csv(r"C:\Users\User\Desktop\ProjectPycharm\MergeTextNewFile2.csv")
X_train = x['X']
Y_train = x['Y']

pipeLine = Pipeline([('vect', CountVectorizer(analyzer=lambda df: wt(sample_word))),
                     ('tfidf', TfidfTransformer()),])
vec_ter_x = pipeLine.fit_transform(X_train)

smoteData = SMOTE(random_state=42)
xtrain , x_test , ytrain , y_test = train_test_split(vec_ter_x , Y_train ,test_size= 0.1 , random_state=2)
train_x_val , train_y_val =smoteData.fit_sample(xtrain,ytrain)
nb = MultinomialNB()
nb.fit(train_x_val , train_y_val)
a = nb.predict(pipeLine.transform(sample_word))
gg = np.array(a)
listDATA = gg.tolist()
# print(listDATA)
pos = 0
neg = 0
neu = 0

# for i in listDATA:
#     if i == 'pos':
#         pos +=1
#     elif i == 'neu':
#         neu +=1
#     else:
#         neg +=1
print('Pos :',pos)
print('Neg :',neg)
print('Neu:',neu)


ypred = nb.predict(x_test)
print(classification_report(ypred, y_test))
accuracy = accuracy_score(ypred, y_test)
print("Accuracy score = %.2f" % accuracy)