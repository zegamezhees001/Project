import firebase_admin

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from pythainlp.tokenize import word_tokenize as wt
from pythainlp.corpus import thai_stopwords

from functionCleanText import clean_text
from firebase_admin import credentials, db


text = ["การศึกษาคือกระบวนการที่สนับสนุนการเรียนรู้ หรือการได้มาซึ่งความรู้ ทักษะ คุณค่า ความเชื่อ และนิสัย วิธีการศึกษามีทั้ง การเล่าเรื่อง การทำกลุ่มอภิปราย การสอน การอบรม และการวิจัยทางตรง การศึกษามักถูกเข้าใจว่าเป็นการชี้แนะของผู้ให้การศึกษา แล้วผู้เรียนก็ต้องศึกษาด้วยตัวของเขาด้วย การศึกษาสามารถจัดแบบเป็นทางการและไม่เป็นทางการ ที่จะทำให้เกิดประสบการณ์ เกิดผลอย่างเป็นรูปธรรมต่อการคิด การรู้สึก หรือพฤติกรรม ก็ถือเป็นการศึกษาได้",
            "เศรษฐกิจ คือ งานอันเกี่ยวกับการผลิต การจำหน่ายจ่ายแจก และการบริโภคใช้สอยสิ่งต่าง ๆ ของชุมชน"]



file = (r"C:\Users\User\Desktop\ProjectPycharm\Classify\texttext.csv")
tt = pd.read_csv(file)
word_clean = [clean_text(txt) for txt in tt['text']]
print(word_clean)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(word_clean)

filepath = (r"C:\Users\User\Desktop\ProjectPycharm\CollectData\CleanDataAnakotmai.csv")
df = pd.read_csv(filepath)

# test clustering
# vectorizer = Pipeline([('vect',CountVectorizer(analyzer=lambda tt:wt(tt))),
#                      ('tfidf',TfidfTransformer()),])
# X =vectorizer.fit_transform(tt['text'])


# cv = CountVectorizer(analyzer=lambda tt:wt(tt))
# X = cv.fit_transform(clean_text1)
# print(X)
pipeLine = Pipeline([('vect',CountVectorizer(analyzer=lambda df:wt(df))),
                     ('tfidf',TfidfTransformer()),])

true_k = 3
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()


print("\n")
print("Prediction")
X = vectorizer.transform(df['text'])
predicted = model.predict(X)
print(predicted)
# a1 = 0
# b1 = 0
# c1 = 0
# for i in predicted:
#     if i == 0:
#         a1 += 1
#     elif i == 1:
#         b1 += 1
#     else:
#         c1 += 1
# print(a1,b1,c1)
#
# X = cv.transform(df['text'])
# predicted = model.predict(X)
# print(predicted)


# firebase add data


#  upto firebase
# cred = credentials.Certificate(r"C:\Users\User\Desktop\ProjectPycharm\sentimentanalysis-d39db-firebase-adminsdk-m0vr4-414c7cc0dd.json")
# firebase_admin.initialize_app(cred,{
#     'databaseURL' : 'https://sentimentanalysis-d39db.firebaseio.com/'
#
# })
# ref = db.reference('Sentiment')
# ref.update({
#     'เพื่อไทย/clustering': {
#         'การศึกษา':'21',
#     },
# })