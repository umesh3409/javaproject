import os
os.system('cls')

# =///////////////////////
import tkinter
home=tkinter.Tk()
home.title('umesh')
home.minsize(400,500)
home.maxsize(400,500)
screen='0'
scr=tkinter.Label(home,text=screen,bg='black',fg='white',width=14,font=('bold',25),padx=13.5,pady=5)
scr.place(x=45,y=19)
def btn_7():
    global screen
    if screen=='0':
        screen='7'
    else:
        screen+='7'
    scr.config(text=screen) 
def btn_8():
    global screen
    if screen=='0':
        screen='8'
    else:
        screen+='8'
    scr.config(text=screen)
def btn_9():
    global screen
    if screen=='0':
        screen='9'
    else:
        screen+='9'
    scr.config(text=screen)           
def btn_4():
    global screen
    if screen=='0':
        screen='4'
    else:
        screen+='4'
    scr.config(text=screen)
def btn_5():
    global screen
    if screen=='0':
        screen='5'
    else:
        screen+='5'
    scr.config(text=screen)
def btn_6():
    global screen
    if screen=='0':
        screen='6'
    else:
        screen+='6'
    scr.config(text=screen)
def btn_1():
    global screen
    if screen=='0':
        screen='1'
    else:
        screen+='1'
    scr.config(text=screen)
def btn_2():
    global screen
    if screen=='0':
        screen='2'
    else:
        screen+='2'
    scr.config(text=screen)
def btn_3():
    global screen
    if screen=='0':
        screen='3'
    else:
        screen+='3'
    scr.config(text=screen)
def btn_0():
    global screen
    if screen=='0':
        screen='0'
    else:
        screen+='0'
    scr.config(text=screen)
def btn_D():
    global screen
    screen!='0'
    screen+='/'
    scr.config(text=screen)
def btn_M():
    global screen
    if screen!='0':
        screen+='*'
    scr.config(text=screen)
def btn_S():
    global screen
    if screen!='0':
     screen+='-'
    scr.config(text=screen)
def btn_A():
    global screen
    if screen!='0':
        screen+='+'
    scr.config(text=screen)    
def btn_DOT():
    global screen
    if screen!='0':
        screen+='.'
    scr.config(text=screen)
def btn_E():
    global screen
    screen=str(eval(screen))
    if screen!='0':
     scr.config(text=screen)
def btn_C():
    global screen
    screen='0'
    scr.config(text=screen)
def btn_BACK():
    global screen
    if len(screen)==1:
        screen='0'
    else:
        screen=screen[:-1]    
    scr.config(text=screen)

btnC=tkinter.Button(home,bg='red',command = btn_C,text='C',font=('bold',25),padx=12,pady=5)
btnC.place(x=45,y=75)
btnBACK=tkinter.Button(home,bg ='blue',command = btn_BACK,text='BACK',font=('bold',25),padx=16.5,pady=5)
btnBACK.place(x=120,y=75)
btnD=tkinter.Button(home,bg='#aebd24',command=btn_D,text='/',font=('bold',25),padx=17.5,pady=5)
btnD.place(x=271,y=75)
btn7=tkinter.Button(home,bg='pink',command=btn_7,text='7',font=('bold',25),padx=15,pady=5)
btn7.place(x=45,y=150)
btn8=tkinter.Button(home,bg='pink',command=btn_8,text='8',font=('bold',25),padx=15,pady=5)
btn8.place(x=120,y=150)
btn9=tkinter.Button(home,bg='pink',command=btn_9,text='9',font=('bold',25),padx=15,pady=5)
btn9.place(x=195,y=150)
btnM=tkinter.Button(home,bg='#aebd24',command=btn_M,text='* ',font=('bold',25),padx=12,pady=5)
btnM.place(x=270,y=150)
btn4=tkinter.Button(home,bg='pink',command=btn_4,text='4',font=('bold',25),padx=15,pady=5)
btn4.place(x=45,y=225)
btn5=tkinter.Button(home,bg='pink',command=btn_5,text='5',font=('bold',25),padx=15,pady=5)
btn5.place(x=120,y=225)
btn6=tkinter.Button(home,bg='pink',command=btn_7,text='6',font=('bold',25),padx=15,pady=5)
btn6.place(x=195,y=225)
btnS=tkinter.Button(home,bg='#aebd24',command=btn_S,text='- ',font=('bold',25),padx=13,pady=5)
btnS.place(x=270,y=225)
btn1=tkinter.Button(home,bg='pink',command=btn_1,text='1',font=('bold',25),padx=15,pady=5)
btn1.place(x=45,y=300)
btn2=tkinter.Button(home,bg='pink',command=btn_2,text='2',font=('bold',25),padx=15,pady=5)
btn2.place(x=120,y=300)
btn3=tkinter.Button(home,bg='pink',command=btn_3,text='3',font=('bold',25),padx=15,pady=5)
btn3.place(x=195,y=300)
btnA=tkinter.Button(home,bg='#aebd24',command=btn_A,text='+',font=('bold',25),padx=13.5,pady=5)
btnA.place(x=270,y=300)
btn0=tkinter.Button(home,bg ='pink',command=btn_0,text='0',font=('bold',25),padx=15,pady=5)
btn0.place(x=45,y=375)
btnDOT=tkinter.Button(home,bg = '#c45050',command=btn_DOT,text='. ',font=('bold',25),padx=15,pady=5)
btnDOT.place(x=120,y=375)
btnE=tkinter.Button(home,bg='green',command=btn_E,text='=',font=('bold',25),padx=52,pady=5)
btnE.place(x=195,y=375)

home.mainloop()