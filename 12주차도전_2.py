from tkinter import *
from tkinter.messagebox import *

def login():
    if sid.get()=='sejong':
        if spw.get()=='1234':
            showinfo('success', '로그인 성공')
        else:
            showinfo('fail', '패스워드 오류')
    else:
        showinfo('fail', '회원가입!!')

#메인코드
w=Tk()
w.title('Welcome to Sejong!!')
logo=Label(w, text='세사대-온라인 강의실', fg='green', font=('Times', '25'))
sid=Entry(w) #id
spw=Entry(w, show='♡') #pw
btn1=Button(w, text='LOGIN', fg='white', bg='green', command=login)


logo.pack()
sid.pack()
spw.pack()
btn1.pack()
w.geometry('400x300')
