#!/usr/bin/python3

import tweepy
import time
import datetime
import time
import random

###########
# Apparently Tweepy is still broken and you cant sent DMs :/
###########


followers = []

#from borschkeys import *
from testkeys import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
#bla= tweepy.Cursor(api.followers, screen_name="username")
#print(api.followers_ids(id=user.id))

followers = api.followers_ids(id=user.id)
#get_last_tweet(api);
print (user.name)

id = 868495528291598337

api.send_direct_message(user_id=id, text="Hello")
	


while(False):
	time.sleep(30)
	followers_now = api.followers_ids(id=user.id)
	if (followers_now == followers): continue 
	for id in followers_now:
		if id not in followers:
			print(id)
			try:
				api.send_direct_message(user_id = id, text = "Hello")
			except tweepy.error.TweepError:
			        pass
	followers=followers_now
	print( str(random.randint(1,100)) )
				
