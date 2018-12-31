#!/usr/bin/python3

import tweepy
import time
import datetime
import random
from math import * 

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

tw_nu = random.randint(1,8)

if   (tw_nu == 1):
    tweet = "Wow! Nur noch " + str(days.days) + " Tage bis zum Borsch Fest!!! \n #BF19"
elif (tw_nu == 2):
    tweet = "Hey, In " + str(days.days) + " Tagen ist Borsch Fest!"
elif (tw_nu == 3):
    tweet = "Schon gehört?! In " + str(days.days) + " Tagen ist wieder Borsch Fest!!!"
elif (tw_nu == 4):
    tweet = "Borsch Fest ist in "+str(days.days) + " Tagen! \n  #BF19"
elif (tw_nu == 5):
    tweet = "Man mag es kaum glauben, aber Борщ-фестиваль ist in " + str(days.days) + " Tagen!!"
elif (tw_nu == 6):
    tweet = "Schreibt's euch in den Kalender: Am 25.12.19 ist wieder Borsch Fest!"
elif (tw_nu == 7):
    tweet = "Weniger als "+str(ceil(days.days/7))+" Wochen!"
elif (tw_nu == 8):
    tweet = "Leute, nicht vergessen: Noch "+str(days.days)+" Tage zum großen Fest!  \n #BF19"
elif (tw_nu == 4):
    tweet = "For out international friends: Don't miss the Borsch-Party in "+str(days.days) + " days! \n  #BF19"
else:
    tweet = str(days.days) + "  дня до фестиваля Борща!!!  \n #BF19"


    
try:
   api.update_status(tweet)
except tweepy.error.TweepError:
    print("Duplicate!")
    pass
 
