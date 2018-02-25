import os
from os import listdir
from os.path import isfile, join
import shutil
# print "Enter"
operating_system = input("Enter 1 if you are using windows and 2 if linux :- ")
if operating_system == "1":
    path_to_desktop = input("Enter the full path of Desktop \nFormat :- C:\\\\Users\\\\User_name\\\\Desktop :- ")
    path_to_move = input("Enter the full path where you want to move the files\nFormat :- C:\\Users\\\\User_name\\\\Folder_you_want_to_move :- ")
    # onlyfiles = [f for f in listdir((path_to_desktop)) if isfile(join((path_to_desktop),f))]
    onlyfiles = [f for f in listdir((path_to_desktop)) if isfile(join((path_to_desktop),f))]
    for i in onlyfiles:
        a =  i.split(".")
        if a[-1]=="lnk":
            continue
        else:
            b=join((path_to_desktop),i)
            c=join((path_to_move),a[-1])
            if not os.path.exists(c):
                os.makedirs(c)
            shutil.move(b,c)
elif operating_system == "2":
    path_to_desktop = input("Enter the full path of Desktop or any other folder you want to go \nFormat :- /home/user_name/Folder_you_want_to_go :- ")
    path_to_move = input("Enter the full path where you want to move the files\nFormat :- /home/user_name/Folder_you_want_to_move :- ")
    # onlyfiles = [f for f in listdir((path_to_desktop)) if isfile(join((path_to_desktop),f))]
    onlyfiles = [f for f in listdir(path_to_desktop) if isfile(join(path_to_desktop,f))]
    for i in onlyfiles:
        a =  i.split(".")
        if a[-1]=="lnk":
            continue
        else:
            b=join(path_to_desktop,i)
            c=join(path_to_move,a[-1])
            if not os.path.exists(c):
                os.makedirs(c)
            shutil.move(b,c)
    # pass
else:
    print("Please Enter correctly 1 or 2 and run the script again")
