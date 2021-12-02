import gtts
from gtts.tts import gTTS
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import random
import wikipedia
import datetime
import pyautogui
import webbrowser
import keyboard
import pyjokes
from PyDictionary import PyDictionary as dic
import datetime
from playsound import playsound
from tkinter import Label,Entry,Button,Tk,StringVar #for gui
from pytube import YouTube #for you tube video download
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
import PyPDF2
from gtts import gTTS
import speedtest
from pywikihow import search_wikihow
import psutil
import cv2
from send_whatsapp_msg import sending_msg
import smtplib
from my_translator import my_trans



engine = pyttsx3.init('sapi5')  #for taking voice from windows
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)  #for setting voice - male or female voice...0=male , 1=female
#print(voices[1].id)

#engine.setProperty('rate',100)  #speaking speed

def speak(audio):
    engine.say(audio)
    print(audio)
    print("   ")
    engine.runAndWait()

def wish_me() :   #depending on time
    hour = int(datetime.datetime.now().hour)
    if hour >=4 and hour<12 :
        speak("Good morning Anushka!")

    elif hour>=12 and hour<=17 :
        speak("good afternoon Anushka")

    elif hour>=18 and hour<=22 :
        speak("good evening anushka")

    else   : 
        speak("Hey it's night time...greetings of the day Anushka...")

    f=open("nick_name.txt") #read the name
    name=f.read()
    f.close()
    data="I am"+name+"your desktop assistant...How can i help you"
    speak(data)

def takeCommand():   #takes microphone input from user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        
        #print("Listening...")
        print("speak")
        print('recognizing...')
        r.pause_threshold=1   #gap (waiting) while speaking...predefined  #also other speaking and toning attributes can be changed
        r.energy_threshold=9000   #important

        audio=r.listen(source)
        
        try :   #incase error occurs
            
            #print("Recognizing")
            query=r.recognize_google(audio, language='en-in')
            print("User said : ",query)

        except Exception as e:   #when no recogntn happens
            print("Say that again please...")
            return "None"

        return query.lower()

def music():
    speak("Do you want to name a song?")
    choice = takeCommand()

    if 'no' in choice :
        speak("okay maam! playing a random song from dextors choice....enjoy the song ")
        music_dir = 'C:\\Users\\PC\\Desktop\\music'
        song= os.listdir(music_dir)
        #print(song,type(song))
        r=random.randint(0,len(song))
        os.startfile(os.path.join(music_dir,song[r])) #starting the song

    else:  #users chocie of song
        speak("tell the name of the song you want to hear")
        music_name = takeCommand()  #rakes music name from user
        speak("Enjoy your choice of song")
        music_dir = 'C:\\Users\\PC\\Desktop\\music'  #path 
        song= os.listdir(music_dir) #all list r here. now from this list song name gvn by user is compared and played accrdnly. if not in list , then from YT songs
        music_choice =music_name+'.mp3'  #users choice..then searchd in the list for that song

        if music_choice in song :
            file=music_dir+'\\'+music_choice
            os.startfile(file)

        else:

            pywhatkit.playonyt(music_name)

def nick_name():
    f=open("nick_name.txt",mode='w')
    speak("maam tell the nickename which you want to give for your assistant")
    take=takeCommand()
    f.write(take)
    f.close()
    speak(f"my new nick name is{take}")

def youtube_auto():
    speak("What is your command ma'am...")

    while True:
        cm=takeCommand()

        if 'play' in cm:
            keyboard.press('space bar') 
        if 'puase' in cm:
            keyboard.press('space bar') 
        elif 'restart' in cm:
            keyboard.press('0')
        elif 'skip' in cm:
            keyboard.press('l')
        elif 'back' in cm:
            keyboard.press('j')
        elif 'out of full screen' in cm:
            keyboard.press('f')
        elif 'full screen' in cm:
            keyboard.press('f')
        elif 'out of film mode' in cm:
            keyboard.press('t')
        elif 'film mode' in cm:
            keyboard.press('t')
        elif 'unmute' in cm:
            keyboard.press('m')
        elif 'mute' in cm:
            keyboard.press('m')
        elif 'start the video' in cm:
            keyboard.press('k')
        elif 'half screen' in cm:
            keyboard.press('f')
        elif 'next video' in cm:
            keyboard.press('SHIFT+n')
        elif 'previous video' in cm:
            keyboard.press('SHIFT+p')
        elif 'decrease playback rate' in cm:
            keyboard.press('SHIFT+,')
        elif 'increase playback rate' in cm:
            keyboard.press('SHIFT+.')

        #for stopping automation
        i=0
        f=0
        list=['stop','off automation','stop automation','close automation','nothing','leave']
        while(i<len(list)):
            if list[i] in cm:
                speak("Ok ma'am stopping youtube automation")
                f=1
            i=i+1
               
        if(f):
            break

