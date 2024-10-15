import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "7313a27268794eb8aa52bea2be81f581"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame
    pygame.mixer.init()

    # Load MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Wait until music has finished playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust tick() argument as needed

    pygame.mixer.music.unload()
    os.remove("temp.mp3")   


def aiProcess(command):
    client = OpenAI(api_key = "sk-VOkleE2Xrqif43yja8dDSoSz6ZfnvFRoAkNYTeks-qT3BlbkFJ87_orFgetkc9k99jyrjTujKoUp7hyEGEQKtPrIFnQA",
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant, skilled in  general tasks like Alexa and Google Cloud, Give short responses PLease"},
        {"role": "user", "content": command}
    ]
    )

    return(completion.choices[0].message) 


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")  
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com") 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link) 

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse JSON response
            data = r.json()

            # Extract headlines from the response
            articles = data.get('articles', [])

            # Print each headline
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)
                



if __name__ == "__main__":
    speak("Initializing Cypher.....")
   # Listen to the wake word "cypher" 
    while True:
        r = sr.Recognizer()
    

        # recognize speech using Google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            if(word.lower() == "cypher"):
                speak("Yeah")
                # listen for command
                with sr.Microphone() as source:
                    print("cypher active...")
                    audio = r.listen(source)
                    command= r.recognize_google(audio)
                    processCommand(command) 



        except Exception as e:
            print("Error; {0}".format(e))   