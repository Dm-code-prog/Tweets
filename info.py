import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')


import tweepy
import numpy as np


def getTweet():
    client = tweepy.Client(bearer_token=TOKEN)
    query = "bitcoin"
    tweets = client.search_recent_tweets(query, max_results=10)

    texts = np.array([i['text'] for i in tweets.data])
    return texts