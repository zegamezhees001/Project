import tweepy
import pandas as pd

consumerKey = "INKFuJbdhm4umODXmXOzh9sRh"
consumerSecret = "KES9DBLkBCnoe7QtRA8EdJNM6CODK2hMry4i44NxptItWhoHln"
accessToken = "254573033-4eKzjAdSrjzLAdEL5aHCz0W0q30I1UI1uWIMlWc9"
accessTokenSecret = "g3RhcTjZJnRJbuF6n4O9gjyGUe6dtDs8iIQROCk4DwXp2"

auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
searchTerm = input("Enter Keyword : ")
noOfSearchTerms = int(input("Enter How many tweets  to analyze: "))
tweets = tweepy.Cursor(api.search, q=searchTerm, lang="th").items(noOfSearchTerms)

data1=[]
for tweet in tweets:
    data1.append(tweet.text)
    print(tweet.text)
print(len(data1))
df = pd.DataFrame({'Text' :data1})
df.to_csv("Prachathipat.csv")