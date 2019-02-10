#!/usr/bin/python3

import tweepy
import time
import datetime
import random



from borschkeys import *
#from testkeys import *


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

msg="Random Borsch Bild: "

num=random.randint(1,90)

img="/home/pi/Borsch-Bot/Borsch_Pics/"+str(num)+".jpg"

#try:
api.update_with_media(img, msg)
#except tweepy.error.TweepError:
#    print("Duplicate!")
#    pass
 
