from tkinter import *
import tkinter.messagebox
w=Tk()
w.geometry('400x500') 
w.title("Registration form")
l1 =Label(w, text="REGISTRATION FORM",font=('Times New Roman', 20,'bold'))
l1.place(x=57,y=50)
nl= Label(w, text="Name :",width=20,font=('Times New Roman',15,))
nl.place(x=2, y=130)
ne = Entry(w)
ne.place(x=170, y=130)

el=Label(w, text="Email :",width=20,font=('Times New Roman',15))
el.place(x=2, y=180)
ee =Entry(w)
ee.place(x=170, y=180)

al=Label(w, text="Age :",width=20,font=('Times New Roman',15))
al.place(x=-6, y=230)
ae = Entry(w)
ae.place(x=170, y=230)

gl = Label(w, text="Gender :",width=20,font=('Times New Roman',14))
gl.place(x=10, y=280)
g =StringVar(value=None)
m= Radiobutton(w, text="Male", variable=g, value="Male",font=('Times New Roman',10))
m.place(x=165, y=280)
f = Radiobutton(w, text="Female", variable=g, value="Female",font=('Times New Roman',10))
f.place(x=230, y=280)


ml =Label(w, text="Mobile No.",width=20,font=('Times New Roman',13))
ml.place(x=28, y=330)
me =Entry(w)
me.place(x=170, y=330)

def submit():

    tkinter.messagebox.showinfo(title="success",message="Registration Successful!!",ANCHOR=CENTER)
    
b= Button(w,text='Submit form',width=20,bg='mediumPurple',fg='white',command=submit)
b.place(x=120,y=380)

w.mainloop()
