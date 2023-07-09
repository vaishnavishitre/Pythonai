from winreg import QueryInfoKey
import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import requests
import json
import webbrowser
import os
import pywhatkit as kit
import smtplib

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[0].id)
print(voices[0].id)
author = 'Vaishnavi'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak(F"GOOD MORINING {author}")
    elif hour >= 12 and hour < 16:
        speak(f"GOOD AFTERNOON{author}")
    else: 
        speak(f"good Eveing{author}")

    speak(f"Hello {author} I am jarvis, How can i help you?")

def takeCommand():
    """
    take microphone input from user and return string
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :{query} \n ") 
    except Exception as e:
        print(f"Sorry {author}, Say that again...")
        return "none"
    return query

if __name__ == '__main__':
   wishMe()
   if 1:
       query = takeCommand().lower()
       if 'wikipedia' and 'who' in query:
           speak("Searching wikipedia...")
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query, sentences=3)
           speak("According yo wikipedia..")
           print(results)
           speak(results)
       elif 'news' in query:
           speak("news headline")
           query= query.replace("news","")
           url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=5be0e10d6f0e4fa297ecb73dba39087d"
           news = requests.get(url).text
           news = json.loads(news)
           art = news['articles']
           for article in art:
               print(article['title'])
               speak(article['title'])

               print(article['description'])
               speak(article['description'])
               speak(" Moving on to next news")
       elif  'open google' in query:
        webbrowser.open("google.com")
       
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")

       elif 'search browser' in query:
           speak("what should i search?")
           um = takeCommand().lower()
           webbrowser.open(f"{um}")
       
       elif 'ip address' in query:
           
           ip = requests.get('http:/api.ipify.org').text
           print(f"Your ip is {ip}")
           speak(f"Your ip is {ip}")
      
       elif 'open command prompt' in query :
           os.system("start cmd")
       
       elif 'open vs code' in query:
           codepath =  "C:\\Microsoft VS Code\\Code.exe"
           os.startfile(codepath)

       # elif 'any command' in query:
        #   codepath =  "path of the file or app that needs to be started "
         #  os.startfile(codepath)

       elif 'play music' in query:
           music_dir = "C:\\Users\\Vaishnavi\\Dropbox\\PC\\Desktop\\internship\\music"
           songs = os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir, songs[0]))  

       elif 'play youtube' in query: 
           speak("what should i search in youtube")
           cm = takeCommand().lower()
           kit.playonyt(f"{cm}")
       
       elif 'send message' in query:
           speak("Who do u want to send the message?")
           num = input("enter number:\n")
           speak("What do u want to send?")
           msg = takeCommand().lower()
           H = int(input("enter hour?\n"))
           M = int(input("enter minutes"))
           kit.sendwhatmsg(num, msg,H,M)

    
 #"""   elif 'send mail' in query:
           """ speak("What should i send?")
           content = takeCommand().lower()
           speak("whom to send mail? , enter email address")
           to = input("Enter email address:\n")
           sendEmail(to,content) 
           
           for that allow email for less secure 
           in google settings """    

