#실습2
from tkinter import *
from tkinter import messagebox
# 함수정의
def login():
    if pw.get()=='sejong':
        messagebox.showinfo('success','로그인 성공')
    else:
        messagebox.showinfo('fail','로그인 실패')
# 메인코드
w=Tk()
w.title('Welcome to sejong') #윈도우 제목
label1=Label(w,text='패스워드')
pw=Entry(w,show='*')
btn1=Button(w,text='확인',command=login)
btn2=Button(w,text='종료',command=quit)

# 위젯배치
label1.pack()
pw.pack()
btn1.pack()
btn2.pack()

w.geometry('300x200')