def chrome_auto() :
    speak("chrome automation started")
    
    while True:
        com=takeCommand()
        if 'close this tab' in com:
            keyboard.press_and_release('Ctrl + w')
        elif 'close this window' in com:
            keyboard.press_and_release('Alt + F4')
        elif 'close the window' in com:
            keyboard.press_and_release('Alt + F4')
        elif 'close window' in com:
            keyboard.press_and_release('Alt + F4')
        elif 'new tab' in com:
            keyboard.press_and_release('Ctrl + t')
        elif 'new window' in com:
            keyboard.press_and_release('Ctrl + t')
        elif 'menu' in com:
            keyboard.press_and_release('Alt+F')
        elif 'incognito mode' in com:
            keyboard.press_and_release('Ctrl + Shift + n')
        elif 'next tab' in com:
            keyboard.press_and_release('Ctrl + PgDn')
        elif 'previous tab' in com:
            keyboard.press_and_release('Ctrl + PgUp')
        elif 'go to tab 1' in com:
            keyboard.press_and_release('Ctrl + 1')           
        elif 'rightmost tab' in com:
            keyboard.press_and_release('Ctrl + 9')
        elif 'minimize window' in com:
            keyboard.press_and_release('Alt + Space +n')
        elif 'maximize window' in com:
            keyboard.press_and_release('Alt + Space +x')
        elif 'print the page' in com:
            keyboard.press_and_release('Ctrl + p')
        elif 'reload the current page' in com:
            keyboard.press_and_release('F5')
        elif 'chrome history' in com:
            keyboard.press_and_release('Ctrl + h')
        elif 'top of the page' in com:
            keyboard.press_and_release('Home')
        elif'bottom of the page' in com:
            keyboard.press_and_release('End')
        elif 'show bookmark' in com:
            keyboard.press_and_release('Ctrl + Shift + o')
        elif 'open file' in com:
            keyboard.press_and_release('Ctrl + 0')
        
        i=0
        f=0
        list=['off automation','stop automation','close automation','nothing','leave']
        while(i<len(list)):
            if list[i] in com:
                speak("Ok sir stop chrome automation")
                f=1
            i=i+1
               
        if(f):
            break

def apps_open(query):

    if 'open youtube' in query :
        webbrowser.open("youtube.com")

    elif 'open google' in query :
        webbrowser.open("google.com")

    elif 'open instagram' in query :
        webbrowser.open("instagram.com")

    elif 'open whatsapp' in query :
        webbrowser.open("whatsapp.com")

    elif 'open netflix' in query :
        speak("Opening netflix..")
        webbrowser.open("Netflix.com")

    elif 'open virtual studio code' in query :
        codepath = "C:\\Users\\PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    elif 'open chrome' in query :
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")   #for opening

def close_app(query):
    
    if "chrome" in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif "youtube" in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif "code" in query:
        os.system("TASKKILL /F /im code.exe")

    elif "telegram" in query:
        os.system("TASKKILL /F /im Telegram.exe")

    elif "instagram" in query:
        os.system("TASKKILL /F /im instagram.exe")

    elif "facebook" in query:
        os.system("TASKKILL /F /im facebook.exe")

def wiki(query):
    speak('Searching in wikipedia...please wait for a moment !')

    query = query.replace('dextor' , '')
    query = query.replace('search' , '')
    query = query.replace('in' , '')
    query = query.replace('wikipedia' , '')  #searching the query in wikipedia
    qu=query.replace(" ","_")  #for opening wikipda webpg need _
   
    #try except use for if not found in wikipeia and handle the error
    try:
                que="https://en.wikipedia.org/wiki/"+qu #open wikipedia
                webbrowser.open(que) #open
                wiki=wikipedia.summary(query,5) #for searching in wikipedia for info : 5-> no .of lines
                speak("According to the wikipedia...!")
                speak(wiki) #speak

    except:
                speak("Not match anything in wikipedia... can i searh in google")
                take=takeCommand()
                if 'no' in take:
                    speak("Ok sir.. you can ask anything")
                else:
                    speak("Ok sir,this is what i found for your serach")
                    pywhatkit.search(query)

