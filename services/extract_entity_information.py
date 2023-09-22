from pip._vendor import requests
# pprint is used to format the JSON response
from pprint import pprint

# variables to store subscription key and root URL for the Cognitive Service resource
subscription_key = ""
endpoint = ""

# append the Text Analytics endpoint information to the URL
entities_url = endpoint + "/text/analytics/v2.1/entities"

def entity_information(lang,text):

# variable to store a JSON formatted document that contains two entries in a JSON array.
    documents = {"documents": [
        {"id": "1", "language": lang,
        "text": text},
    ]}

    # Setup the header information for the REST request passing in the subscription key
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}

    # Build the REST request by passing in the complete URL, header information for authentication, and the JSON document
    response = requests.post(entities_url, headers=headers, json=documents)

    # Create a variable to store the results that are returned from the REST request
    entities = response.json()

    # Output the result using pprint.
    return entities
