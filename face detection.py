import tkinter as tk
from tkinter import messagebox
from tkinter.constants import FALSE
import cv2
import os
from PIL import Image
import numpy as np
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
global detect
detect = 0
def register():
    x1,x2=10,140
    y1=100
    gap=50
    window=tk.Tk()
    window.title("Register Attendance")
    window.geometry("600x300")
    head=tk.Label(window,text="Register Attendance",font=("Sans Serif",30,"bold"))
    head.place(x=100,y=10)


    l1=tk.Label(window,text="Name:",font=("Sans Serif",20,"bold"))
    l1.place(x=x1,y=y1)
    t1=tk.Entry(window,width=50,bd=2)
    t1.place(x=x2,y=y1,height=25)

    l2=tk.Label(window,text="USN:",font=("Sans Serif",20,"bold"))
    l2.place(x=x1,y=y1+1*gap)
    t2=tk.Entry(window,width=50,bd=2)
    t2.place(x=x2,y=y1+1*gap,height=25)

    l3=tk.Label(window,text="Section:",font=("Sans Serif",20,"bold"))
    l3.place(x=x1,y=y1+2*gap)
    t3=tk.Entry(window,width=50,bd=2)
    t3.place(x=x2,y=y1+2*gap,height=25)

    def train_classifier():
        data_dir="C:/Users/peter/OneDrive/Desktop/mini project/data"
        path = [os.path.join(data_dir,f) for f in os.listdir(data_dir)]
        faces  = []
        ids   = []
        
        for image in path:
            img = Image.open(image).convert('L');
            imageNp= np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split(".")[1])
            
            faces.append(imageNp)
            ids.append(id)
        ids = np.array(ids)
        
        #Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        messagebox.showinfo('Result','Training dataset completed!!!')
        
    b1=tk.Button(window,text="Training",font=("Sans Seri",20),command=train_classifier)

    gapDown = 180

    def generate_dataset():
        if(t1.get()=="" or t2.get()=="" or t3.get()==""):
            messagebox.showinfo('Result','Please provide complete details of the user')
        else:
            mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root123",
            database="facedetection"
            )
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * from user")
            myresult=mycursor.fetchall()
            id=1
            for x in myresult:
                id+=1
            sql="insert into user(id,name,usn,section) values(%s,%s,%s,%s)"
            val=(id,t1.get(),t2.get(),t3.get())
            mycursor.execute(sql,val)
            mydb.commit()
            
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            def face_cropped(img):
                gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray,1.3,5)
                #scaling factor=1.3
                #Minimum neighbor = 5

                if faces == ():
                    return None
                for(x,y,w,h) in faces:
                    cropped_face=img[y:y+h,x:x+w]
                return cropped_face

            cap = cv2.VideoCapture(0)
            img_id=0

            while True:
                ret,frame = cap.read()
                if face_cropped(frame) is not None:
                    img_id+=1
                    face = cv2.resize(face_cropped(frame),(200,200))
                    face  = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1, (0,255,0),2)
                    # (50,50) is the origin point from where text is to be written
                    # font scale=1
                    #thickness=2

                    cv2.imshow("Cropped face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==150:
                        break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo('Result','Generating dataset completed!!!')

    b3=tk.Button(window,text="Register",font=("Sans Serif",20),command=generate_dataset)
    b3.place(x=10+gapDown,y=y1+3*gap-20)

    window.mainloop()


def attendance():
    global detect
    detect = 0

    y1=80
    gap=50
    x2 = 200
    x1=50
    global window
    window=tk.Tk()
    window.title("Attendance")
    window.geometry("500x300")

    head=tk.Label(window,text="Attendance Register ",font=("Sans Serif",30,"bold"))
    head.place(x=100,y=10)

    l4=tk.Label(window,text="Subject:",font=("Sans Serif",20,"bold"))
    l4.place(x=x1,y=y1+gap)

    t4 = StringVar()
    t4.set("20CSE71")
    t4box = ttk.Combobox(window, textvariable=t4,font=("Sans Serif",12))
    t4box['values'] = ('20CSE71', '20CSE72', '20CSE73', '20CSE74', '20CSE75')
    t4box.place(x=x2, y=y1 + gap, width=100,height=35)


            # DOB field
    l5=tk.Label(window,text="Date:",font=("Sans Serif",20,"bold"))
    l5.place(x=x1,y=y1+2*gap)

    cal = DateEntry(window, width=12, year=2022, month=1, day=18, borderwidth=2,font=("Sans Serif",12))
    cal.place(x=x2, y=y1 + 2 * gap, width=100,height=35)

    def reg_attendance():
        global detect
        detect+=1
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coords = []

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
                global id
                id,pred = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int(100*(1-pred/300))
                
                mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="root123",
                database="facedetection"
                )
                mycursor=mydb.cursor()
                details = []
                mycursor.execute("select name,usn,section from user where id="+str(id))
                details = mycursor.fetchone()
                if details is not None:
                    global name,usn,section,subject,date
                    name = details[0]
                    usn = details[1]
                    section  = details [2]
                    subject = t4.get()
                    date = cal.get_date()        
                    print(details)
                    global detect
                    detect+=1
                    if confidence>74:
                        cv2.putText(img,name,(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)   
                    else:
                        cv2.putText(img,"UNKNOWN",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),1,cv2.LINE_AA)



                coords=[x,y,w,h]
            return coords
                
        def recognize(img,clf,faceCascade):
            coords = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)

            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture =  cv2.VideoCapture(0)

        while True:
            ret,img = video_capture.read()
            img=  recognize(img,clf,faceCascade)
            cv2.imshow("face detection",img)

            if cv2.waitKey(1)==27 & 0xFF:
                break

            if detect>5:

                    sql="insert into attendance(id,name,usn,section,subject,date) values(%s,%s,%s,%s,%s,%s)"
                    val=(id,name,usn,section,subject,date)

                    mydb=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="root123",
                    database="facedetection"
                    )
                    mycursor=mydb.cursor()
                    mycursor.execute(sql,val)
                    mydb.commit()
                    video_capture.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Done","Attendance Marked")
        cv2.destroyAllWindows()

    b1=tk.Button(window,text="Mark Present",font=("Sans Serif",12),command=reg_attendance)
    b1.place(x=x2,y=y1+3*gap,height=30,width=100)

def homepage():
    y1=100
    gap=50
    x2=350
    x1=50
    window=tk.Tk()
    window.geometry("500x250")
    window.title("Face recognition system")
    head=tk.Label(window,text="Attendance System ",font=("Sans Serif",30,"bold"))
    head.place(x=100,y=10)

    b1=tk.Button(window,text="Take Attendace",font=("Sans Serif",20),command=attendance)
    b1.place(x=x1,y=y1+gap)
    b2=tk.Button(window,text="Register",font=("Sans Serif",20),command=register)
    b2.place(x=x2,y=y1+gap)


    window.mainloop()

homepage()