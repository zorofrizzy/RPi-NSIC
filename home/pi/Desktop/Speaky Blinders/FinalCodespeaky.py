import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
from time import sleep

# Import the required module for text  
# to speech conversion
#camera module
from picamera import PiCamera
from gtts import gTTS

# This module is imported so that we can  
# play the converted audio 

import os

camera = PiCamera()


camera.resolution = (1024, 768)
camera.start_preview()

# Camera warm-up time
sleep(2)

camera.capture('new.jpg')
sleep(1)
camera.stop_preview()
camera.close()

language = 'en'

api_instance = cloudmersive_ocr_api_client.ImageOcrApi()
image_file = '/home/pi/Desktop/new.jpg' # file | Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = '9c08f189-d653-4997-ab19-8aa1fdf2f581'

try:
    # Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.
    api_response = api_instance.image_ocr_post(image_file)
    s = api_response.text_result
    print(s)
    print(api_response.mean_confidence_level)
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    #os.system('echo "{0}" | festival --tts'.format(s))
    myobj = gTTS(text=s, lang=language, slow=False)
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("convaudio.mp3") 
  
    # Playing the converted file
    os.system("omxplayer convaudio.mp3")      
    
except ApiException as e:
    print("Exception when calling ImageOcrApi->image_ocr_post: %s" % e)
