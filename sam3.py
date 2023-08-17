import pyttsx3                   #to convert text to speech
import speech_recognition as sr  #to convert speech to text
import webbrowser                #opens webbrowser
import datetime                  #for date and time
import wikipedia                 # to get information from wiki           
import requests           
import pyjokes                   #Cracks jokes when asked
import keyboard
from tkinter import * 
import numpy as np
import cv2 
import pyautogui
from PIL import ImageTk,Image
#import PIL.Image, PIL.ImageTk     
       


assistant_name = "doodle"  #name of assistant 

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():
  
    r = sr.Recognizer()
  
    # from the speech_Recognition module 
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')
          
        # seconds of non-speaking audio before 
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)
          
        # Now we will be using the try and catch
        # method so that if sound is recognized 
        # it is good else we will have exception 
        # handling
        try:
            print("Recognizing")
              
            # for Listening the command in india english 
            # we can also use 'hi-In' for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
              
        except Exception as e:
            print(e)
            speak("Say that again")
            return "None"
          
        return Query
  
def speak(audio):
      
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')
      
    # setter method .[0]=male voice and 
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[0].id)
      
    # Method for the speaking of the the assistant
    engine.say(audio)  
      
    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()
  
def tellDay():
      
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number 
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
  

def greet():
    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning ")
    elif (hour >= 12) and (hour < 18):
        speak(f"Good afternoon")
    elif (hour >= 18) and (hour < 21):
        speak(f"Good Evening ")
    speak("How may I assist you?")



 
def tellTime():
      
    # This method will give the time
    time = str(datetime.datetime.now())
      
    # the time will be displayed like 
    # this "2020-06-05 17:50:14.582630"
    #nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is " + hour + "Hours and" + min + "Minutes")    

def weather():

    city = "hyderabad"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    speak(
        f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")


def Take_query():
  
    # calling the greet function for 
    # making it more interactive
    #greet()

      
    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate 
    # the program
    while(True):
          
        # taking the query and making it into
        # lower case so that most of the times 
        # query matches and we get the perfect 
        # output
        query = takeCommand().lower()
        if "open youtube" in query:
            speak("Opening youtube")
              
            # in the open method we just to give the link
            # of the website and it automatically open 
            # it in your default browser
            webbrowser.open("www.youtube.com")
            continue
          
        elif "google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
              
        elif "day" in query:
            tellDay()
            continue
          
        elif "time" in query:
            tellTime()
            continue
          
        #this will exit and terminate the program
        elif "bye" in query:
            speak("Bye")
            exit()
          # this will exit and terminate the program
        elif "bhai" in query:
          speak("Bye")
          exit()
 


        #elif "remember" in query:
        #  Tremember()
          
        elif "from wikipedia" or "about" in query:
              
            # if any one wants to have a information
            # from wikipedia
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
              
            # it will give the summary of 3 lines from 
            # wikipedia we can increase and decrease 
            # it also.
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            speak(result)
          
        elif "your name" in query:
            speak("I am Sam. Your desktop Assistant")

        elif "weather" in query:
            weather()

        elif "joke" in query:
            speak(pyjokes.get_joke())

       # elif "screenshot" in query:
            speak("taking screenshot")
        #    image = pyautogui.screenshot()
        #   image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
         #   cv2.imwrite("image1.png",image)
         #   print("image is stored in sam folder")

        elif "Hi" or "Hello" in query:
          speak("Hello there")

  
if __name__ == '__main__':
      
    # main method for executing
    # the functions
    Take_query()
    #widget = widget()
  