import requests
# pprint is used to format the JSON response
from pprint import pprint
import os

subscription_key = "ca8704057cda444fb6210114b3f8fdbc"
#os.environ)["LANGSUBKEY"]
#"ca8704057cda444fb6210114b3f8fdbc"
endpoint = "https://testls01.cognitiveservices.azure.com/"
#os.environ)["LANDENDPOINT"]
#"https://testls01.cognitiveservices.azure.com/"

language_api_url = endpoint + "/text/analytics/v3.0/languages"


def detect_language_fn(text):
    documents = {"documents": [
        {"id": "1", "text": text}
    ]}

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(language_api_url, headers=headers, json=documents)
    languages = response.json()


    return languages
