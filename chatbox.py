from tkinter import *
import sys
root = Tk()
def send():
    send = "You => "+e.get()
    txt.insert(END, "\n"+ send)
    if (e.get()=="hello"):
        txt.insert(END,"\n"+"Bot => Hi")
    elif (e.get()=="hi"):
        txt.insert(END,"\n"+"Bot => Hello")
    elif (e.get()=="how are you"):
        txt.insert(END,"\n"+ "Bot => Fine and you")
    elif (e.get()=="fine"):
        txt.insert(END,"\n"+"Bot => Nice to Hear")
    else:
        txt.insert(END,"\n"+"Bot => Sorry I didn't get it")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root, text="Send",command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title("CHATBOX")
root.mainloop()
