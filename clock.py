from datetime import datetime
import pytz
from tkinter import *
import time
 

root=Tk()
root.geometry("500x250")


def times():
    
    home=pytz.timezone('Asia/Kolkata')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    name.config(text="INDIA")
    clock.after(1000,times)

    home=pytz.timezone('Asia/Tokyo')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    clock1.config(text=current_time)
    name1.config(text="JAPAN")
    clock1.after(1000,times)

    home=pytz.timezone('US/Central')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    clock2.config(text=current_time)
    name2.config(text="TEXAS")
    clock2.after(1000,times)


name=Label(root,text ="INDIA",font=("times",20,"bold"))
name.place(x=80,y=5)
clock=Label(root,text ="ededed",font=("digital dream",20,))
clock.place(x=30,y=50)




name1=Label(root,text ="JAPAN",font=("times",20,"bold"))
name1.place(x=330,y=5)
clock1=Label(root,text ="ededed",font=("digital dream",20,))
clock1.place(x=280,y=50)



name2=Label(root,text ="TEXAS",font=("times",20,"bold"))
name2.place(x=180,y=120)
clock2=Label(root,text ="ededed",font=("digital dream",20))
clock2.place(x=140,y=165)



times()
root.mainloop()