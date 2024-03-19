import openai
from Body.listen import micExecution
from Body.speak import speak
import datetime
import sys
import cv2
import pyautogui as p

import webbrowser
import os
import wikipedia
from requests import get 
import time
import shutil
import pyjokes
import pyautogui as pg
import requests
import instaloader
import PyPDF2
import pywhatkit as kit
from bs4 import BeautifulSoup
import pyautogui 
import speedtest
from img_gen import img_genertor


openai.api_key =  "Your API key"


print(">> Spider is Initializing : Just a moment.")


def chat_with_gpt(prompt):
    msg= openai.ChatCompletion.create(
        
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":prompt}]
    )
    
    return msg.choices[0].message.content.strip()

def spider_password():

    speak("--Speak the Password to Initialize Spider--")
    

    for i in range(3):
        password=micExecution().lower()
        
        if len(password)<3:
            spider_password()
        
        pw_file=open("password.txt","r")
        pw=pw_file.read()
    
        if password==pw:
            speak("Access Granted")
            speak("Spider has been Activated")
            # wake_up()
            User_recognizer()
            
        elif i==2 and password!=pw:
            speak("Access Denied")
            speak("Spider has been locked")
            exit()
            
        elif password!=pw:
            speak("Access Denied")
            chance=2-i
            speak(f"You have {chance} chances left")

def User_recognizer():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('Trainer/trainer.yml')

    # Load the cascade classifier
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Create a dictionary to map IDs to names
    names = {0: "Anuj"} 

    # Set the confidence threshold for face recognition
    confidence_threshold = 70

    # Open the webcam
    video_capture = cv2.VideoCapture(0)
    speak("Please Look into the Camera for Identification")
    

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Recognize the face
            id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

            # Check if the face is recognized
            if confidence < confidence_threshold:
                name = names[id]
                speak("Verification Completed")
                if name=="Vidhi" or name=="Shreya":
                    speak(f"Welcome Miss. {name}")
                else:
                    speak(f"Welcome Mr. {name}")
                wake_up()
            else:
                name = "Unknown"
                speak("User Unidentified")
                User_recognizer()

            # Draw a rectangle around the face and display the name
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and destroy the windows
    video_capture.release()
    cv2.destroyAllWindows()

            
def wake_up():
    
    query=micExecution()
    
    if len(query)<3:
        wake_up()

    elif "wake up" in query or "spider" in query or "WAKE UP" in query or "SPIDER" in query or "Alright" in query:
        print(">> Waking up Spider...")
        MainExe()
        
    else:
        wake_up()


