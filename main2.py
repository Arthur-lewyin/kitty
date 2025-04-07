from tkinter import * 
import tkinter.font as font

root = Tk()
root.geometry("700x250")

def convert():
    pound = enter.get()

    if(pound.replace('.',"").isnumeric()):
        e = ((float(pound)*1.15))
        euro.config(text = " well good thing you owe:" + str(e))
        em.grid_forget()
    else:
        em.grid(row =1, column =1)

heading = Label(text = "Debt colector", font = font.Font(size = 20), fg = "green") 
heading.pack() 

closer = Frame(root)
closer.pack(pady=30)

poundL = Label(closer, text = "How many pounds do you have?", font =font.Font(size=20),fg = 'orange')
poundL.grid(row = 0,column = 0) 

enter = Entry(closer ,width = 20)
enter.grid(row = 0, column = 1)

euro = Label(closer, font = font.Font(size = 12))
euro.grid(row =2, column =1, columnspan =2, pady =10)

con = Button(closer,text="convert",bg = "orange",fg= "green", command = convert)
con.grid(row =3, column = 0)

em = Label(closer, text = "Yeah that's not possible...")

root.mainloop()