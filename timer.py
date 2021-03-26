from tkinter import*
import time
from pynotifier import Notification

m = Tk()
m.geometry('100x100')
def Timer (t , desc):
    while t :
        mins , secs = divmod(t,60)
        timer = print('{:02d}:{:02d}'.format(mins , secs))
        print(timer, end='\r')
        time.sleep(1)
        t-=1
        time1.configure(text = timer)
    Notification(title='TIMER RAN OUT !!!', description=desc, duration=5 , urgency='critical').send()

def timm ():
    pass
t = input('how much time to countdown by seconds \n: ')
desc = input('what is the description of the notification \n: ')
Timer(int(t) , str(desc))
label = Label(m , text = ' enter the time to countdown' , justify = 'left').grid(column = 0 , row = 0)
inputt = Entry(m , text = "").grid(row = 0 , column = 1 , width = 100).grid(column = 1 , row = 0)
button = Button(m , text = 'start timer').grid(row = 2 , column = 1).grid(row = 3 , column = 2)
time1 = Label(m , text = Timer(t , desc), font = "Helvetica").grid(row = 2 , column = 2)
m.mainloop()
##still not working