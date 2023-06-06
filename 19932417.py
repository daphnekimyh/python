from tkinter import *
from tkinter.messagebox import *

def plus():
    first=int(num1.get())
    second=int(num2.get())
    num3.delete(0,END)
    num3.insert(0,first+second)
    
w=Tk()
w.title('더하기 계산기')

Label1=Label(w,text='첫번째 숫자')
Label4=Label(w,text='+')
Label2=Label(w,text='두번째 숫자')
Label3=Label(w,text='정답')
btn1=Button(text='=',command=plus)
btn2=Button(w,text='종료',command=quit)

num1=Entry(w)
num2=Entry(w)
num3=Entry(w)

Label1.pack()
num1.pack()
Label4.pack()
Label2.pack()
num2.pack()
btn1.pack()
Label3.pack()
num3.pack()
btn2.pack()

w.geometry('280x210')
