from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time


subscription_key = "<enter your key here>"
endpoint = "<enter your endpoint URL here>"


def caption_images(image):

    description_results = ''

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


    '''
    Describe an Image - remote
    This example describes the contents of an image with the confidence score.
    '''
    print("===== Describe an image - remote =====")
    # Call API
    description_results = computervision_client.describe_image(image)

    
    '''
    Describe an Image - local
    This example describes the contents of an image with the confidence score.
    '''
    print("===== Describe an Image - local =====")
    # Open local image file
    # local_image_path = "Images/Landmark.jpg"
    # local_image = open(local_image_path, "rb")

    # Call API
    # description_result = computervision_client.describe_image_in_stream(local_image)

    # # Get the captions (descriptions) from the response, with confidence level
    # print("Description of local image: ")
    # if len(description_result.captions) == 0:
    #     print("No description detected.")
    # else:
    #     for caption in description_result.captions:
    #         print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))

    return description_results
    '''
    END - Describe an Image - local
    '''
