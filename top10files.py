import os
from os import listdir
from os.path import isfile, join
import shutil
import sys

# def sizeof_fmt(num, suffix='B'):
#     for unit in ['','K','M','G','T','P','E','Z']:
#         if abs(num) < 1000.0:
#             return "%3.1f%s%s" % (num, unit, suffix)
#         num /= 1000.0
#     return "%.1f%s%s" % (num, 'Yi', suffix)

class Filesize(object):
    """
    Container for a size in bytes with a human readable representation
    Use it like this::

        >>> size = Filesize(123123123)
        >>> print size
        '117.4 MB'
    """

    chunk = 1000
    units = ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
    precisions = [0, 0, 1, 2, 2, 2]

    def __init__(self, size):
        self.size = size

    def __int__(self):
        return self.size

    def __str__(self):
        if self.size == 0: return '0 bytes'
        from math import log
        unit = self.units[min(int(log(self.size, self.chunk)), len(self.units) - 1)]
        return self.format(unit)

    def format(self, unit):
        if unit not in self.units: raise Exception("Not a valid file size unit: %s" % unit)
        if self.size == 1 and unit == 'bytes': return '1 byte'
        exponent = self.units.index(unit)
        quotient = float(self.size) / self.chunk**exponent
        precision = self.precisions[exponent]
        format_string = '{:.%sf} {}' % (precision)
        return format_string.format(quotient, unit)

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
    print (Filesize(i),j)
