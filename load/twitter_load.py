"""
Module load twitter data
"""
from utils import elastic

def load_tweets(tweets):
    """
    Insert tweets on ElasticSearch
    """
    try:
        elastic.insert(tweets)
    except:
        return "Unsuccessful load data"
    return "Successful load data"
