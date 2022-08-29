import os, sys
from datetime import date
print("this is a terminal in python for basic commands")
while True:
    cmd = input("$ ")
    if cmd == "cmd":
        os.system("cmd /c cmd.exe") 
    elif cmd == "time":
        today = str(date.today())
        print(today)
    elif cmd == "exec":
        print("make sure you are in the directory of the file\nif you are then put in the file name(with extension)")
        file_name = input()
        os.system(file_name)