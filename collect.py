import pandas as pd
from datetime import datetime

import tweepy
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as dates

mpl.use('TkAgg')

def load_keys():
    keysfile = open('keys.json', 'r')
    keys = json.load(keysfile)['twitter']
    # json loaded data as unicode, convert as str in case
    consumer_key = str(keys['consumer_key'])
    consumer_secret = str(keys['consumer_secret'])
    access_key = str(keys['access_token'])
    access_secret = str(keys['access_secret'])
    return consumer_key, consumer_secret, access_key, access_secret

def initialize_twitter_api():
    consumer_key, consumer_secret, access_key, access_secret = load_keys()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api

def get_tweets_from_archive():
    f = file.open('trump_dump.json')
    return json.load(f, strict=False)

def get_tweets_from_pickle():
    unpickled_df = pd.read_pickle("trump_dump.pkl")
    return unpickled_df

def clean_dates(times):
    times = [' '.join(t.splitlines()) for t in times]
    times = [datetime.strptime(t, '%a %b %d %H:%M:%S %z %Y') for t in times]
    return times

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analyse_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

def get_all_tweets(screenname):
    api = initialize_twitter_api()
    tweets = api.user_timeline(screen_name = screenname,count=200)
    return tweets

def get_tweet_times(tweets):
    tweet_times = [ tweet.created_at for tweet in tweets]
    return tweet_times

def plot_activity(tweet_times):
    ax = plt.subplot(111)
    ax.bar(tweet_times,height=0.1, width=0.01)
    plt.show()

def populate_dataframe(tweets)
    data = pd.DataFrame(data=np.array([' '.join(tweet['text'].splitlines()) for tweet in tweets]), columns=['tweets'])
    data['date'] = np.array(clean_dates(get_tweet_times(tweets)))
    data['len']  = np.array([len(data['tweets']) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])


if __name__ == '__main__':
    tweets = get_all_tweets('realDonaldTrump')
    tweet_times = get_tweet_times(tweets)

    import ipdb
    ipdb.set_trace()

    plot_activity(tweet_times)
