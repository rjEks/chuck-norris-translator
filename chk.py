import requests
import boto3


def return_joke():
    
    chk_endpoint_response = requests.get("https://api.chucknorris.io/jokes/random")
    chk_endpoint_response_json = chk_endpoint_response.json()
    
    return chk_endpoint_response_json["value"]