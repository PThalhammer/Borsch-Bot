#!/usr/bin/python3

import tweepy
import time
import datetime
import random


#from borschkeys import *
from testkeys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

today =  datetime.date.today()
partytime =  datetime.date(2019,12,25) 

days = partytime-today
#print(days.days)


user = api.me()
#print(user.id)

tw_nu = random.randint(1,6)

if   (tw_nu == 1):
    tweet = "Wow! Nur noch " + str(days.days) + " Tage bis zum Borsch Fest!!!"
elif (tw_nu == 2):
    tweet = "Hey, In " + str(days.days) + " Tagen ist Borsch Fest!"
elif (tw_nu == 3):
    tweet = "Schon gehört?! In " + str(days.days) + " Tagen ist Borsch Fest!!!"
elif (tw_nu == 4):
    tweet = "Borsch Fest ist in "+str(days.days) + " Tagen!"
elif (tw_nu == 5):
    tweet = "Man mag es kaum glauben, aber Борщ-фестиваль ist in " + str(days.days) + " Tagen!!"
else:
    tweet = str(days.days) + "  дня до фестиваля Борща!!!"

try:
   api.update_status(tweet)
except tweepy.error.TweepError:
    print("Duplicate!")
    pass
 