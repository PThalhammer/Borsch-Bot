#!/usr/bin/python3

import tweepy
import time
import datetime
import time
import random


#from borschkeys import *
from testkeys import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


mentions = []

<<<<<<< HEAD
with open("../etc/mentions.txt") as my_file:
=======
with open("/home/pi/Borsch-Bot/etc/mentions.txt") as my_file:
>>>>>>> 82746c4bd65c7d6f92b7fa76a0cad77afd26d02e
            mentions = my_file.read().split(',')
#	    mentions = my_file.readlines()

print(mentions)
            
user = api.me()

new_mentions=api.mentions_timeline()

for tweet in new_mentions:
            if str(tweet.id) in mentions: continue
            print(tweet.id)
<<<<<<< HEAD
            msg = "@"+str(tweet.author.screen_name)+" Привет! Leider gibt's noch nichts neues zum Borsch Fest. Falls du's jedoch nicht abwarten kannst, hier ein  Rezept zum nachkochen: https://tinyurl.com/y8l3k346 "
=======
            msg = "@"+str(tweet.author.screen_name)+" Привет! Leider gibt's noch nichts neues zum Borsch Fest. Falls du's jedoch nicht abwarten kannst, hier ein Rezept zum nachkochen https://tinyurl.com/y8l3k346 "
>>>>>>> 82746c4bd65c7d6f92b7fa76a0cad77afd26d02e
            api.update_status(msg,in_reply_to_status_id=tweet.id)
            mentions.append(str(tweet.id))

print(mentions)
            
<<<<<<< HEAD
with open("../etc/mentions.txt", 'w') as f:
=======
with open("/home/pi/Borsch-Bot/etc/mentions.txt", 'w') as f:
>>>>>>> 82746c4bd65c7d6f92b7fa76a0cad77afd26d02e
    for item in mentions:
        f.write(str(item)+",")
	