def wish():
    hour = int(datetime.datetime.now().hour)
    tt=time.strftime("%H:%M %p")
    if hour > 0 and hour < 12:
        speak(f"Good Morning Sir!, Its {tt}")
    elif hour >= 12 and hour <= 15:
        speak(f"Good Afternoon Sir!, Its {tt}")
    elif hour > 15 and hour <= 20:
        speak(f"Good Evening Sir!, Its {tt}")
    else:
        speak(f"Hello Sir!, Its {tt}")
        

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def MainExe():
    wish()
    speak("You called me? I am here Boss")
    speak("So tell me what do you want me to do?")
    
    
    def response():
        while True:
            query=micExecution().lower()
            
            if len(query)<2:
                # speak("Boss I think you forgot to communicate...")k
                response()
            
                  
            if "google" in query:
                speak("Sir what do you want me to search on google")
                cmmnd=micExecution().lower()
                webbrowser.open(f"{cmmnd}")
                response()
            
            elif "gmail" in query:
                Gmpath = "https://www.gmail.com/"
                os.startfile(Gmpath)
                response()

            elif "facebook" in query:
                Fbpath = "https://www.facebook.com/"
                os.startfile(Fbpath)
                response()

            elif "camera" in query:
                cap = cv2.VideoCapture(0)  # 0:internal camera, 1:external camera
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()  # releasing the camera
                cv2.destroyAllWindows()
                response()

            elif "spotify" in query:
                Spath = "https://www.spotify.com/"
                os.startfile(Spath)
                response()
            
            # """performing the online task"""
            
            # to get the ip address from the get function of request module
            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP Adress is {ip}")
                response()

            elif "wikipedia" in query:
                speak("Sir what do you want me to search on wikipedia")
                cmnd=micExecution().lower()
                results = wikipedia.summary(f"{cmnd}",sentences=1)
                speak("According to wikipedia:") 
                speak(results)
                response()
                
            elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    response() 
                    
            elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the current time is {strTime}")
                    response()  
                    
                          
            # elif "open" in query:
            #         from dictapp import openappweb
            #         openappweb(query)
            #         response()
            # elif "close" in query:
            #         from dictapp import closeappweb
            #         closeappweb(query)
            #         response()
            
            elif "alarm" in query:
                    # print("input time example:- 10 and 10 and 10")
                    # speak("Set the time")
                    speak("Sir at what time you waant to set the alarm?")
                    a = input("Please tell the time :- ")
                    # a=micExecution().lower()
                    alarm(a)
                    speak("Done,sir")     
                    response()
            
            #Youtube Authentication
            
            elif "song" in query:
                speak("sir which song you want me to play")
                song=micExecution().lower()
                kit.playonyt(f"{song}")
                response()
            
            elif "pause" in query or "stop" in query:
                pyautogui.press("k")
                speak("video paused")
                response()
                
            elif "video" in query:
                pyautogui.press("k")
                speak("video played")
                response()
                
            elif "mute" in query:
                pyautogui.press("m")
                speak("video muted")   
                response()             
                    
            elif "volume up" in query:
                from keyboard import volumeup
                speak("Turning volume up,sir")
                volumeup()
                response()
                
            elif "volume down" in query:
                from keyboard import volumedown
                speak("Turning volume down, sir")
                volumedown()  
                response()    
             
            #Memorizing       
            elif "remember" in query:
                speak("Boss what do you want me to remember?")
                remember=micExecution().lower()
                rememberMessage = remember.replace("remember","")
                rememberMessage = remember.replace("spider","")
                # speak("You told me"+rememberMessage)
                speak("OK Boss! Noted...")
                remember = open("Remember.txt","a")
                remember.write(rememberMessage)
                remember.close()
                response()
                
            elif "something" in query or "remind" in query:
                remind = open("Remember.txt","r+")
                speak(remind.read())
                # if "i" in remind or "I" in remind:
                #     msg=str(remind)
                #     new_msg=msg.replace("i","You")
                #     new_msg=msg.replace("I","You")
                #     print(new_msg)
                #     speak(new_msg)   
                # else:
                #     speak(remind.read()) 
                remind.truncate(0)   
                remind.close()   
                response()
                
            
            # news        
            elif "news" in query:
                from NewsRead import latestnews
                latestnews()       
                response() 
             
            #calculating any value       
            elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("spider","")
                    Calc(query)
                    response()       
            
            #whatapp automation
            elif "message" in query:
                speak("Boss to whome you want to send the message?") 
                from whatsApp import sendMessage
                sendMessage()
                response()   
                
            #Controlling the system
            elif "shut down" in query:
                os.system("shutdown /s /t 5")   
            
            elif "restart" in query:
                os.system("shutdown /r /t 5")     
                
            elif "sleep" in query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")    
               
            
            elif "open" in query:
                #EASY METHOD
                query = query.replace("open","")
                query = query.replace("spider","")
                pyautogui.press("super")
                pyautogui.typewrite(query)
                pyautogui.sleep(2)
                pyautogui.press("enter")
                response()
                   
            elif "internet speed" in query:
                wifi  = speedtest.Speedtest()
                upload_net = round(wifi.upload()/1048576,2)         #Megabyte = 1024*1024 Bytes
                download_net = round(wifi.download()/1048576,2)
                speak(f"Wifi download speed is {download_net} mbps")
                speak(f"Wifi Upload speed is {upload_net} mbps")  
                response()  
                
            elif "play a game" in query:
                from game import game_play
                game_play()
                response()
            
                
                
            elif "movie" in query or "Movie" in query:
                
                speak("Boss i have 3-4 movies on my system")
                speak("Which movie do you want to watch?")
                movie_names=micExecution().lower()
                speak("I have")
                speak("50 Shades of Grey")
                speak("Godzilla versus King Kong")
                speak("Conjuring : The Devil made me do it, your favourite one")
                speak("and The Invicible Man")
                movie=micExecution().lower()
                if "shades" in movie:
                    apath="C:\\Users\\anujb\\Videos\\Movies\\50 Shades of grey\\Fifty.Shades.of.Grey.2015.Hindi.Dubbed.HDRip.mkv"
                    os.startfile(apath)
                    response()
                    
                elif "godzila" in movie:
                    bpath="C:\\Users\\anujb\\Videos\\Movies\\Godzilla vs King Kong\Godzilla.vs.Kong.2021.ORG.1080p.HD.DesireMoVies.RED.mkv"  
                    os.startfile(bpath) 
                    response()

                elif "conjuring" in movie:
                    cpath="C:\\Users\\anujb\\Videos\\Movies\\Conjuring\\5_6212835292206859403.mp4"
                    os.startfile(cpath)
                    response()

                elif "invicible" in movie:
                    dpath="C:\\Users\\anujb\\Videos\\Movies\\The Invicible Man\\The_Invisible_Man_(2020).mkv"
                    os.startfile(dpath)
                    response()
                
                else:
                    speak("Sorry Boss i dont have this movie")
                    response()  

                    
            elif "image" in query:
                speak("Boss what type of image do you want?")
                img=micExecution().lower()
                img_genertor(img,"img.png")
                speak("Boss I have generated your Image! Kindly Check")
                response()
                
            
                    
            msg=chat_with_gpt(query)
            speak(msg)   
            
            if "by" in query or "Goodbye" in query or "goodbye" in query:
                sys.exit()
                
    response()    
        
# spider_password()   
# wake_up() 



