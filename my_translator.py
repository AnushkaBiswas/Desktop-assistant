import pyttsx3
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
from playsound import playsound

var_diff=0 #for creating diff file name at a run time
assistant=pyttsx3.init("sapi5") #creation object for speak
voices=assistant.getProperty('voices') #check voices

assistant.setProperty('voice', voices[0].id) # 1 for female 0 for male
assistant.setProperty('rate',170)
def speaking(audio):
    assistant.say(audio) #say() method to speak 
    print("")
    assistant.runAndWait() #to run the speech we use runAndWait() All the say() texts won’t be said unless the interpreter encounters runAndWait().
    print("")

#normal english speaking
def command():  #Create command function
 
    #recognizer
    command=sr.Recognizer()

    #recognize from micrphone
    with sr.Microphone() as source:
        print("Listening.....!")

        command.pause_threshold=1 #Represents the minimum length of silence (in seconds) that will register as the end of a phrase. Can be changed
        command.energy_threshold=9000
        
        audio=command.listen(source) 

        try:
            print("Recognizing....!")
            ## recognize speech using goggle
            query=command.recognize_google(audio,language='en-in')
            print("You said =", query)

        except Exception as Error:
            return "None"

        return query.lower()

#for taking any langues command and function take argument of lang
def lang_Command(lang):
    command=sr.Recognizer()

    #recognize from micrphone
    with sr.Microphone() as source:
        print("Listening.....!")

        command.pause_threshold=1 #Represents the minimum length of silence (in seconds) that will register as the end of a phrase. Can be changed
        command.energy_threshold=9000

        audio=command.listen(source) 

        try:
            print("Recognizing....!")

            #we can add more languages inn this dict
            dict_lang={'marathi':'mr','bihari':'bh','italian':'it','korean':'ko','swedish':'sw','malayalam':'ml','latin':'la','urdu':'ur','armenian':'hy','english':'en','hindi':'hi','bengali':'bn','arabic':'ar','tamli':'ta','spanish':'es','french':'fr','chinese':'zh-cn'}
            ## recognize speech using goggle
            lang=dict_lang[lang] #give lang short form

            query=command.recognize_google(audio,language=lang)  
            print("You said =",query)

        except Exception as Error:
            return "None"

        return query.lower()

#for convert one to another  and take text, source lang and destination lang
def convert(text,s,lang):
    #we can add more languages inn this dict
    dict_lang={'marathi':'mr','bihari':'bh','italian':'it','korean':'ko','swedish':'sw','malayalam':'ml','latin':'la','urdu':'ur','armenian':'hy','english':'en','hindi':'hi','bengali':'bn','arabic':'ar','tamli':'ta','spanish':'es','french':'fr','chinese':'zh-cn'}
    if lang in dict_lang: #if lang found in dict
        transl=Translator()
        language=dict_lang[lang]
        s=dict_lang[s]
        textlang=transl.translate(text,src=s,dest=language).text #for convert
        textm=textlang
        speech=gTTS(text=textm) #gtts for specific languages pronounce
        global var_diff #globar var for make diff file name
        var_lang=var_diff+1
        # print(type(speech))
        
        file='trans'+str(var_lang)+'.mp3' #file name
        # kabir_lang=kabir_lang+1
        var_diff+=1
        try:
            #play translator
              speech.save(file)
              playsound(file)
            
        except:
               speaking("Language not found")
    # else:
    #     speaking("Language not found")


#here to start
def my_trans():
    speaking("Translator on")
    while True:
        #take which language user want to speak :source language
       speaking("which language you want to talk")
       lang=command()
       lang=lang.replace("dexter",'')
       word='ok maam.. tell the line'
       speaking(word)
    
       take_text=lang_Command(lang) #take line

       #choice convert language : destinationa lang
       choice_lang='maam..which language you want to translate'
       speaking(choice_lang)
       ch_lang=command()
       convert(take_text,lang,ch_lang) #convert another language
       speaking("Translation done..")

#if user want to more language for transkate
       speaking("do you want to translate more sentencese")
       word=command()
       li_stop=['stop','no', 'no more','end','no thank you','no thanks','off','close']
       i=0
       f=0
       while(i<len(li_stop)):
            if li_stop[i] in word:
                f=1
                break
            i=i+1
       if(f==1):
           speaking("Ok maam...translator closed sucessfully")
           break
