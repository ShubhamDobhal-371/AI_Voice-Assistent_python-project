from email.mime import audio
from time import *
from unittest import main
import pyttsx3 #convert Text to voice
import speech_recognition as sr #convert voice to text
import datetime
import os#operating system 
import cv2#use for webcam operation
import random
import socket
import wikipedia
import webbrowser
import pywhatkit as kit #{this three pakage is used for youtube and browsing}
#import vlc
#import pafy
import pyautogui
import pyjokes
import time
import requests
import geocoder
from geopy.geocoders import Nominatim
import sys
import speedtest
import csv
import numpy as np
import face_recognition
import os
import json

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)#using setproperty methode we can set the voice of our ai
engine.setProperty('rate',160)#speech[rate] speed adjust

def speak(audio):#speak function it take text argument and convert in to voice
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():#take the user command through microphone(convert voice to text)
    try:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold=1.9
            audio = r.listen(source,timeout=1,phrase_time_limit=5)
            

        
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said :{query}")
    except Exception as e:
        time.sleep(3)
        speak("say that again please..")
        return "none"

    return query

def wish():# this function is wish function and wish
    hour = int(datetime.datetime.now().hour)
    time_now = datetime.datetime.now()
    tStr = time_now.strftime('%H:%M')


    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<=18:
        speak("good afternoon")
    else:
        speak("good evening")
    
    speak(f"its {tStr}")

    speak("i am jarvis sir,i am your personal AI based voice assistent,how can i help you")



def notepad():

    speak("tell me the query .")
    speak("i am ready to write .")
    writes=takecommand()

    time=datetime.datetime.now().strftime("%H:%M:%S")
    filename=str(time).replace(":","-") + "-note.txt"
    with open(filename,"w") as file:
        file.write(writes)
    path1="C:\\Users\\shubhu rajput\\python26\\" + str(filename)
    path2="C:\\Users\\shubhu rajput\\python26\\Database\\Notepad\\" + str(filename)

    os.rename(path1,path2)
    os.startfile(path2)
def TimeTable():
    speak("wait sir i will checking...")

    FiveTo6 ='''In this time , you have to get up and listen something positive
5:00 Am to 6:00 Am 
thanks'''

    SixTo9 ='''
In this time  , You have to study
6:00 am to 9:00 Am
thanks'''

    NineTo10=''' get ready for college 
9:00 am to 9:30 Am
thanks'''

    TenTo17=''' You Have to do Lectures and practicals and Other college Works
10:00 am to 5:00 pm
thanks'''

    EighteenTo21='''Its time for chilling and  watch movies , web series 
6:00 pm to 9:00 pm
thanks'''

    hour=int(datetime.datetime.now().strftime("%H"))

    if hour>=5 and hour<=6:
        speak(FiveTo6)
        return FiveTo6

    elif hour>=6 and hour<=9:
        speak(SixTo9)
        return FiveTo6

    elif hour>=9 and hour<=10:
        speak(NineTo10)
        return NineTo10

    elif hour>=10 and hour<=17:
        speak(TenTo17)
        return TenTo17

    elif hour>=18 and hour<=21:
        speak(EighteenTo21)
        return EighteenTo21

    else:
        speak("Its time to sleep")
        return '''In this time , You have to sleep .'''

# def latestnews():
#     api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=5b82b45932bd4045a6069a2e0b86b4b6",
#             "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=5b82b45932bd4045a6069a2e0b86b4b6",
            
#             "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=5b82b45932bd4045a6069a2e0b86b4b6",
#             "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=5b82b45932bd4045a6069a2e0b86b4b6",
#             "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=5b82b45932bd4045a6069a2e0b86b4b6"

# }

#     content = None
#     url = None
#     speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
#     field = input("Type field news that you want: ")
#     for key ,value in api_dict.items():
#         if key.lower() in field.lower():
#             url = value
#             print(url)
#             print("url was found")
#             break
#         else:
#             url = True
#     if url is True:
#         print("url not found")

#     news = requests.get(url).text
#     news = json.loads(news)
#     speak("Here is the first news.")

#     arts = news["articles"]
#     for articles in arts :
#         article = articles["title"]
#         print(article)
#         speak(article)
#         news_url = articles["url"]
#         print(f"for more info visit: {news_url}")

#         a = input("[press 1 to cont] and [press 2 to stop]")
#         if str(a) == "1":
#             pass
#         elif str(a) == "2":
#             break
        
#     speak("thats all")


def att():

    path = r'C:\Users\shubhu rajput\python26\facedetection project\photos'
    images = []
    personNames = []
    myList = os.listdir(path)
    #print(myList)

    for cu_img in myList:
        current_Img = cv2.imread(f'{path}/{cu_img}')
        images.append(current_Img)
        personNames.append(os.path.splitext(cu_img)[0])
    #print(personNames)

    def faceEncodings(images):#encoding function the different points from the face(128 different)
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#when the take image from camera we get in "BGR" formate so hence we convert in to the "RGB form" 
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnown=faceEncodings(images)

    speak("Authorization Process in Progress")

    def attendance(name):
        with open(r'C:\Users\shubhu rajput\python26\facedetection project\attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])

            if name not in nameList:
                time_now = datetime.datetime.now()
                tStr = time_now.strftime('%H:%M:%S')
                dStr = time_now.strftime('%d/%m/%Y')
                f.writelines(f'\n{name},{tStr},{dStr}')
                

    


    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)#face distance find the distance of face if its less then face match
            # print(faceDis)
            matchIndex = np.argmin(faceDis)#np.argmin face distance list madhun min value find karta hai [find minimum distance value]

            if matches[matchIndex]:
                name = personNames[matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)#use to create ragtangle on the face
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)#use to give name on the rechtangle
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)#use to give name on the rechtangle and which font and color,thickness
                
                speak(name)

                attendance(name)
                return name

        cv2.imshow("Camera",frame)
        if cv2.waitKey(10)==13:
            break
    cap.release()
    cv2.destroyAllWindows()  

