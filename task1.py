import pyttsx3 #pip install pyttsx3==2.6
import datetime
import time
from win10toast import ToastNotifier#pip install win10toast
toaster = ToastNotifier()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def nowtime():
    strTime = datetime.datetime.now().strftime("%H") 
    return strTime
nowtime=nowtime()
#print(nowtime)


query = {
  "Morning walk and exercise":5,
  "brush":6 ,
  "Take bath":7,
  "have your breakfast ":8,
  "join your online class":10,
  "have fruits":11,
  "have your lunch":13,
  "take rest":14,
  "go out to play and relax yourself":16,
  "have your evening snacks":18,
  "its time to study":19,
  "have your dinner with your family":21,
  "prepare yourself for next day classes":22,
  "go to bed for sleep":23

}

#print(tuple(query.items())[i]][0])

while True:
    for i in range(0,len(query)):
        task=tuple(query.items())[i][0]
        y=int(query.get(task))
        #print(task)
        #print(y)

        
        if y==int(nowtime):
            speak("it is,"+str(nowtime)+",now"+str(task))
            toaster.show_toast(str(task),"It is "+str(nowtime),duration=10) 

    time.sleep(3600)
            

