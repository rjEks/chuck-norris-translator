import boto3 
import os
import translate


translate_client = boto3.client('translate')

def handler(event, context):
    
    translate.translate()



