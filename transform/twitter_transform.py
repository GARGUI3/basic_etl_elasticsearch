'''
Module transform data
'''
import random
import string

def generate_id(size=24):
    """Generate a random string ID"""
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(size))

def transform_tweets(tweets):
    """Tranform data to send ElasticSearch"""
    data = []
    rule_id = generate_id()
    print("Rule_id: " + rule_id)
    print("Inserted tweets: " + str(len(tweets)))
    for tweet in tweets:
        tweet['engagement_count'] = (tweet['likes_count'] + tweet['retweets_count'])
        tweet['rule_id'] = rule_id
        new_tweet = {
            'tweet': tweet,
            'metadata': {
                '_index': 'tweet_data',
                '_type': 'tweet'
            }
        }
        data.append(new_tweet)

    return data
