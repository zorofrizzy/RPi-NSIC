import speech_recognition as sr
import pyaudio
from subprocess import call

r=sr.Recognizer()
with sr.Microphone(device_index=2, sample_rate = 44100, chunk_size=512) as source:
    print("Say Something!")
    audio = r.listen(source)
try:
    print("Google thinks you said: " + r.recognize_google(audio, language = 'en-us', show_all=False))
    call(["speake3", r.recognize_google(audio, language = 'en-us', show_all=False)])
except sr.unknownValueError:
    print("Couldn't understand!")
except sr.RequestError as e:
    print("Couldn't contact server")
