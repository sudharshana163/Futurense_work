
# Transaction - "ACID"
# A-Atomicity --> the changes of all transaction is done in a single unit or there is no changes in transactions
# C-Consistency --> it is nothing but sequential execution of query
# I-Isolation -->Isolation is the separation of resource or data modifications made by different transactions.
#         -->in this isolation there are four levels of isolation
#             * serializable - it is a highest level which means one trascation must be complete and another can start
#             * repeatable reads  -
# D-Durability -->


from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('600x500')
root.resizable(0, 0)
# root.title('')


x = StringVar()
y = StringVar()


def home():
    x.set("")
    y.set("")

    f1 = Frame()
    f1.place(x=0, y=0, width=600, height=500)
    f1.configure()

    b1 = Button(f1, text='DB Operations', font=('', 9), command=db_operation)
    b1.place(x=210, y=50, height=50, width=120)

def db_operation():
    f1 = Frame()
    f1.place(x=0, y=0, width=600, height=500)
    f1.configure()
    b2 = Button(f1, text='MySql', font=('', 9), command=nextpage)
    b2.place(x=210, y=110, height=50, width=120)
    b2 = Button(f1, text='Oracle', font=('', 9), command=oracle)
    b2.place(x=210, y=175, height=50, width=120)
    b2 = Button(f1, text='Architechiure', font=('', 9), command=Architecture)
    b2.place(x=210, y=245, height=50, width=120)
    b2 = Button(f1, text='back', font=('', 9), command=home)
    b2.place(x=210, y=305, height=50, width=120)
def nextpage():
    f2 = Frame()
    f2.place(x=0, y=0, width=600, height=500)
    f2.configure()

    b1 = Button(f2, text='DML', font=('Eras Bold ITC', 16), command=DML)
    b1.place(x=100, y=100, height=100, width=150)

    b1 = Button(f2, text='DDL', font=('Eras Bold ITC', 16), command=DDL)
    b1.place(x=300, y=100, height=100, width=150)

    b1 = Button(f2, text='<-HOME', font=('Eras Bold ITC', 16), command=db_operation)
    b1.place(x=400, y=400, height=70, width=100)


def DML():
    f2 = Frame()
    f2.place(x=0, y=0, width=600, height=500)
    f2.configure()

    b1 = Button(f2, text='Insert ', font=('', 16), command=Insert)
    b1.place(x=250, y=100, height=80, width=90)

    b1 = Button(f2, text='Update', font=('', 16), command=Update)
    b1.place(x=250, y=200, height=80, width=90)

    b1 = Button(f2, text='Delete', font=('', 16), command=Delete)
    b1.place(x=250, y=300, height=80, width=90)

    b1 = Button(f2, text='<-Back', font=('', 16), command=nextpage)
    b1.place(x=400, y=400, height=60, width=90)


def Insert():
    with open('Insert.txt') as f:
        contents = f.read()
        messagebox.showinfo('Insert',contents)



def Update():
    with open('Update.txt') as f:
        contents = f.read()
        messagebox.showinfo('Update',contents)



def Delete():
    with open('Delete.txt') as f:
        con=f.read()
        messagebox.showinfo('MySql', con)

def Mysql():
    with open('Mysql..txt') as g:
        messagebox.showinfo('MySql', 'Configuration need to be done')
def oracle():
    messagebox.showinfo('Oracle',"Configuration need to be done")
def Architecture():
    with open('Architecture.txt') as f:
        contents=f.read()
        messagebox.showinfo('Architechiure',contents)
    #print(contents)
def DDL():
    pass

home()
root.mainloop()