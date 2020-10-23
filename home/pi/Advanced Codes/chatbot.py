#CHATBOT : AT A CERTAIN INPUT GIVE A SPECIFIC OUTPUT


aD={ "HI" : "HELLO",
     "WASSUP" : "NOTHING MUCH DO YOU WANT TO KN OW THE WEATHER?",
     "YES" : "WELL UT'S ABOUT TO RAIN",
     "TELL ME A JOKE" : "WELL, YOU ARE ONE",
     "BYE" : "PRESS '1' TO EXIT"}



while True:
    userInput=input()
    if userInput=='1':
        break;
    elif userInput!='1':
         if userInput=="HI":
            k=aD.get("HI")
            
         elif userInput=='WASSUP':
              k=aD.get("WASSUP")

         elif userInput=="YES":
              k=aD.get("YES")

         elif userInput=="TELL ME A JOKE":
              k=aD.get("TELL ME A JOKE")

         else:
              k=aD.get("BYE")
    else:
        k="THE INPUT DOESN'T EXIST"
    print(k)

print("NED OF CODE")     
              
              
            
        
