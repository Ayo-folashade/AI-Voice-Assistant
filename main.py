import datetime
import subprocess
import webbrowser
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from pyjokes import pyjokes
from speech_recognition import Recognizer
from ecapture import ecapture as ec
import requests

listener: Recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jezz' in command:
                command = command.replace('jezz', '')
                print(command)
    except:
        pass
    return command

def run_jezz():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'are you in a relationship' in command:
        talk('No am not, but i do have a secret crush')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open google' in command:
        webbrowser.open_new_tab("https://www.google.com")
        talk("Google chrome is open now")
    elif 'search' in command:
        command = command.replace("search", "")
        webbrowser.open_new_tab(command)
        talk("Your search has finished loading")
    elif 'open gmail' in command:
        webbrowser.open_new_tab("gmail.com")
        talk("Google Mail open now")
    elif 'news' in command:
        news = webbrowser.open_new_tab("https://guardian.ng/")
        talk('Here are some headlines from The Guardian, Happy reading')
    elif "camera" in command or "take a picture" in command:
        ec.capture(0, "robo camera", "img.jpg")
        talk("Picture taken")
    elif "weather" in command:
        api_key = "key"
        base_url = "url"
        talk("what city")
        city_name = take_command()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            talk(" Temperature in kelvin unit is " +
                  str(current_temperature) +
                  "\n humidity in percentage is " +
                  str(current_humidiy) +
                  "\n description  " +
                  str(weather_description))
            print(" Temperature in kelvin unit = " +
                  str(current_temperature) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))
    else:
        talk('Did not catch that.')

while True:
    run_jezz()