def rept_words():
            speak("speak maam !")
            
            while True:
                word=takeCommand()

                li_stop=['stop no more','stop please','stop','please no more','no more','end please']
                i=0
                f=0

                while(i<len(li_stop)):
                    if li_stop[i] in word:
                        f=1
                        break   #inner loop breaks if stop

                    i=i+1
                    
                if(f==1):
                    speak("Ok cool sir...now stop the repeatition mode..")
                    break  #for breaking whole loop for stop

                speak(word)

def joke_speak():
    get=pyjokes.get_joke(language='en',category='all')
    speak(get)

    speak("How was the joke...?")
    li=['worst','ghatia','bekar','not good','bad', 'average', 'not upto the standard']
    choice=takeCommand()

    i=0
    f=0
    while(i<len(li)):
        if li[i] in choice:
            f=1
        i=i+1
    if(f==1):   #bad joke
        speak("sorry maam can i try a new joke?")
        ch=takeCommand()
        li_ch=['no','stop','leave','enough','no more', 'not required']
        i=0
        f=0
        while(i<len(li_ch)):
            if li_ch[i] in ch:
                f=1

            i=i+1
        if(f==1):
            speak('okay maam...Next time i will try to tell a better jokes')

        else:   #if continue
            speak("Thanks maam for giving me one more chance...here is a new joke for you maam")
            joke_speak()

    else:  #non bad joke
        speak("glad that you liked the joke...! Do you want to hear more jokes ?")
        ch=takeCommand()
        li_ch=['no','stop','leave','enough','no more','no thank you']
        i=0
        f=0
        while(i<len(li_ch)):
            if li_ch[i] in ch:
                f=1
            i=i+1
        if(f==1):
            speak('ok maam.')

        else:  #yes wants more jokes
            speak("here is the next joke for you..")
            joke_speak()

def dict():
    speak("Activated dictionary")
    speak("what do you want to know ma'am !")
    prb1=takeCommand()

    #for getting the meaning of a word
    if 'meaning' in prb1:
        prb1=prb1.replace('what is the',"")
        prb1=prb1.replace('of',"")
        prb1=prb1.replace('dexter',"")
        prb1=prb1.replace('meaning',"")
        prb1=prb1.replace(' ',"")

        result=dic.meaning(prb1)
        speak(f"the meaning of {prb1} is {result}")

    elif 'synonym' in prb1 :
        prb1=prb1.replace('what is the',"")
        prb1=prb1.replace('of',"")
        prb1=prb1.replace('dexter',"")
        prb1=prb1.replace('synonym',"")
        prb1=prb1.replace(' ',"")

        result=dic.synonym(prb1)
        speak(f"the synonym of {prb1} is {result}")

    elif 'antonym' in prb1 :
        prb1=prb1.replace('what is the',"")
        prb1=prb1.replace('of',"")
        prb1=prb1.replace('dexter',"")
        prb1=prb1.replace('antonym',"")
        prb1=prb1.replace(' ',"")

        result=dic.antonym(prb1)
        speak(f"the meaning of {prb1} is {result}")


#translator   
def take_beng():    #taking command in any language

    r=sr.Recognizer()
    with sr.Microphone() as source:
        
        #print("Listening...")
        print("speak")
        print('recognizing...')
        r.pause_threshold=1   #gap (waiting) while speaking...predefined  #also other speaking and toning attributes can be changed
        r.energy_threshold=9000
        audio=r.listen(source)
        
        try :   #incase error occurs
            
            print("Recognizing")
            query=r.recognize_google(audio, language='bn')
            print("User said : ",query)

        except Exception as e:   #when no recogntn happens
            print("Say that again please...")
            return "None"

        return query.lower()

def trans() :    #translating the command 
    speak("Tell me the line for translation")
    line = take_beng()
    translt = Translator()
    result = translt.translate(line,dest='en')
    txt = result.text
    speak("The translation for this line is :"+txt)


def temp(query):
    #srch= "temperature in kolkata
    query = query.replace("today's" , '')

    url = f"https://www.google.com/search?q={query}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div", class_ ="BNeawe").text
    speak("The temperature is : "+temperature)


