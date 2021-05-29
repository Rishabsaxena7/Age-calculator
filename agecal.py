import tkinter
from tkinter import *
from datetime import date
#create window
win=Tk()
win.geometry("1000x600")
win.resizable(False,False)
win.title('Age Calculator')
#add image
img=PhotoImage(file="age.png")
a=Label(image=img)
a.pack(padx=80,pady=80)
#define function to calculate age
def cal():
    today=date.today()
    birthDate=date(int(year.get()),int(month.get()),int(day.get()))
    age=today.year -birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
    Label(text=f"{a.get()} your age is {age}",font=40,fg="black").place(x=300,y=550)
#create labels
Label(text="Name",font=23).place(x=200,y=250)
Label(text="Year",font=23).place(x=200,y=300)
Label(text="Month",font=23).place(x=200,y=350)
Label(text="Day",font=23).place(x=200,y=400)
#create entrys
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
nameEntry=Entry(win,textvariable=a,width=30,bd=3,font=20)
nameEntry.place(x=300,y=250)
year=Entry(win,textvariable=b,width=30,bd=3,font=20)
year.place(x=300,y=300)
month=Entry(win,textvariable=c,width=30,bd=3,font=20)
month.place(x=300,y=350)
day=Entry(win,textvariable=d,width=30,bd=3,font=20)
day.place(x=300,y=400)
#create button
button=Button(win,text="Calculate Age",font=20,bg="black",fg="white",width=11,height=2,command=cal)
button.place(x=300,y=450)
win.mainloop()