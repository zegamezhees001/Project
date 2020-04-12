# # import firebase_admin
# # from firebase_admin import credentials, db
# #
# #
# # # ./sentimentanalysis-d39db-firebase-adminsdk-m0vr4-414c7cc0dd.json
# #
# # # Initialize the app with a service account, granting admin privileges
# # # def initFireBase():
# # #     fileName = 'sentimentanalysis-d39db-firebase-adminsdk-m0vr4-414c7cc0dd.json'
# # #     dataBaseRef = 'https://sentimentanalysis-d39db.firebaseio.com/'
# # #     cred = credentials.Certificate(fileName)
# # #     firebase_admin.initialize_app(
# # #         cred, {"databaseURL": dataBaseRef})
# # #
# # # def funcCallBack(dataEvent):
# # #         if dataEvent.data != '':
# # #             keys = list(dataEvent.data.keys())
# # #             # do something....
# # #
# # # def realTimeDb():
# # #         root = db.reference("comments")
# # #         root.listen(callback=funcCallBack)
# #
# # cred = credentials.Certificate("sentimentanalysis-d39db-firebase-adminsdk-m0vr4-414c7cc0dd.json")
# # firebase_admin.initialize_app(cred,{
# #     'databaseURL' : 'https://sentimentanalysis-d39db.firebaseio.com/'
# #
# # })
# #
# # ref = db.reference('/')
# # ref.set({
# #     'box':
# #         {
# #             'box01':{
# #                 'color':'red',
# #                 'width': 1,
# #                 'height': 3,
# #             }
# #         }
# # })
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.cluster import KMeans
#
# documents = ["the young french men crowned world champions",
#              "Google Translate app is getting more intelligent everyday",
#              "Facebook face recognition is driving me crazy",
#              "who is going to win the Golden Ball title this year",
#              "these camera apps are funny",
#              "Croacian team made a brilliant world cup campaign reaching the final match",
#              "Google Chrome extensions are useful.",
#              "Social Media apps leveraging AI incredibly",
#              "Qatar 2022 FIFA world cup is played in winter"]
#
# vectorizer = TfidfVectorizer(stop_words='english')
# data = vectorizer.fit_transform(documents)
#
# true_k = 3
# clustering_model = KMeans(n_clusters=true_k,
#                           init='k-means++',
#                           max_iter=300, n_init=10)
# clustering_model.fit(data)
#
# print("Top terms per cluster:")
#
# sorted_centroids = clustering_model.cluster_centers_.argsort()[:, ::-1]
# terms = vectorizer.get_feature_names()
#
# for i in range(true_k):
#     print("Cluster %d:"%i, end='')
#     for ind in sorted_centroids[i, :10]:
#         print(' %s'%terms[ind], end='')
#     print()
#     print()
#
# print()
# print("Predictions of new documents")
#
# new_doc = ["how to install Chrome"]
# Y = vectorizer.transform(new_doc)
# prediction = clustering_model.predict(Y)
# print(prediction)
#
# new_doc = ["UCL Final match is played in Madrid this year"]
# Y = vectorizer.transform(new_doc)
# prediction = clustering_model.predict(Y)
# print(prediction)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

documents = ["This little kitty came to play when I was eating at a restaurant.",
             "Merley has the best squooshy kitten belly.",
             "Google Translate app is incredible.",
             "If you open 100 tab in google you get a smiley face.",
             "Best cat photo I've ever taken.",
             "Climbing ninja cat.",
             "Impressed with google map feedback.",
             "Key promoter extension for Google Chrome."]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:"%i),
    for ind in order_centroids[i, :10]:
        print(' %s'%terms[ind]),
    print

print("\n")
print("Prediction")

Y = vectorizer.transform(["chrome browser to open."])
prediction = model.predict(Y)
print(prediction)

Y = vectorizer.transform(["My cat is hungry."])
prediction = model.predict(Y)
print(prediction)
