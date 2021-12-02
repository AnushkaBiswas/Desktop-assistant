import pyttsx3
import speech_recognition as sr
import pywhatkit
import keyboard
import webbrowser
import time


assistant=pyttsx3.init("sapi5") #creation object for speak
voices=assistant.getProperty('voices') #check voices

assistant.setProperty('voice', voices[0].id) # 1 for female 0 for male
assistant.setProperty('rate',170)
def speaking(audio):
    assistant.say(audio) #say() method to speak 
    print(audio)
    assistant.runAndWait() #to run the speech we use runAndWait() All the say() texts won’t be said unless the interpreter encounters runAndWait().
    print("")

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
            print("You said =",query)

        except Exception as Error:
            return "None"

        return query.lower()


def seraching(data,namePerson):
        i=0
        while(i<len(data)):
            if (namePerson==data[i]):
                return i
            i=i+1
        return -1 #if not found


def sending_msg(query):

    if "whatsapp" in query:
        speaking("maam..tell me the name....")
        namePerson=command() #take name

        if 'main study' in namePerson:   #wp group
            speaking("Tell me the message ...!")#take whatsapp massage
            #take timing for the massage
            msg=command()
            path='https://web.whatsapp.com/accept?code=DxnuLnqj8e62d2x921jzKx'

            webbrowser.open(path)
            time.sleep(20)
            keyboard.write(msg)
            time.sleep(1)
            #keyboard.press('enter')
            speaking("ok,sir,sending whatsapp massage")

        elif 'unknown' in namePerson: #for unknown
            speaking("write the number maam..!")
            no=input("Enter number:") #take number
            no="+91"+no #+91 for india
            speaking("Tell me the message ...!")
            msg=command() #take whatsapp massage
            #take timing for the massage
            speaking("write the time")
            speaking("Time in hour")
            hr=int(input("Write : "))
            speaking("Time in minutes")
            mn=int(input("Write : "))
            pywhatkit.sendwhatmsg(no,msg,hr,mn,20) #send whatsapp massage
            keyboard.press("enter")
          
            speaking("ok,maam,,sending whatsapp massage")


        else :  # known contact
            #Open file of contact name
            f=open("contact_name.txt")
            data=f.read() #get all the contact
            data=data.split(',') #convert into list
            f.close()


            idx=seraching(data,namePerson) #calling search
            if(idx!=-1): #contact is found
                #open mobile number file
                f=open("mobile_number.txt")
                number=f.read()#get all the number
                number=number.split(",") #convert into list
                no=number[idx] #get exactly number
                no="+91"+no
                speaking("Tell me the message ...!")#take whatsapp massage
                #take timing for the massage
                msg=command()
                speaking("write the time")
                speaking("Time in hour")
                hr=int(input("Write : "))
                speaking("Time in minutes")
                mn=int(input("Write : "))
                pywhatkit.sendwhatmsg(no,msg,hr,mn,20) #send the massage
                speaking("ok,maam,sending whatsapp message")
                #keyboard.press("enter")
                


            else:   #adding contact
                speaking("maam the name is not found")
                speaking("maam..do you want to add the name in the contact...!")
                choice=command() #if gives for add contact
                if 'no' in choice:
                    speaking("Ok maam fine")

                else:  #yes..adds contact
                    speaking("write the name maam :")
                    name=input('name :')
                    speaking("Write the number maam")
                    no=input("Write number :")
                    f1=open('contact_name.txt',mode='a')
    
                    name=','+name
                    no=','+no
                    f1.write(name)
                    f2=open('mobile_number.txt',mode='a')
                    f2.write(no)
                    f1.close()
                    f2.close()
                    speaking("Contact add sucessfully")

