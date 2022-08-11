import boto3 
import os
import src.translate as translate
import src.chk as chk
from src.secrets_manager import get_secret
import src.tweet as tweet

translate_client = boto3.client('translate')
secrets = get_secret()

def handler(event, context):
    
    chk_text = chk.return_joke()
    chk_joke = translate.translate(chk_text,translate_client,"en","pt")

    bearer_token,api_key,api_key_secret,access_token,\
    access_token_secret = tweet.set_credentials(secrets)

    tweet_client = tweet.get_client(bearer_token,api_key,api_key_secret,access_token, \
                       access_token_secret)  

    tweet.post_tweet(tweet_client,chk_joke)