def taskExicution():

    na=att()
    print(na)

    if na=="SHUBHU":
        speak("you are authorize user..")
        wish()

        while True:
            query=takecommand().lower()

            #logic for task


            if "hey jarvis"  in query:
                speak("hi sir")

            elif "how are you" in query:
                speak("i am good, what about you.")

            elif "who made you" in query:
                speak("i was born when shubham made me on 7th of september 2022")

            elif "tell me about yourself" in query:
                speak("Jarvis is my name , helping you is my game,i can look upon weather or give you latest update. aks,and you shall know,my operating speed is 15262731.88611502 byte,")

            elif "thank you" in query:
                speak("i am here to help")

            elif "i love you" in query:
                speak("aww i would like to express my feeling through a love poem. would you like to here one?")
                c=takecommand()
                

            elif "open notepad" in query:
                # npath="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories/Notepad"
                # os.startfile(npath)
                notepad()
            elif "close notepad" in query:
                speak("okay sir closing notepad...")
                os.system("TASKKILL/F /IM \"Notepad.exe\"")

                

            elif "open command prompt" in query:
                os.system('start cmd')

            elif "open camera" in query: 

                cap=cv2.VideoCapture(0)#used to open default laptop camera
                speak("press escape key for closed camera")
                while True:
                    ret,img=cap.read()
                    cv2.imshow('webcam',img)
                    k=cv2.waitKey(1)
                    
                    if cv2.waitKey(1) and 0xFF==ord('q'):
                        break

                else:
                    break
                cap.relese()
                cv2.destroyAllWindows()

            elif "play music" in query:
                music_dir="D:\music"
                songs=os.listdir(music_dir)
                
                rd=random.choice(songs)
                print(rd)
                os.startfile(os.path.join(music_dir,rd))

            elif "ip address" in query:
                hostname=hostname = socket.gethostname()
                ip=socket.gethostbyname(hostname)
                speak(f"your ip address is:{ip}")


            elif "wikipedia" in query:
                speak("searching wikipidia...")
                query=query.replace("wikipedia","")
                result=wikipedia.summary(query,sentences=1)
                speak("according to wikipedia")
                speak(result)

            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")

            elif "open google" in query:
                speak("sir,what should search on google")
                cm=takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "open instagram" in query:
                webbrowser.open("www.instagram.com")

            elif "open javatreepoint" in query:
                webbrowser.open("www.javatpoint.com")

            elif "send message" in query:
                current_time=datetime.datetime.now()
                h=current_time.hour
                m=current_time.minute

                speak("what message you want to send...")
                kit.sendwhatmsg("+917020341372","hi dada kasho hai majama hai ki",h,m+2)

            elif "shutdown" in query:
                os.system("shutdown/s")

            elif "restart"in query:
                os.system("restart/r")

            elif "logout" in query:
                os.system("shutdown -l") 

            elif "hidden menu" in query:
                pyautogui.hotkey('winleft','x')      

            elif "task manager" in query:
                pyautogui.hotkey('ctrl','shift','esc')

            elif "task view" in query:
                pyautogui.hotkey('winleft','tab')
                
            elif "which window" in query:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')

            elif "exit" in query:
                speak("thank you sir have a nice day")
                exit()
            elif "screenshot" in query:
                img =pyautogui.screenshot()
                img.save("D:/jarvis screenshort/ss.png")
                speak("done.")

            elif "news" in query:
                from NewsFetch import latestnews
                latestnews()
                
            elif "joke" in query:
                joke=pyjokes.get_joke()
                speak(joke)

        
                
            
                

            elif "get my location" in query:
                ip=geocoder.ip("192.168.240.105")
                ip=geocoder.ip("me")
                latitude,longitude=ip.latlng
                la=str(latitude)
                lo=str(longitude)

                geolocator=Nominatim(user_agent="geoapiExecises")
                location=geolocator.reverse(la+","+lo)
                speak(f" sir i am not sure but we are in {location}")
                
            elif "internet speed" in query:
                speak("wait a second...")
                st=speedtest.Speedtest()
                dl=st.download()
                up=st.upload()
                speak(f"downloading speed is {dl} byte and uploading speed is{up} byte ")

            elif "detect me" in query:
                speak("sir detection process in progress please wait a second....")
                att()
            
            elif "my time table" in query:
                TimeTable()

            
    elif na!="SHUBHU" or na==None:
        speak("sorry Authorization fail!!")
        exit()



if __name__ == "__main__":
    
    while True:
        permission=takecommand().lower()
        if "wake up" in permission:
            taskExicution()

        elif "goodbye" in permission:
            sys.exit()
            
        
        
        
        
    

    






    