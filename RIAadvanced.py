# open code
# sendEmail
# play music
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib


print("Initializing Ria...")

MASTER = "master"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def speak(text):
        engine.say(text)
        engine.runAndWait()

def wishMe():

        hour = int(datetime.datetime.now().hour)
        
        if hour>=0 and hour<12:
                speak("Good morning" + MASTER)
        elif hour >=12 and hour<18:
                speak("Good afternoon" + MASTER)
        else:
                speak("Good evening" + MASTER)


        # speak("I am Riya...how may I help you.")
 
def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
        try:
                print("Recognizing...")
                query = r.recognize_google(audio, language = 'en-in')
                print(f"user said: {query}\n")
        except Exception as e: 
                print("Sorry, could you please say that again.")
                query = None
                
        return query
speak("Initializing Riya...")
wishMe()
query = takeCommand()
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("", '')
    server.sendmail("ImRageelixerdupe@gmail.com", to, content)
    server.close()

if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace('wikipedia', "")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(results)
elif 'youtube' in query.lower():
        url = 'www.youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
        webbrowser.get(chrome_path).open_new(url)
elif 'rubik\'s cube' in query.lower():
        url = 'www.youtube.com/c/Jperm'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
        webbrowser.get(chrome_path).open_new(url)
elif 'yahoo' in query.lower():
        url = 'mail.yahoo.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open_new(url)

#elif 'play music' or 'music' in query.lower():
        # songs_dir = ""
        # songs = os.listdir(song_dir)
        # os.startfile(os.path.join(songs_dir, songs[0])) 


elif 'open code' in query.lower():
        codePath = "C:\\Users\\Vikram\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath) 
elif 'email' in query.lower():
        try:
                speak("What should I send.")
                content = takeCommand()
                to = "srividya_nagarajan@yahoo.com" 
                sendEmail(to, content)
                speak("Email has been sent successfully!")
        except Exception as e:
                print(e) 

elif 'open gmail' in query.lower():
        url = 'https://mail.google.com/mail/u/0/#inbox'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open_new(url)
elif 'open reddit' in query.lower():
        url = 'reddit.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open_new(url)
elif 'open stack overflow' or 'stackoverflow' in query.lower():
        url = 'stackoverflow.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open_new(url)
elif 'nothing' or 'go to sleep' or 'stop' in query.lower():
        speak("Ok, sorry to disturb")



        

