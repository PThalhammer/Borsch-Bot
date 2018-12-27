#!/usr/bin/python3

import tweepy
import time
import datetime
import time

followers = []

consumer_key = 'QQo8N56cfZYN1qT0pEDWKfhDR'
consumer_secret = 'edsr1pvh8ghuNDvavYBlat4mI0OOXLVE1y7iUMFX3r7Fl8Ewpd'
access_token = '1066107262006104065-7tH86y2z0cvbp6WOUExzKj18fUzhaf'
access_token_secret = 'qPKefmkz0uYR8mzHyfHJNVpfKpnWdVpBZSwyqic9y2XCa'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.me()
#bla= tweepy.Cursor(api.followers, screen_name="username")
print(api.followers_ids(id=user.id))

followers = api.followers_ids(id=user.id)
#get_last_tweet(api);
print (user.name)

	

while(False):
	time.sleep(60)
	print("Checking...")
	followers_now = api.followers_ids(id=user.id)
	print(followers)
	print("*********")
	print(followers_now)
	if (followers_now == followers): continue 
	for id in followers_now:
		if id not in followers:
			print("Sending message...")
			api.send_direct_message(user_id = id, text = "Привет!")
	followers=followers_nows
	time.sleep(60)
			