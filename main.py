""" Main Function """
from extract import twitter_extract
from transform import twitter_transform
from load import twitter_load
from dotenv import load_dotenv
from pathlib import Path  # python3 only

env_path = Path('.') / 'environment_variables.env'
load_dotenv(dotenv_path=env_path)

# Get tweets, first paramets username, second parameter tweets number to extract max 100
TWEETS = twitter_extract.get_tweets("Cristiano", 50)
DATA = twitter_transform.transform_tweets(TWEETS)
RES = twitter_load.load_tweets(DATA)

print(RES)
