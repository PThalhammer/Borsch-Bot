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

user = api.me()
#print(user.id)
proverbs = []
with open("../etc/proverbs.txt") as f:
    proverbs = f.readlines()

proverbs = [x.strip() for x in proverbs] 

n  = random.randint(1,250)

tweet = "Пословица дня: \n"+proverbs[n]

try:
   api.update_status(tweet)
except tweepy.error.TweepError:
    print("Duplicate!")
    pass
 
