import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
import os
from picamera import PiCamera
from time import sleep
api_instance = cloudmersive_ocr_api_client.ImageOcrApi()



camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('sneak.jpg')
camera.stop_preview()



image_file = 'sneak.jpg' # file | Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = '9c08f189-d653-4997-ab19-8aa1fdf2f581'

try:
    # Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.
    api_response = api_instance.image_ocr_post(image_file)
    s = api_response.text_result
    print(s)
  
    # Playing the converted file 
    os.system('echo "{0}" | festival --tts'.format(s))
except ApiException as e:
    print("Exception when calling ImageOcrApi->image_ocr_post: %s" % e)
