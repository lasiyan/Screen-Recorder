from PIL import ImageGrab
import time
import keyboard
import cv2
import numpy as np

import define

bRecord = False
output = None


def GetFileName():
    now = time.localtime()
    title = "%04d-%02d-%02d_%02dh%02dm%02ds" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    return title

def GetFramerate(roi=[]): # Calc frame-rate from 10 frame's avg time (first frame was dropped)
    sum = 0.0
    for i in range(11):
        last_time = time.time()
        frame = cv2.cvtColor(np.array(ImageGrab.grab(roi)), cv2.COLOR_BGR2RGB)
        cv2.waitKey(1)
        if not i == 0:  # drop first frame 
            sum += (1 / (time.time()-last_time))
        print('cal fps: {0}'.format(1 / (time.time()-last_time)))

    frame_rate = sum / 10
    print('Set Frame rate: %f' % frame_rate)

    return frame_rate

def Capture(root, roi=[]):
    global bRecord

    if bRecord:
        return

    # Hide dialog(tkinter) UI
    root.attributes('-alpha', 0.0)

    img = ImageGrab.grab(roi)
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    cv2.imwrite('Screen_%s.png' % GetFileName(), frame)

    # re-show
    root.attributes('-alpha', 0.8)

    return

def StartRecord(root, roi, debug):

    global isRecord, output

    root.attributes('-alpha', 0.0)

    width = roi[2] - roi[0]
    height = roi[3] - roi[1]
    codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    frame_rate = GetFramerate(roi)

    output = cv2.VideoWriter('outputput_%s.mp4' % GetFileName(), codec, frame_rate, (width, height))

    cnt = 1
    while output.isOpened():
        img = ImageGrab.grab(roi)
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if debug :
            cv2.imshow('Preview', frame)  # Display the picture

        output.write(frame)

        key = cv2.waitKey(1)

        bRecord = True

        print("recording%s" % ("." * (cnt % 10)))
        cnt+=1

        if keyboard.is_pressed(define.DEF_KEY_REC_STOP):
            StopRecord(root)
            break

    return

def StopRecord(root):
    global output

    cv2.destroyAllWindows()
    output.release()
    root.attributes('-alpha', 0.8)
    bRecord = False

    return