def audiobook():
    speak("Tell me the name of the book")

    name= takeCommand()

    if 'constitution' in name :

        os.startfile("C:\\Users\\PC\\Desktop\\books-dextor audiobook\\constitution.pdf")
        book = open("C:\\Users\\PC\\Desktop\\books-dextor audiobook\\constitution.pdf",'rb')
        pdf_rdr= PyPDF2.PdfFileReader(book)
        pages = pdf_rdr.getNumPages()     #to get page number of the book
        speak(f"The number of pages in the book are : {pages}")

        speak("From which page I have to start reading ?")
        numPg = int(input("Enter the page number to start from : "))
        page = pdf_rdr.getPage(numPg)
        text = page.extractText()

        speak("In which language I have to speak ?")
        lang=takeCommand()


        if 'bengali' in lang :
            transl = Translator()
            textBeng = transl.translate(text,'bn')
            textm = textBeng.text
            speech= gTTS(text=textm)

            try :
                speech.save("book.mp3")
                playsound("book.mp3")

            except :
                playsound("book.mp3")

        elif 'english' in lang :
            transl = Translator()
            textBeng = transl.translate(text,'en')
            textm = textBeng.text
            speech= gTTS(text=textm)

            try :
                speech.save("book.mp3")
                playsound("book.mp3")

            except :
                playsound("book.mp3")

        elif 'hindi' in lang :
            transl = Translator()
            textBeng = transl.translate(text,'hi')
            textm = textBeng.text
            speech= gTTS(text=textm)

            try :
                speech.save("book.mp3")
                playsound("book.mp3")

            except :
                playsound("book.mp3")


        else :
            speak(text) # eng lang read

    

    elif '0' in name :

        os.startfile("C:\\Users\\PC\\Desktop\\books-dextor audiobook\\zero.pdf")
        book = open("C:\\Users\\PC\\Desktop\\books-dextor audiobook\\zero.pdf",'rb')
        pdf_rdr= PyPDF2.PdfFileReader(book)
        pages = pdf_rdr.getNumPages()     #to get page number of the book
        speak(f"The number of pages in the book are : {pages}")

        speak("From which page I have to start reading ?")
        numPg = int(input("Enter the page number to start from : "))
        page = pdf_rdr.getPage(numPg)
        text = page.extractText()

        speak("In which language I have to speak ?")
        lang=takeCommand()


        if 'bengali' in lang :
            transl = Translator()
            textBeng = transl.translate(text,'bn')
            textm = textBeng.text
            speech= gTTS(text=textm)

            try :
                speech.save("book.mp3")
                playsound("book.mp3")

            except :
                playsound("book.mp3")

        elif 'english' in lang :
            transl = Translator()
            textBeng = transl.translate(text,'en')
            textm = textBeng.text
            speech= gTTS(text=textm)

            try :
                speech.save("book.mp3")
                playsound("book.mp3")

            except :
                playsound("book.mp3")

        elif 'hindi' in lang :
            transl = Translator()
            textBeng = transl.translate(text,'hi')
            textm = textBeng.text
            speech= gTTS(text=textm)

            try :
                speech.save("book.mp3")
                playsound("book.mp3")

            except :
                playsound("book.mp3")

        else :
            speak(text) # eng lang read

            
def intrnt_speed_test(query):
    speak("Checking internet speed.....")
    speed = speedtest.Speedtest()

    downloading = speed.download()   #gives downloading speed in mbpt
    mbpsdownld = int(downloading/800000)  #to convert mbpt to mbps

    uploading = speed.upload()   #gives uoploading speed in mbpt
    mbpsupld = int(uploading/800000)

    if 'uploading speed' in query :
        speak(f"The uploading speed is {mbpsupld} mbps")

    elif 'downloading speed' in query :
        speak(f"The downloading speed is {mbpsdownld} mbps")

    else :
        speak(f"The downloading speed is {mbpsdownld} mbps and The uploading speed is {mbpsupld} mbps")


#email sending   -merror
def sendEmail(to,content) :
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','password')
    server.sendmail('sender email',to,content)
    server.close()


def email():
    speak("Write your content of the mail")
    content = takeCommand()
    speak("To whom do you want to send this email ?")
    to = input("Enter the email id of the person : ")
    sendEmail(to,content)
    speak("The email has been send")



def yt_download():
    root=takeCommand()
    root.geometry('500x300')
    root.resizable(0,0)
    root.title("Youtube Video Downloader")
    Label(root,text='Youtube Video Downloader',font='arial 15 bold').pack()
    speak("Sir...Enter the Video link")
    link=StringVar()
    Label(root,text="Paste Link Here",font='arial 15 bold').place(x=160,y=60)
    Entry(root,width=70,textvariable=link).place(x=32,y=90)

    def videoDownloader():
        url=YouTube(str(link.get()))
        video=url.streams.first()
        video.download('C:\\Users\\KABIR\\Desktop\\My Video')
        Label(root,text='Downloaded',font='arial 15 bold').place(x=180,y=210)
    
    Button(root,text='Download',font='arial 15 bold',bg='pale violet red',padx=2,command=videoDownloader).place(x=180,y=150)
    root.mainloop()
    speak("Video Download successfully")
    os.startfile("C:\\Users\\KABIR\\Desktop\\My Video")
    speak("Here is your video")

def main_execution() :

    #checking charge automtclly if low then warning
    battery = psutil.sensors_battery()
    prcntg = battery.percent
    if prcntg<=20 :
                speak(f"warning...please charge your device. The current battery percentage is {prcntg}")        
    
    while True :

        query = takeCommand()


        if 'hello' in query:
            speak('Hello Anushka , i am your personal assisstant!...how may i help you?')

        elif 'how are you' in query:
            speak('I am fine maam!')

        elif 'stop' in query :
            speak("Thank you maam. have a nice day")
            break

        elif 'the time' in query:
            strt = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {strt}")

        elif 'youtube search' in query:
            speak("ok maam , this is what i found for your search")
            query=query.replace('dexter','')
            query=query.replace('youtube search','')
            web ="https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            speak("done maam") 

        elif 'google search' in query :
            speak("ok maam , this is what i found for your search")
            query=query.replace('dexter','')
            query=query.replace('google search','')
            pywhatkit.search(query)
            speak("done maam")

            try:
                wik=wikipedia.summary(query,5)
                speak(wik) #speaking

            except:
                pass

        elif 'website' in query :
            speak("ok maam , opening the website..")
            query=query.replace('dexter','')
            query=query.replace('website','')
            query=query.replace(' ','')
            web1 = query.replace('open','')
            web2= 'https://www.' + web1+ '.com'   #website open format
            webbrowser.open(web2)
            speak("done maam")

        elif 'play music' in query:
            music()

        elif 'wikipedia' in query :
            wiki(query)

        elif 'send' in query :
            sending_msg(query)

        elif 'add contact' in query :
            speak("write the name maam :")
            name=input('name :')
            speak("Write the number maam")
            no=input("Write number :")
            f1=open('contact_name.txt',mode='a')
    
            name=','+name
            no=','+no
            f1.write(name)
            f2=open('mobile_number.txt',mode='a')
            f2.write(no)
            f1.close()
            f2.close()
            speak("Contact add sucessfully")


        elif 'nick name' in query :
            nick_name()

        elif 'take screenshot' in query :
            speak("ok, what should i name that file")
            nm = takeCommand()
            path_name = nm + ".png"
            path="C:\\Users\\PC\\Desktop\\screenshots\\" + path_name
            ss= pyautogui.screenshot()
            ss.save(path)
            os.startfile(path) #open file
            speak("here is your screnshot")

        elif 'open' in query : #app opening
            speak("ok ma'am")
            apps_open(query)

         #app closing
        elif 'close' in query:
            speak('ok maam closing the app')
            close_app(query)
            

        elif 'youtube automation' in query:
            youtube_auto()

        #utube automation
        elif 'play video' in query:
            keyboard.press('space bar') 
        elif 'puase video' in query:
            keyboard.press('space bar') 
        elif 'restart video' in query:
            keyboard.press('0')
        elif 'skip video' in query:
            keyboard.press('l')
        elif 'back video' in query:
            keyboard.press('j')
        elif 'out of full screen' in query:
            keyboard.press('f')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'out of film mode' in query:
            keyboard.press('t')
        elif 'film mode video' in query:
            keyboard.press('t')
        elif 'unmute video' in query:
            keyboard.press('m')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'start the video' in query:
            keyboard.press('k')
        elif 'half screen video' in query:
            keyboard.press('f')
        elif 'next video' in query:
            keyboard.press('SHIFT+n')
        elif 'previous video' in query:
            keyboard.press('SHIFT+p')
        elif 'decrease playback rate' in query:
            keyboard.press('SHIFT+,')
        elif 'increase playback rate' in query:
            keyboard.press('SHIFT+.')


        #chrome automation
        elif 'chrome automation' in query :
            chrome_auto()

        elif 'close this tab' in query:
            keyboard.press_and_release('Ctrl + w')
        elif 'close the tab' in query:
            keyboard.press_and_release('Ctrl + w')
        elif 'close this window' in query:
            keyboard.press_and_release('Alt + F4')
        elif 'close the window' in query:
            keyboard.press_and_release('Alt + F4')
        elif 'close window' in query:
            keyboard.press_and_release('Alt + F4')
        elif 'new tab' in query:
            keyboard.press_and_release('Ctrl + t')
        elif 'new window' in query:
            keyboard.press_and_release('Ctrl + t')
        elif 'menu' in query:
            keyboard.press_and_release('Alt+F')
        elif 'incognito mode' in query:
            keyboard.press_and_release('Ctrl + Shift + n')
        elif 'next tab' in query:
            keyboard.press_and_release('Ctrl + PgDn')
        elif 'previous tab' in query:
            keyboard.press_and_release('Ctrl + PgUp')
        elif 'go to tab 1' in query:
            keyboard.press_and_release('Ctrl + 1')           
        elif 'rightmost tab' in query:
            keyboard.press_and_release('Ctrl + 9')
        elif 'minimize window' in query:
            keyboard.press_and_release('Alt + Space +n')
        elif 'maximize window' in query:
            keyboard.press_and_release('Alt + Space +x')
        elif 'print the page' in query:
            keyboard.press_and_release('Ctrl + p')
        elif 'reload the current page' in query:
            keyboard.press_and_release('F5')
        elif 'chrome history' in query:
            keyboard.press_and_release('Ctrl + h')
        elif 'top of the page' in query:
            keyboard.press_and_release('Home')
        elif'bottom of the page' in query:
            keyboard.press_and_release('End')
        elif 'show bookmark' in query:
            keyboard.press_and_release('Ctrl + Shift + o')
        elif 'open file' in query:
            keyboard.press_and_release('Ctrl + 0')


        #jokes
        elif 'jokes' in query :
            joke_speak()

        #repeat words
        elif 'repeat my words' in query :
            rept_words()

        elif 'my location' in query:
            speak("okay maam wait a second")
            webbrowser.open("https://www.google.com/maps/@22.4794134,88.3618911,21z")

        elif 'my address' in query:
            speak('your present address is 8/33 B, netaji nagar, Kolkata-92')


        elif 'dictionary' in query:
            dict()

        
        elif 'alarm' in query:
            speak("Enter the time")
            time= input()

            while True:
                alrm= datetime.datetime.now()
                now= alrm.strftime("%H:%M:%S")

                if now==time:
                    speak("Time to wake up!")
                    playsound('audio.mp3')
                    speak("alarm closed")

                elif now>time:
                    break

        elif 'translator' in query :
            #trans()
            my_trans()

        #reminder
        elif 'remember that' in query :
            remb = query.replace("remember that","")
            speak("you told me to remember that : "+remb)

            remember = open('data.txt','w')   #creating new file whch stores what is to be remembered
            remember.write(remb)
            remember.close()

        elif 'what did i say you to remember' in query :
            remember = open('data.txt','r')
            speak("you told me to remember that"+remember.read())
            remember.close()


        elif 'temperature' in query :
            temp(query)

        elif 'weather report' in query :
            temp(query)

        elif 'audiobook' in query:
            audiobook()


        #checking internet soeed
        elif "internet speed" in query :
            intrnt_speed_test(query)

        elif "downloading speed" in query :
            intrnt_speed_test(query)

        elif "uploading speed" in query :
            intrnt_speed_test(query)

        #to ask anything to dextor
        elif 'how to' in query :
            speak("Getting the information from internet")
            op = query.replace("dexter","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)

            assert len(how_to_func) ==1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

        #check battery %
        elif "battery" in query or "how much power left" in query or "charge" in query :
            battery = psutil.sensors_battery()
            prcntg = battery.percent
            speak(f"Maam your system has {prcntg} percentage battery")

            if prcntg<=20 :
                speak("warning...please charge your device")

        elif 'open camera' in query :
            cap = cv2.VideoCapture(0)      # 0 for using internal camera
            while True :
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k= cv2.waitKey(50)
                if k==27 :
                    break
                cap.release()
                cv2.destroyAllWindows()


        elif 'email' in query :
            email()

        

main_execution()
