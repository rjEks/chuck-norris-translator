import boto3 
import os
import translate
import chk


translate_client = boto3.client('translate')

def handler(event, context):
    
    chk_text = chk.return_joke()
    chk_joke = translate.translate(chk_text,translate_client,"en","pt")
    


