from tkinter import *
import re

win=Tk()

win.geometry("800x800")
win.title("WORD COUNTER")
win['bg']="pale turquoise"

no_of_words=0
no_of_chars=0

def key_release(b):
    global no_of_words
    global no_of_chars
    label5.config(text="")
    words=re.findall(r"[\S]+", text1.get(1.0,END))
    no_of_words=len(words)
    chars=len(text1.get(1.0,END))
    no_of_chars=str(chars-1)
    label4.config(text=no_of_chars)
    label3.config(text=str(no_of_words))

def submit():
    global no_of_words
    global no_of_chars
    label5.config(text=" There are " + str(no_of_chars) + " characters " + "and " + str(no_of_words) + " words. ")

def clear():
    global no_of_words
    global no_of_chars
    text1.delete(1.0,END)
    no_of_words=0
    no_of_chars=0
    label3.config(text=str(no_of_words))
    label4.config(text=str(no_of_chars))
    label5.config(text="")

def undo():
    global no_of_words
    global no_of_chars
    label5.config(text="")
    if int(no_of_chars)>0:
        data=text1.get(1.0,"end-2c")
        text1.delete(1.0,END)
        text1.insert(1.0,data)
        count=int(no_of_chars)-1
        if count>0:
            words=re.findall(r"[\S]+", text1.get(1.0,END))
            no_of_words=len(words)
            chars=len(text1.get(1.0,END))
            no_of_chars=str(chars-1)
            label4.config(text=str(no_of_chars))
            label3.config(text=str(no_of_words))
        elif count==0:
            no_of_chars=0
            no_of_words=0
            label4.config(text=str(no_of_chars))
            label3.config(text=str(no_of_words))

label1=Label(win, text="Total number of words:", font=("Arial", 15))
label1.place(x=5,y=10)
label1['bg']="pale turquoise"

label2=Label(win, text="Total number of characters:", font=("Arial", 15))
label2.place(x=970,y=10)
label2['bg']="pale turquoise"

label3=Label(win, text="0", font=("Arial", 15))
label3.place(x=220,y=10)
label3['bg']="pale turquoise"

label4=Label(win, text="0", font=("Arial", 15))
label4.place(x=1225,y=10)
label4['bg']="pale turquoise"

label5=Label(win, text="", font=("Arial", 20), fg="medium orchid")
label5.place(x=415,y=600)
label5['bg']="pale turquoise"

text1=Text(win, width=115, relief=RAISED, height=20, takefocus=0, font=("Arial", 15), fg="grey", wrap=WORD, spacing1=1)
text1.place(x=5,y=50)
text1['bg']="white smoke"

btn1=Button(win, text="SUBMIT", font=("Arial", 15), command=submit, fg="medium violet red")
btn1.place(x=300,y=540)

btn2=Button(win, text="CLEAR", font=("Arial", 15), command=clear, fg="medium violet red")
btn2.place(x=600,y=540)

btn3=Button(win, text="UNDO", font=("Arial", 15), command=undo, fg="medium violet red")
btn3.place(x=900,y=540)

text1.bind("<KeyRelease>", lambda a:key_release(a))

win.mainloop()