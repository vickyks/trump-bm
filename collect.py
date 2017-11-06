import tweepy
import json

import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np

import csv

keysfile = open('keys.json', 'r')
keys = json.load(keysfile)['twitter']

# json loaded data as unicode
consumer_key = str(keys['consumer_key'])
consumer_secret = str(keys['consumer_secret'])
access_key = str(keys['access_token'])
access_secret = str(keys['access_secret'])


def initialize_twitter_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api


def get_all_tweets(screenname):
    api = initialize_twitter_api()
    tweets = api.user_timeline(screen_name = screenname,count=200)
    return tweets


def get_tweet_times(tweets):
    tweet_times = [ tweet.created_at for tweet in tweets]
    return tweet_times


def plot_activity(tweet_time):
    ax = plt.subplot(111)
    ax.bar(tweet_times,y,width=0.01)
    plt.show()


if __name__ == '__main__':
    tweets = get_all_tweets('realDonaldTrump')
    tweet_times = get_tweet_times(tweets)
    plot_activity(tweet_times)
