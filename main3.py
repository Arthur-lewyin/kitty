from tkinter import * 
import tkinter.font as font

root = Tk()
root.geometry("800x50")

def prank():
    kg = E1.get()

    if(kg.replace('.',"").isnumeric()):
        pl.config(text = 'Enter Password, Hint ur weight in pounds!')
        lg1.grid_forget()
        errormsg.grid_forget()
        lg2.grid(row=1,column=1)
        el.grid(row =2, column= 0)
        ee.grid(row = 2, column= 1)
        con.grid(row =3, column =1)
    else:
        errormsg.grid(row = 2, column = 0)


def convert():
    kg = ee.get()

    if(kg.replace('.',"").isnumeric()):
        p = ((float(kg)*2.2))
        pounds.config(text = "Here Ya go, ur weight in pounds is:" + str(p))
        errormsg2.grid_forget()
    else:
        errormsg2.grid(row = 4, column= 1)

pl= Label(text = 'Enter Password, Hint ur weight in kg!', font = font.Font(size=20),fg="black")
pl.pack()

frame = Frame(root)
frame.pack()

E1 = Entry(frame,width = 20)
E1.grid(row=0 , column= 2)

p = Label(frame, text= "Enter Password! :", font = font.Font(size=10))
p.grid( row =0, column=0)

lg1 = Button(frame,text= "Log in!",bg= "grey",command= prank)
lg1.grid(row=1, column= 1)

lg2 = Button(frame,text= "Log in!",bg= "grey",command=root.destroy)

el = Label(frame, text= "To help you out enter kg here ->", font= font.Font(size= 12))

ee= Entry(frame, width= 20)

errormsg = Label(frame, text= "OKAY, don't be shy put numbers in!")

con = Button(frame, text= "convert!", bg="grey",command = convert)

pounds = Label(frame, font = font.Font(size= 12))
pounds.grid(row = 4, column=1)

errormsg2 = Label(frame, text= "i'm just here to help, put real numbers in")

root.mainloop()