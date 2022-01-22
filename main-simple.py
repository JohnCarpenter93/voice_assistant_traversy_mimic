import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import time
import os # to remove created audio files


r = sr.Recognizer() # initialise a recogniser

# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"Robochatterbox: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

# Robochatterbox's responses
def respond(voice_data):
    
    # 1: greeting
    if "hello" in voice_data:
        speak("Hello, my name is robot chatter box")

    # 2: name
    if "what is your name" in voice_data:
        speak("My name is robot chatter box")

    # 3: time
    if "tell me the time" in voice_data:
        speak(ctime())

    # 4: search google
    if "google search" in voice_data:
        search_term = record_audio("What do you want to search for?")
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    # 5: exit the program
    if "goodbye" in voice_data:
        speak("going offline")
        exit()


time.sleep(1)

speak("How can I help you on this fine day?")

while 1:
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond