import requests
# pprint is used to format the JSON response
from pprint import pprint

subscription_key = "YourKey"
endpoint = "YourEndpoint"

sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"
keyphrase_url = endpoint + "/text/analytics/v3.0/keyphrases"

def sentiment_analysis_key_phrases(lang,text):

    documents = {"documents": [
        {"id": "1", "language": lang,
        "text": text},
    ]} 

    # Identify Sentiment
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(sentiment_url, headers=headers, json=documents)
    sentiments = response.json()
    
    # Extract Key Phrases
    response = requests.post(keyphrase_url, headers=headers, json=documents)
    key_phrases = response.json()
    

    return sentiments,key_phrases
