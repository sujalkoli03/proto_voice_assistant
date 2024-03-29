import win32com.client
# Voice assistant using openai made by Aishwarya & Sujal
import openai
from key import apikey
import pyttsx3
import speech_recognition as sr
import webbrowser
#import pyaudio
import os
import datetime

#****

#say = win32com.client.Dispatch("SAPI.SpVoice")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


chatStr = ""


def chat(question):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f'sujal & aish: {question}\n A S A I: '
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    speak(response["choices"][0]["text"])

    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.6
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"Aish and Sujal said: {query}")
        return query
    except Exception as e:
        return "sorry from Aish & Sujal please repeat"


if __name__ == '__main__':
    print("Voice assistant using openai made by Aishwarya & Sujal")

    speak("Voice assistant using openai made by Aishwarya & Sujal starting up")
    while True:
        print("Listening(aiktoy thamba jara)....")
        hukum = takeCommand()
        #say.Speak(text)
        sites = [["youtube", "https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google", "https://www.google.com/"],["udemy", "https://www.udemy.com/"],["my college", "https://www.nmiet.edu.in/"],["books", "https://books.google.com/"]]

        for site in sites:
            if f"Open {site[0]}".lower() in hukum.lower():
                speak(f"Opening {site[0]} aish & sujal..")
                webbrowser.open(site[1])
        if "the time" in hukum:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Sir time is {hour} vaajun {min} minutes")
        apps = [["game", "C:\\Users\\Public\\Desktop\\VALORANT.lnk"], ["vs code", "C:\\Users\\LEGION\\OneDrive\\Desktop\\Visual Studio Code.lnk"],
                 ["code blocks", "C:\\Users\\LEGION\\OneDrive\\Desktop\\CodeBlocks.lnk"], ["brave", "C:\\Users\\Public\\Desktop\\Brave.lnk"]]
        for app in apps:
            if f"Open {app[0]}".lower() in hukum.lower():
                speak(f"Opening {app[0]} aish & sujal..")
                os.startfile(app[1])
        if "the time" in hukum:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Sir time is {hour} vaajun {min} minutes")
        elif "bye" in hukum:
            speak("thanks for hanging out Aish and sujal")
            break
        elif "bro Quit".lower() in hukum.lower():
            speak("thanks for hanging out Aish and sujal")
            exit()
        elif "reset chat".lower() in hukum.lower():
            chatStr = ""
        elif "proto".lower() in hukum.lower():
            print("Chatting...")
            chat(hukum)



















