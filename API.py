'''from TwitterAPI import TwitterAPI
consumer_key = "INKFuJbdhm4umODXmXOzh9sRh"
consumer_secret = "KES9DBLkBCnoe7QtRA8EdJNM6CODK2hMry4i44NxptItWhoHln"
access_token_key = "254573033-4eKzjAdSrjzLAdEL5aHCz0W0q30I1UI1uWIMlWc9"
access_token_secret = "g3RhcTjZJnRJbuF6n4O9gjyGUe6dtDs8iIQROCk4DwXp2"
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
r = api.request('search/tweets', {'q':'#พรรคอนาคตใหม่'},)
for item in r:
    print(item['text']if 'text' in item else item)'''

import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'INKFuJbdhm4umODXmXOzh9sRh'
consumer_secret = 'KES9DBLkBCnoe7QtRA8EdJNM6CODK2hMry4i44NxptItWhoHln'
access_token = '254573033-4eKzjAdSrjzLAdEL5aHCz0W0q30I1UI1uWIMlWc9'
access_token_secret = 'g3RhcTjZJnRJbuF6n4O9gjyGUe6dtDs8iIQROCk4DwXp2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
#csvFile = open('Datatweet.csv', 'a',encoding='utf-8')
#Use csv Writer
#svWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#พรรคอนาคตใหม่",tweet_mode='extended',count=300,
                           lang="th",
                           since="2019-01-01").items():
    print (tweet.created_at, tweet.full_text)
    #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])