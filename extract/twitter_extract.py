'''
Module extract data
'''
import os
import tweepy

def get_tweets(username, count):
    '''
    Get tweets by username
    '''
    consumer_key = os.environ.get("consumerKey")
    consumer_secret = os.environ.get("consumerSecret")
    access_token_key = os.environ.get("accessTokenKey")
    access_token_secret = os.environ.get("accessTokenSecret")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name=username, count=count)
    data = []
    for tweet in tweets:
        new_tweet = {
            "retweets_count": tweet.retweet_count,
            "likes_count": tweet.favorite_count,
            "body": tweet.text,
            "type": "original",
            "posted_time": tweet.created_at
        }
        data.append(new_tweet)

    return data
