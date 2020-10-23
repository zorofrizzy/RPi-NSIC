#speech to text using SPEECH_RECOGNITION

import speech_recognition as sr

# taking input from microphone

read = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)

    print(audio)


#https://www.youtube.com/watch?v=K_WbsFrPUCk
