import os
from os import listdir
from os.path import isfile, join
import shutil
import sys

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1000.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1000.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

list1 = [0,0,0,0,0,0,0,0,0,0]
list2 = [0,0,0,0,0,0,0,0,0,0]
walk_dir = []
operating_system = input("Enter 1 if you are using windows and 2 if linux :- ")
if operating_system == "1":

    arr = ["A:" , "B:" ,"C:" ,"D:" ,"E:" ,"F:" ,"G:" ,"H:" ,"I:" ,"J:" ]
    for i in arr:

        if os.path.exists(i):
            walk_dir.append(i)
elif operating_system == "2":
    walk_dir=['/home']
else:
    print("Please Enter correctly 1 or 2 and run the script again")
    exit(0)

for i in walk_dir:
    for root, subdirs, files in os.walk(i):

        x = os.path.abspath(root)
        for file1 in files:
                filename = os.path.join(x,file1)
                # print(filename)
                try:
                    a = int(os.path.getsize(filename))
                    # print a,filename
                    for j in range(len(list1)):
                        if a > list1[j]:
                            list1.insert(j,a)
                            list2.insert(j,filename)
                            list1.pop(-1)
                            list2.pop(-1)
                            break
                except:
                    #print filename," doesn't exists"
                    pass
for i,j in zip(list1,list2):
    print (sizeof_fmt(i),j)
