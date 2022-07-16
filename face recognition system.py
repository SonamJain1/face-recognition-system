import cv2
import numpy as np

import time
from face import*

from tkinter import*
import tkinter 
from tkinter import messagebox
from tkinter.ttk import*


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os.path
from gmail import*

import pyttsx3

from small import tempp

from os import listdir
from os.path import isfile, join

data_path = 'C:/Users/Hirdesh Jain/Desktop/jarvis/faces/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]

Training_Data, Labels = [], []

for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels, dtype=np.int32)


model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Training_Data), np.asarray(Labels))

print("Model Training Complete!!!!!")


root=tkinter.Tk()

def password(event):
    x=(e.get())
    y = "hir123"
    if x==y:
        messagebox.showinfo('password is ','correct')
        speak('welcome sir')
        e.delete(0,END)
        root.destroy()
        return  
    elif x!=y:
        messagebox.showinfo('password is wrong ',str(x))
        if count>2:
            cv2.imwrite("F:/opencv/new.jpg",frame)
            maill()
            print('yes')
        root.destroy()  
root.bind('<Return>',password)


def cancle():
    x=e.get()
    e.delete(0,END)

bullet = "\u2022"


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices)

#voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"   # female voice 
engine.setProperty('voice',voices[0].id)
#engine.setProperty('voice',voices[1].id) # for femail voice
#engine.say('i m back for u sir ')
#engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak('good morning sir')

face_classifier = cv2.CascadeClassifier('C:/Users/Hirdesh Jain/Desktop/jarvis/haarcascade_frontalface_default.xml')

def face_detector(img, size = 0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return img,[]

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200,200))

    return img,roi

cap = cv2.VideoCapture(0)
result = True

if __name__ == '__main__':
    
    count =0
    while True:

        ret, frame = cap.read()

        image, face = face_detector(frame)
        
        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            result = model.predict(face)

            if result[1] < 500:
                confidence = int(100*(1-(result[1])/300))
                display_string = str(confidence)+'% Confidence it is user'
            cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)


            if confidence > 80:
                cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

                cv2.imshow('Face Cropper', image)
                count+=1
                if count == 2:
                    speak('welcomr sir')
                    break

            elif confidence < 75:
                
                cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('Face Cropper', image)
                
                count+=1
                if count>2:
                    #speak('''you are not my boss. I got order from my boss. so i will give you only one chance for fill the password.
                     #if you enter wright password then you can access me. if you fill wrong passwod. then i will shoutdown''')
                    speak('you have only one chance')
                    l=Label(root,text='password',relief=SUNKEN)
                    l.place(x=100,y=10)

                    e=Entry(root,show=bullet,width=20)
                    e.place(x=200,y=10)


                    b1=tkinter.Button(root,text='Save',width=5,height=1,bg='white',fg='blue',command=password)
                    b1.place(x=130,y=40)

                    b2=tkinter.Button(root,text='cancle',width=5,height=1,bg='white',fg='blue',command=cancle)
                    b2.place(x=230,y=40)

                    window_width = 800 
                    window_height =800 

                    position_right = int(root.winfo_screenwidth()/2 - window_width/3)
                    position_down = int(root.winfo_screenheight()/2 - window_height/15)

                    root.geometry("+{}+{}".format(position_right,position_down))

                    root.geometry('500x80')
                    root.mainloop()
                    break
   
                print('ok')


        except:
            cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow('Face Cropper', image)
            pass

        if cv2.waitKey(1)==13 or count>2:
            maill()
            time.sleep(2)
            break
    cap.release()
    cv2.destroyAllWindows()
    
