import pandas as pd
import firebase_admin
from firebase_admin import credentials, db
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from pythainlp.tokenize import word_tokenize as wt
from pythainlp.corpus import thai_stopwords

from functionCleanText import clean_text



filetrain = (r"C:\Users\User\Desktop\ProjectPycharm\Classify\AnakotmaiTrain.csv")
word = pd.read_csv(filetrain)
word_clean = [clean_text(txt) for txt in word['text']]


fileclustering = (r"C:\Users\User\Desktop\ProjectPycharm\Classify\Dataaftersentiment\SetthakitmaiNeatral.csv")
wordcluster = pd.read_csv(fileclustering)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(word_clean)


true_k = 7
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()

print("\n")
print("Prediction")
X = vectorizer.transform(wordcluster['text'])
predicted = model.predict(X)
print(predicted)

a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0


for i in predicted:
    if i == 0:
        a1 += 1
    elif i == 1:
        a2 += 1
    elif i == 2:
        a3 += 1
    elif i == 3:
        a4 += 1
    elif i == 4:
        a5 += 1
    elif i == 5:
        a6 +=1
    else:
        a7 += 1

print("นโยบายด้านประชาธิปไตยและสิทธิมนุษยชน : ", a1, "\n",
      "นโยบายด้านการต่างประเทศ", a2, "\n",
      "นโยบายด้านการศึกษา", a3, "\n",
      "นโยบายด้านการสร้างความเสมอภาคทางสังคม", a4, "\n",
      "นโยบายด้านการเกษตร", a5, "\n",
      "นโยบายด้านเศรษฐกิจ", a6, "\n",
      "นโยบายด้านสวัสดิการและแรงงาน", a7, "\n")

# firebase add data


#  upto firebase
cred = credentials.Certificate(r"C:\Users\User\Desktop\ProjectPycharm\sentimentanalysis-d39db-firebase-adminsdk-m0vr4-414c7cc0dd.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://sentimentanalysis-d39db.firebaseio.com/'

})
ref = db.reference('Sentiment')
ref.update({
    'เศรษฐกิจใหม่/cluster/Neutral': {
        'นโยบายด้านประชาธิปไตยและสิทธิมนุษยชน': a1,
        'นโยบายด้านการต่างประเทศ': a2,
        'นโยบายด้านการศึกษา': a3,
        'นโยบายด้านการสร้างความเสมอภาคทางสังคม': a4,
        'นโยบายด้านการเกษตร': a5,
        'นโยบายด้านเศรษฐกิจ': a6,
        'นโยบายด้านสวัสดิการและแรงงาน': a7,
    },
})






