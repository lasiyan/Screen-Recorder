from tkinter import *
import threading
import time
import keyboard

import define
import func as Func

# Keyboard event
def SetFunc(event):

    global coordinate
    
    if keyboard.is_pressed(define.DEF_KEY_REC_START):
        threading.Thread(target=Func.StartRecord(root, coordinate, False), daemon=True).start()

    if keyboard.is_pressed(define.DEF_KEY_REC_START_UI):    #debugging
        threading.Thread(target=Func.StartRecord(root, coordinate, True), daemon=True).start()

    if keyboard.is_pressed(define.DEF_KEY_SCREN_CAP):
        threading.Thread(target=Func.Capture(root, coordinate), daemon=True).start()

    return

# Dialog re-size event
def SetSize(event):

    time.sleep(0.001)

    global coordinate
    coordinate = list()
    
    width = root.winfo_width()
    height = root.winfo_height()
    
    coordinate.append(root.winfo_rootx())   # x cord.
    coordinate.append(root.winfo_rooty())   # y cord.
    coordinate.append(coordinate[0] + width)
    coordinate.append(coordinate[1] + height)

    Title = define.DEF_TITLE + ' ' + str(width) + ' x ' \
         + str(height) + ' ' + str(coordinate[0]) + ' x ' + str(coordinate[1])

    root.title(Title)
    
    time.sleep(0.01)


root = Tk()

root.title(define.DEF_TITLE)
root.attributes('-alpha', 0.8)
root.attributes("-topmost", 1)
root.geometry("320x240+100+100" )

root.bind("<Key>", SetFunc)
root.bind("<Configure>", SetSize)

Msg1 = Label(root, text="1. Record Start: %s" % define.DEF_KEY_REC_START, anchor=CENTER, font='console 20 bold')
Msg1.pack(padx = 5, pady = 8)
Msg1 = Label(root, text="2. Record Stop: %s" % define.DEF_KEY_REC_STOP, anchor=CENTER, font='console 20 bold')
Msg1.pack(padx = 5, pady = 8)
Msg1 = Label(root, text="3. ScreenShot: %s" % define.DEF_KEY_SCREN_CAP, anchor=CENTER, font='console 20 bold')
Msg1.pack(padx = 5, pady = 8)

SetSize(None)

root.attributes('-toolwindow', 'True')

root.mainloop()
