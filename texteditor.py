

    

from tkinter import *


import  tkinter.filedialog


root=Tk()

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y)

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)







text=Text(root)

def FontHelvetica():

  global text
text.config(font="Helvetica")
def FontCourier():
  global text
text.config(font="Courier")
font=Menubutton(root, text="Font") 

font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu
helvetica=IntVar() 
courier=IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier,
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, 
command=FontHelvetica)




























menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
menu.add_cascade(label='Font', menu=font.menu)
helpmenu.add_command(label='About')


mylist = Listbox(root, yscrollcommand = scrollbar.set )
#for line in range(100):
 #  mylist.insert(END, "This is line number " + str(line))

#mylist.pack( side = TOP ,  fill = BOTH )

#scrollbar.config( command = mylist.yview )

#text = Text(root, height = 550, width = 550)
#text.pack()




#import tkinter as db


def saveas():
    global text  
    t = text.get("1.0", "end-1c")
    savelocation=tkinter.filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()
button =Button(root, text='Save', width=25, command=saveas)
button.pack()







T = Text(root, height=400, width=400)
T.pack()
T.insert(END, 'Welcome to our text editor \nBEST Editor\n')

root.title("OUR EDIT0R")
root.geometry("900x900")


root.mainloop()



    
	