import boto3


def translate(text, client, source_language, target_language):
    
    translate_response = client.translate_text(
        Text=text,
        SourceLanguageCode=source_language,
        TargetLanguageCode=target_language
    )
    
    return translate_response