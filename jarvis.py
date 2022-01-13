import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from tkinter import *

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
'''for voice in voices:
    #print(voice, voice.id)'''
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    minute=int(datetime.datetime.now().minute)
    if hour >=0 and hour<=11 and minute<=59:
        speak("Good Morning!")
    elif hour>=12 and hour <=17 and minute<=59:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am friday, how may I help you?")
def takeCommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        #print("Recoginizing...")
        query=r.recognize_google(audio, language='en-in')
        #print(f"User said:{query}\n ")
    except Exception as e:
        #print(e)
        #print("Sorry sir, please repeat")
        return 'None'
    return query
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('www.rishu1122@gmail.com', 'Ashu@123AB')
    server.sendemail('www.rishu1122@gmail.com', to, content)
    server.close()

class gui:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x600')
        self.button = Button(self.root, text='Listen', command=self.listen)
        self.label_text = StringVar()
        self.label = Label(self.root, textvariable=self.label_text)
        self.button.pack()
        self.label.pack()
        wishMe()

    def listen(self):
        self.label_text.set('Say someting')
        query = takeCommand().lower()
        self.label_text.set('You said '+query)
        self.root.update()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir the time is {strTime}")
        elif 'open netbeans' in query:
            path = "C:\\Program Files\\NetBeans 8.2\\bin\\netbeans64.exe"
            os.startfile(path)
        elif 'email to ashu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'ashu1122sing@gmail.com'
                sendEmail(to, content)
                speak('Email sent successfully to ashu')
            except Exception as e:
                #print(e)
                speak('Sorry could not sent email')
        elif 'abuse' in query:
            speak('gaaandu madherchood')
            speak('bahen ka looda')
            speak('maa kii chuut teri')
        elif 'sun be' in query:
            speak('bol bosdhike')
        elif 'quit working' in query:
            speak('Thank you, for using me.')
            sys.exit(0)

    def run(self):
        self.root.mainloop()

if __name__=="__main__":
    #wishMe()
    obj = gui()
    obj.run()

