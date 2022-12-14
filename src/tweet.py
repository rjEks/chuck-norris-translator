import json
import requests
import tweepy  as tw 
import os
import re

def set_credentials(secrets):

    bearer_token=secrets['BEARER_TOKEN']
    access_token = secrets['ACCESS_TOKEN']
    access_token_secret = secrets['ACCESS_TOKEN_SECRET']
    api_key = secrets['API_KEY']
    api_key_secret = secrets['API_KEY_SECRET']
    
    return bearer_token,api_key,api_key_secret,access_token,access_token_secret

def get_client(bearer_token,api_key,api_key_secret,access_token,
            access_token_secret):    

    client = tw.Client(bearer_token=bearer_token, 
                       consumer_key=api_key, 
                       consumer_secret=api_key_secret, 
                       access_token=access_token, 
                       access_token_secret=access_token_secret )
    return client
    
def post_tweet(client, text):
    
    client.create_tweet(text=text)