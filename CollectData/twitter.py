
import tweepy
from pythainlp.tokenize import word_tokenize as wt
import re
import pandas as pd

consumerKey = "INKFuJbdhm4umODXmXOzh9sRh"
consumerSecret = "KES9DBLkBCnoe7QtRA8EdJNM6CODK2hMry4i44NxptItWhoHln"
accessToken = "254573033-4eKzjAdSrjzLAdEL5aHCz0W0q30I1UI1uWIMlWc9"
accessTokenSecret = "g3RhcTjZJnRJbuF6n4O9gjyGUe6dtDs8iIQROCk4DwXp2"

auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


searchTerm = input("Enter Keyword : ")
# noOfSearchTerms = int(input("Enter How many tweets  to analyze: "))
noOfSearchTerms = 10
tweets = tweepy.Cursor(api.search, q=searchTerm, lang="th",tweet_mode="extended").items(noOfSearchTerms)

# count = 0
data=[]
for tweet in tweets:
    data.append(tweet.full_text)
print(data)
print(len(data))
# df = pd.DataFrame({'Text' :data})
# df.to_csv("Rattaban.csv")

def merge_text(text_array):
    temp = ""
    for data in text_array:
        temp += data + ' '
    return temp

# Cut word with re and word_tokenize
def handle_wt(txt):
    regx = r'https://t.co/\w+|RT\s@\w*\d*:|\n|\s|#|_|\u200b|[=]+\s[ก-๙]+\s[=]+|\n'  # regrx for handle url to split it.
    txt_ = merge_text(re.split(regx, txt))
    txt__ = merge_text(re.findall(r'[a-zA-Zก-๙]+', txt_, re.MULTILINE))
    text_raw = wt(txt__, engine='newmm')
    datas = list(filter(lambda x: x, text_raw))
    return datas


# Clean text
def clean_text(text):
    text = handle_wt(text)  # cut text to array
    texts = ' '.join(word.strip() for word in text if len(word) > 2)  # delete stopwors from text
    return texts

data_clean = [clean_text(txt) for txt in data]
print(data_clean)