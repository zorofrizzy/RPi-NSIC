import speech_recognition as sr
import PocketSphinx
#getting input from mic


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)



#Recognition using Sphinx

try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Audio not understood")
except sr.RequestError as e:
    print("Sphinx Error; {0}".format(e))





























