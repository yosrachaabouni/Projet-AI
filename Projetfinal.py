from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import openai
import APIKey



computervision_client = ComputerVisionClient(APIKey.endpoint, CognitiveServicesCredentials(APIKey.subscription_key))



print("===== Describe an Image - local =====")
# ouvrir l'image qu'on a téléchargé en local 
local_image_path = "image.png"
local_image = open(local_image_path, "rb")

# appel de l'api
description_result = computervision_client.describe_image_in_stream(local_image)

# Get the captions (descriptions) from the response, with confidence level
print("Description of local image: ")
if len(description_result.captions) == 0:
    print("No description detected.")
else:
    for caption in description_result.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))

'''
END - Describe an Image - local
'''

openai.api_key = 'sk-proj-C6joKkEq0v0OFGZJyb2aT3BlbkFJr1yyhwMpXH7RCAPKzc0b'
response = openai.Image.create(

    prompt=f"The description of the image is: '{description_result.captions[0].text}'." if description_result.captions else "No description detected.",
    n=1,
    size="1024x1024"
)   

image_url = response['data'][0]['url']

print(image_url)

# générer une nouvelle image avec une modification demandé 

scene_prompt = "Please generate a scene where the woman is the hospital"

response = openai.Image.create(

    prompt=f"The description of the image is: '{description_result.captions[0].text}'. Please generate a scene where the woman is the hospital .",
    n=1,
    size="1024x1024"
)   

image_url = response['data'][0]['url']

print(image_url)



#modifier une image avec edit ( partie BONUS ) : on importe une image local (image.png) 
#Avec un editeur d'image on lui précise l'emplacement du modification ( mask.png)


openai.api_key = 'sk-proj-C6joKkEq0v0OFGZJyb2aT3BlbkFJr1yyhwMpXH7RCAPKzc0b'
response = openai.Image.create_edit(
  image=open("image.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="add a smile emoji",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(response['data'])



