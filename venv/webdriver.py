'''from selenium import webdriver

driver = webdriver.Chrome("C:/Users/User/Desktop/chomedriver/chromedriver.exe")
url ="https://twitter.com/search?l=th&q=%23%E0%B8%9E%E0%B8%A3%E0%B8%A3%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B8%B2%E0%B8%84%E0%B8%95%E0%B9%83%E0%B8%AB%E0%B8%A1%E0%B9%88%20since%3A2019-01-01%20until%3A2019-03-24&src=typd&lang=th"
driver.get(url)'''

'''import  requests
url ="https://twitter.com/search?l=th&q=%23%E0%B8%9E%E0%B8%A3%E0%B8%A3%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B8%B2%E0%B8%84%E0%B8%95%E0%B9%83%E0%B8%AB%E0%B8%A1%E0%B9%88%20since%3A2019-01-01%20until%3A2019-03-24&src=typd&lang=th"

data = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(data.text,'html.parser')
x = soup.finda_all("h2",{"class":"post-titil"})

for i in x:
    print(i.text)'''

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'INKFuJbdhm4umODXmXOzh9sRh'
consumer_secret = 'KES9DBLkBCnoe7QtRA8EdJNM6CODK2hMry4i44NxptItWhoHln'
access_token = '254573033-4eKzjAdSrjzLAdEL5aHCz0W0q30I1UI1uWIMlWc9'
access_secret = 'g3RhcTjZJnRJbuF6n4O9gjyGUe6dtDs8iIQROCk4DwXp2'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a',encoding='utf-8') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s"%str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Avenger'])