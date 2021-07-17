import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    '''
    It Speaks the given 
    text stored in 'audio'
    '''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''
    It Wish me According to the time.
    '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Very Good Morning to You")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hello!! How may I help you?")
def takeCommand():
    '''
    It takes microphone input from the user 
    and returns string output
    '''

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")

        query=r.recognize_google(audio,language='en-in')
        print(f"You just said: '{query}\n'")
    
    except Exception as e:
        print(e)
        print("Please Repeat Again")
        return "None"
    return query
def sendEmail(to,content):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('desaikavinaa1602@gmail.com','chase1602')
     server.sendmail('desaikavinaa1602@gmail.com',to,content)
     server.close()

if __name__=="__main__":
    speak("Hey Kavina")
    #wishMe()
    query=takeCommand().lower()


    #logic to excute tasks based on query
    if 'wikipedia' in query:
        speak("Searching wikipedia...")
        query = query.replace("wikipedia","")
        result=wikipedia.summary(query,sentences=1)
        print(result)
        speak("According to wikipedia")
        speak(result)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        webbrowser.open("google.com")
    
    elif 'open instagram' in query:
        webbrowser.open("instagram.com")

    elif 'play music' in query:
        music_dir="C:\\Users\\Kavina Desai\\Music"
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")  
        speak(f"The time is {strTime}")     
    elif 'movie' in query:
        vid_dir="C:\\Users\\Kavina Desai\\Desktop\\movies"
        vids=os.listdir(vid_dir)
        print(vids)
        os.startfile(os.path.join(vid_dir,vids[1])) 
    
    elif 'open vs code' in query:
        code_dir="C:\\Users\\Kavina Desai\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
        os.startfile(code_dir)
    
    elif 'send an email' in query:
        try:
            speak("What should I say")
            content=takeCommand()
            to="harryyouemail@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent")
        
        except Exception as e:
            print(e)
            speak("Sorry message not sent")
    
    elif 'bye' in query:
        speak("Thankyou for your time! bye")
        exit()
    
    elif 'send WhatsApp message' in query:
        # speak("To whom I should send")
        # number=takeCommand()
        speak("What shoul I say")
        message=takeCommand()
        pywhatkit.sendwhatmsg('+919904542999',message,19,45)
    