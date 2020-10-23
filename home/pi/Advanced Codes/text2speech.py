import speake3

zor = speake3.Speake()
voices = zor.get('voices')
#for voice in voices:
    #print (voice)
zor.set('voice','en-sc')
zor.set('speed','100')
zor.set('pitch', '90')
zor.set('wordgap','10')
zor.say("how are u")
zor.talkback()
