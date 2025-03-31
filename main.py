from tkinter import * 
import tkinter.font as font

root= Tk()
root.geometry("500x250")

def kitty():
    celcius = enter.get()

    if(celcius.replace('.',"").isnumeric()):
        far = ((float(celcius)* 9/5)+32)
        labelseq.config(text = "temperature in Fareheit:"+ str(far))
        errormsg.grid_forget()
    else:
        errormsg.grid(row =1,column= 1)



temp = Label(text ="Celsius - > Fahrentheit", font = font.Font(size=20), fg = 'grey')
temp.pack()

frame = Frame(root)
frame.pack(pady = 20)

labels = Label(frame, text = "Enter Temprature in Celsius",font=font.Font(size=10))
labels.grid(row= 0, column= 0)

enter = Entry(frame, width = 20)
enter.grid(row = 0, column= 1)

labelseq = Label(frame, font = font.Font(size =12))
labelseq.grid(row =2, column =1, columnspan=2, pady=10)

con = Button(frame, text= "convert", bg = "green", command=kitty)
con.grid(row = 3, column= 0)


errormsg = Label(frame, text = " Please place me a valid number")

root.mainloop()