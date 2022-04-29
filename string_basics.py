# Strings

""" Here the strings are immutable ,and we can't change the existing data and
there is another way to manipulate string using "replace" fun
 and replace function creates a clone of existing data and change it as we want."""
# -----------------
var = "chary"
output = var.replace("c", "C")
# print(output)
# -------

# Swap strings

var = "dhoni"
var1 = "kohli"
var, var1 = var1, var
# print(var,var1,end=" ")

#  ----------------

'''forward compatability : 
backward compatability: 
difference between above two : 
'''
# -------------------------
# Escape character "\"
"There are two ways to keep multiline COMMENTS shown below"
"""this is the one way to keep  string triple cots"""
"or"
"another thing using escpae character like shown in this line \
like this"
# -------------------

# raw data using character called 'r"here anything suppose now in this example we taken some dumy folder    "'

var2 = r"C:\chary\preenth.pdf"
# print(var2)

# -------------------

# shallow copy and deep copy

# shallow copy

var3 = ["chary", "name", "sudheer"]
var4 = var3
var4[1] = "vishnu priya"
# print(var3,var4)

# deep copy

var3 = ["chary", "name", "sudheer"]
var4 = var3[:]
var4[1] = "rashmi"
# print(var3,var4)

# -------------------------
# count,find,index
var5 = "rahul is kabaddi player in indaian team"
'''
print(var5.count("i"))
print(var5.count("i",2))
print(var5.count("i",2,5))
'''

var100 = "rahul is kabaddi player in indaian team"
'''
print(var5.find("i"))
print(var5.find("i",2))                #here if negetive senario this can return -1
print(var5.find("i",2,5))
'''

var000 = "rahul is kabaddi player in indaian team"
'''
print(var5.index("i"))
print(var5.index("i",2))                # but here the index throw an error in negetive senario
print(var5.index("i",2,5))'''

# ------------------
# split() function and partition
var6 = "rahul is kabaddi player in indaian team"
output2 = list(var6)  # it returns charctered list

var6 = "rahul is kabaddi player in indaian team"
output3 = var6.split()  # it returns w.r.t white spaces

var6 = var6.partition("a")

# -----------------------------------
# strip function -> it is used to remove extra spaces starting and ending of string

var7 = " rahul is kabaddi player in indaian team "
output1 = var7.strip()
# print(output1)

# list
var8 = ["a", "b", "c", "d", "e"]
for x, y in enumerate(var8):
    if x % 2 == 0:  # it is done by index here x represents index
        var8.pop(x)  # and y represents value or data in the list
# print(var8)


var8 = ["a", "b", "c", "d", "e"]
for x, y in enumerate(var8[:]):
    if x % 2 == 0:  # it is done by elements
        var8.remove(y)
# print(var8)

# ------------------------

# Comparing two files
# --> reading files
'''
f1 = open("C:/Users/pc/Desktop/GitHub/Futurense_work/file1.txt", "r")
f2 = open("C:/Users/pc/Desktop/GitHub/Futurense_work/file2.txt", "r")
f3 = open("file3.txt", "r+")
# -> i is a flag variable here it is used to track line numbers in txt file
i = 0

for line1 in f1:
    i += 1

    for line2 in f2:

        # matching line1 from both files
        if line1 == line2:
            # print IDENTICAL if similar
            #print("Line ", i, ": IDENTICAL")
        else:
            #print("Line ", i, ": The file is created check file3 ")
            # else print that line from both files
            # line1line2
            #f3.write(
               # "this is the word"+str(i)+ "---> " + line1 + " <---" + "in file1 \nand\n this is the word in " + "---> " + line2 + " <----" + "file2\n\n\n")

        #break

# closing files
f1.close()
f2.close()
f3.close()
'''





# -------------------------------------------------------

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os

# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('300x150')

l=[]
def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )
    l.extend(filenames)



# open button
open_button = ttk.Button(
    root,
    text='Open Files',
    command=select_files
)
open_button.pack(expand=True)
root.mainloop()
import copy
# a=[1,2,3,4,5,6]
# b=a.copy().s
# b[3]="abs"
# print(b)
# print(a)

# a="india is great"
# print(a.partition("i"))
# reading files
f1 = open(r"{}".format(l[0]), "r")
f2 = open(r"{}".format(l[1]), "r")
#
f= open("new.txt","w")
#
# #i=0
l=f1.readlines()
s=f2.readlines()
p=[]
q=[]
for i in l:
    c=i.replace("\n","")
    p.append(c)
for j in s:
    d=j.replace("\n","")
    q.append(d)
i=0
for line1 in range(0,len(p)):
    i=i+1
    for line2 in range(0,len(q)):
        if p[line1]!=q[line2] and line1==line2:
            f.write(p[line1])
            f.write(q[line2])
            # data = [["ABC","DEF"],[p[line1],q[line2]]]
            # print(tabulate(data, headers='firstrow', showindex='always',tablefmt='fancy_grid'))

# closing files
f1.close()
f2.close()
f.close()
os.system(r"C:\Users\pc\Desktop\GitHub\Futurense_work\output.txt")
# # A simple Python program to demonstrate
# # getpass.getpass() to read security question
# # User's password without echoing
# # import maskpass # to hide the password
# #
# # # masking the password
# # pwd = maskpass.askpass(mask="")
# # print(pwd)