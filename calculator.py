from tkinter import *
import math as m
root=Tk()
i = 0
def display_data(num):
    global i
    e1.insert(i,num)
    i = i + 1
def clear_complete_data():
    #e1.delete(0, END)
    data=e1.get()
    e1.delete(0,END)


def clear_one_data():
    data = e1.get()
    updated_data = data[:-1]
    e1.delete(0,END)
    e1.insert(i, updated_data)

def backspace():
    current= e1.get()
    length=len(current)-1
    e1.delete(length,END)

def click(to_print):
    old=e1.get()
    e1.delete(0,END)
    e1.insert(0,old+to_print)
    return



def addition():
    global num1
    global math
    math="addition"
    num1 = e1.get()
    e1.delete(0,END)

def subtraction():
    global num1
    global math
    math = "subtraction"
    num1 = e1.get()
    e1.delete(0,END)

def multiplication():
    global num1
    global math
    math = "multiplication"
    num1 = e1.get()
    e1.delete(0,END)

def division():
    global num1
    global math
    math = "division"
    num1 = e1.get()
    e1.delete(0,END)

def modulodivision():
    global num1
    global math
    math = "modulus"
    num1 = e1.get()
    e1.delete(0,END)

def sc(event):
    key=event.widget
    text=key['text']
    no=e1.get()
    result=''
    if text=='sin':
        result=str(m.sin(float(no)))
    if text=='log':
        result=str(m.log10(float(no)))
    if text=='tan':
        result=str(m.tan(float(no)))
    e1.delete(0,END)
    e1.insert(0,result)

def submit():
    num2 = e1.get()
    e1.delete(0, END)
    if math=="addition":
        e1.insert(i,int(num1) + int(num2))

    elif math=="subtraction":
        e1.insert(i,int(num1) - int(num2))

    elif math=="multiplication":
        e1.insert(i,int(num1) * int(num2))

    elif math=="division":
        e1.insert(i,int(num1) / int(num2))

    elif math=="modulus":
        e1.insert(i,int(num1) % int(num2))




#root=Tk()
root.title("Calculator")
e1=Entry(root,bg="White",borderwidth=5)
e1.grid(row="0",columnspan="5",padx="10",pady="15")

b1=Button(root,text="9",padx="40",pady="20",command=lambda :display_data("9"))
b1.grid(row="1",column="0")
b2=Button(root,text="8",padx="40",pady="20",command=lambda :display_data("8"))
b2.grid(row="1",column="1")
b3=Button(root,text="7",padx="40",pady="20",command=lambda :display_data("7"))
b3.grid(row="1",column="2")
b4=Button(root,text="+",padx="40",pady="20",command=addition)
b4.grid(row="1",column="3")

b5=Button(root,text="6",padx="40",pady="20",command=lambda :display_data("6"))
b5.grid(row="2",column="0")
b6=Button(root,text="5",padx="40",pady="20",command=lambda :display_data("5"))
b6.grid(row="2",column="1")
b7=Button(root,text="4",padx="40",pady="20",command=lambda :display_data("4"))
b7.grid(row="2",column="2")
b8=Button(root,text="-",padx="40",pady="20",command=subtraction)
b8.grid(row="2",column="3")

b9=Button(root,text="3",padx="40",pady="20",command=lambda :display_data("3"))
b9.grid(row="3",column="0")
b10=Button(root,text="2",padx="40",pady="20",command=lambda :display_data("2"))
b10.grid(row="3",column="1")
b11=Button(root,text="1",padx="40",pady="20",command=lambda :display_data("1"))
b11.grid(row="3",column="2")
b12=Button(root,text="*",padx="40",pady="20",command=multiplication)
b12.grid(row="3",column="3")

b13=Button(root,text="0",padx="40",pady="20",command=lambda: click("0"))
b13.grid(row="4",column="0")
b14=Button(root,text="AC",padx="40",pady="20",command=clear_complete_data)
b14.grid(row="4",column="1")
b15=Button(root,text="C",padx="40",pady="20",command=clear_one_data)
b15.grid(row="4",column="2")
b16=Button(root,text="/",padx="40",pady="20",command=division)
b16.grid(row="4",column="3")

b17=Button(root,text="=",padx="40",pady="20",command=submit)
b17.grid(row="5",column="0")
b18=Button(root,text=".",padx="40",pady="20")
b18.grid(row="5",column="1")
b19=Button(root,text="%",padx="40",pady="20",command=modulodivision)
b19.grid(row="5",column="2")
b20=Button(root,text="()",padx="40",pady="20")
b20.grid(row="5",column="3")

b21=Button(root,text="<--",padx="40",pady="20",command=backspace)
b21.grid(row="6",column="0")

b22=Button(root,text="log",padx="40",pady="20")
b22.bind("<Button-1>", sc)
b22.grid(row="6",column="1")

b23=Button(root,text="sin",padx="40",pady="20")
b23.bind("<Button-1>",sc)
b23.grid(row="6",column="2")
b24=Button(root,text="tan",padx="40",pady="20")
b24.grid(row="6",column="3")


root.mainloop()