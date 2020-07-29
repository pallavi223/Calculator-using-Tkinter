from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value= eval(screen.get())    #evalualte string
            except Exception as e:
                print(e)
                value="Error"


        scvalue.set(value)
        screen.update()


    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("210x310")
root.resizable(0,0) #resize window
root.title("Calculator ")
#root.wm_iconbitmap("l.ico")   #icon is not working here watch seperate video of icon

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font = "time 16 bold",bg="blue")
screen.pack(fill=X, ipadx=3, pady = 3 ,padx=3)

f = Frame(root, bg="#2B1097")
b = Button(f, text ="9",padx = 11 , pady = 10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT, padx =2, pady=0)

b = Button(f, text ="8",padx = 11 , pady =10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT,  padx =2, pady=1)

b = Button(f, text ="7",padx = 11, pady = 10, font = "time 15 bold" ,bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT,  padx =2, pady=2)
b = Button(f, text ="6",padx = 11 , pady = 10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT, padx =2, pady=3)

f.pack(expand =True,fill="both")

f = Frame(root, bg="#2B1097")

b = Button(f, text ="5",padx = 11 , pady = 10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT,  padx =2, pady=0)

b = Button(f, text ="4",padx = 11 , pady = 10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT,  padx =2, pady=1)
b = Button(f, text ="3",padx = 11 , pady = 10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT, padx =2, pady=2)

b = Button(f, text ="2",padx = 11, pady = 10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT,  padx =2, pady=3)
f.pack(expand =True,fill="both")


f = Frame(root, bg="#2B1097")
b = Button(f, text ="1",padx = 11 , pady = 10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT,  padx =2, pady=0)

b = Button(f, text ="0",padx = 11 , pady = 10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx= 2, pady=1)
b = Button(f, text ="-",padx = 12.5 , pady = 10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT,  padx =2, pady=2)


b = Button(f, text ="+",padx = 11 , pady =10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT,  padx =2, pady=3)
f.pack(expand =True,fill="both")


f = Frame(root, bg="#2B1097")
b = Button(f, text ="*",padx = 12.5, pady =10, font = "time 15  bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT, padx =2, pady=0)

b = Button(f, text ="/",padx = 12.5, pady = 10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT,  padx =2, pady=1)

b = Button(f, text ="=",padx = 10.8 , pady = 10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT,  padx =2, pady=2)

b = Button(f, text ="C",padx = 14 , pady =10, font = "time 15 bold ",bg="light blue")
b.bind("<Button-1>",click)
b.pack(side = LEFT, padx =2, pady=3)

f.pack(expand =True,fill="both")

f = Frame(root, bg="#2B1097")

root.title()

root.mainloop()