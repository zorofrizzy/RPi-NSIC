import os

with open('zorotext.txt', 'r') as file:
    k = file.read().replace('\n', '')

     
os.system('echo "{0}" | festival --tts'.format(k)) 

