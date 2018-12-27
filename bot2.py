#!/usr/bin/python3

import tweepy
import time
import datetime


consumer_key = 'QQo8N56cfZYN1qT0pEDWKfhDR'
consumer_secret = 'edsr1pvh8ghuNDvavYBlat4mI0OOXLVE1y7iUMFX3r7Fl8Ewpd'
access_token = '1066107262006104065-7tH86y2z0cvbp6WOUExzKj18fUzhaf'
access_token_secret = 'qPKefmkz0uYR8mzHyfHJNVpfKpnWdVpBZSwyqic9y2XCa'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

today =  datetime.date.today()
partytime =  datetime.date(2018,12, 24) 

days = partytime-today
print(days.days)


user = api.me()
print(user.id)


tweet = "Wow! Only " + str(days.days) + " days until Borschtsch Fest!!!"

# api.update_status(tweet)
#def get_last_tweet(api):
#    tweet = api.user_timeline(id = user.id, count = 1)[0]
#    print(tweet.text)

#get_last_tweet(api);
print (user.name)