from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import cred

url=cred.url
key=cred.key

connection = ComputerVisionClient(url,CognitiveServicesCredentials(key))

img = "https://raw.githubusercontent.com/gottagetgit/AI102Files/main/Computer_Vision/Analyze_images_using_Computer_Vision_API/Images/Landmark.jpg"

res = connection.describe_image(img)

for des in res.captions:
    print(des.text,"----------",des.confidence*100)
