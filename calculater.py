from tkinter import *

root =Tk()
root.title("Simple Python Calculator")

e=Entry(root,width=35)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_clicked(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def btn_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)

def btn_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def btn_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiflication"
    f_num = int(first_number)
    e.delete(0, END)

def btn_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)



def btn_equal():
   second_number=e.get()
   e.delete(0,END)
   if math=="addition":
    e.insert(0,f_num + int(second_number))
   if math == "subtraction":
        e.insert(0, f_num - int(second_number))
   if math=="division":
    e.insert(0,f_num / int(second_number))
   if math=="multiflication":
    e.insert(0,f_num * int(second_number))

def btn_clear():
    e.delete(0,END)

button_1=Button(root, text="1",bg="pink",padx=40,pady=20,command= lambda :button_clicked(1))
button_2=Button(root, text="2",bg="pink",padx=40,pady=20,command= lambda :button_clicked(2))
button_3=Button(root, text="3",bg="pink",padx=40,pady=20,command= lambda :button_clicked(3))
button_4=Button(root, text="4",bg="pink",padx=40,pady=20,command= lambda :button_clicked(4))
button_5=Button(root, text="5",bg="pink",padx=40,pady=20,command= lambda :button_clicked(5))
button_6=Button(root, text="6",bg="pink",padx=40,pady=20,command= lambda :button_clicked(6))
button_7=Button(root, text="7",bg="pink",padx=40,pady=20,command= lambda :button_clicked(7))
button_8=Button(root, text="8",bg="pink",padx=40,pady=20,command= lambda :button_clicked(8))
button_9=Button(root, text="9",bg="pink",padx=40,pady=20,command= lambda :button_clicked(9))
button_0=Button(root, text="0",bg="pink",padx=40,pady=20,command= lambda :button_clicked(0))

button_add=Button(root,text="+",bg="purple",padx=40,pady=20,command=btn_add)
button_equal=Button(root,text="=",bg="purple",padx=40,pady=20,command=btn_equal)
button_clear=Button(root,text="clear",bg="purple",padx=40,pady=20,command=btn_clear)
button_subtract=Button(root,text="-",bg="purple",padx=40,pady=20,command=btn_subtract)
button_multiply=Button(root,text="*",bg="purple",padx=40,pady=20,command=btn_multiply)
button_divide=Button(root,text="/",bg="purple",padx=40,pady=20,command=btn_divide)



button_1.grid(row=3,column=2)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=0)

button_4.grid(row=2,column=2)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=0)

button_7.grid(row=1,column=2)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=0)

button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_subtract.grid(row=5,column=0)
button_divide.grid(row=5,column=1)
button_multiply.grid(row=5,column=2)
button_equal.grid(row=4,column=2)
button_clear.grid(row=6,column=1,columnspan=2)


root.mainloop()