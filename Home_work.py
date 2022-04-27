import os
import time
import tkinter.filedialog
import pyautogui
from tkinter import filedialog
from datetime import datetime

#function to print star program

def star(x):
    z=x-1
    #printing spaces using loop
    for i in range(0,x):
        for j in range(0,z):
            print(end=" ")
        z=z-1

        #printing star using loop
        for j in range(0,i+1):
            print("* ",end=" ")
        time.sleep(2)#it is a time duration between the loop to another loop

        a=pyautogui.screenshot()# it is used to takes screenshots automatically
        b=tkinter.filedialog.askdirectory()# it is used to create a dialog to ask user the location
        '''root=tkinter.Tk()
        root.withdraw()'''

        current_time =datetime.now().replace(microsecond=0)
        format="%y_%b_%d_%H_%M_%S"
        current_time=datetime.strftime(current_time, format)
        q="A"+current_time+".png"
        c=os.path.join(b,q)
        a.save(c)
        print("\r")

star(5)


