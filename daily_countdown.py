#!/usr/bin/python3

import tweepy
import time
import datetime
import random


consumer_key = 'QQo8N56cfZYN1qT0pEDWKfhDR'
consumer_secret = 'edsr1pvh8ghuNDvavYBlat4mI0OOXLVE1y7iUMFX3r7Fl8Ewpd'
access_token = '1066107262006104065-7tH86y2z0cvbp6WOUExzKj18fUzhaf'
access_token_secret = 'qPKefmkz0uYR8mzHyfHJNVpfKpnWdVpBZSwyqic9y2XCa'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

today =  datetime.date.today()
partytime =  datetime.date(2018,12, 25) 

days = partytime-today
#print(days.days)


user = api.me()
#print(user.id)

tw_nu = random.randint(1,6)

if   (tw_nu == 1):
    tweet = "Wow! Nur noch " + str(days.days) + " Tage bis zum Borschtsch Fest!!!"
elif (tw_nu == 2):
    tweet = "Hey, In " + str(days.days) + " Tagen ist Borschtsch Fest!"
elif (tw_nu == 3):
    tweet = "Schon gehört?! In " + str(days.days) + " Tagen ist Borschtsch Fest!!!"
elif (tw_nu == 4):
    tweet = "Borschtsch Fest ist in "+str(days.days) + " Tagen!"
elif (tw_nu == 5):
    tweet = "Man mag es kaum glauben, aber Борщ-фестиваль ist in " + str(days.days) + " Tagen!!"
else:
    tweet = str(days.days) + "  дня до фестиваля Борща!!!"

try:
   api.update_status(tweet)
except tweepy.error.TweepError:
    print("Duplicate!")
    pass
 