# -*- coding: utf-8 -*-
from tkinter import *

root=Tk()
root.title("ASCII")

root.geometry("400x400")
root.configure(background = 'snow')

enter_word= Entry(root)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label=Label(root, text="name in Ascii :", bg="light yellow", fg="black")
label1=Label(root, text="encrypted text :", bg="red", fg="black")
def asciiConverter():
    label["text"]=""
    label1["text"]=""
    input_word = enter_word.get()
    for letter in input_word :
        label["text"] += str(ord(letter))+ " "
        ascii=int(ord(letter))
        encrypted=ascii-5
        label1["text"] += str(chr(encrypted))
        
btn=Button(root,text="show name in ascii", command=asciiConverter, bg="gold", fg="black")
btn.place(relx=0.5, rely=0.5,  anchor=CENTER)

label.place(relx=0.5, rely=0.6, anchor=CENTER)

label1.place(relx=0.5, rely=0.7, anchor=CENTER)


root.mainloop()


