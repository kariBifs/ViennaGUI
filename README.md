# Capston
should work for Windows and Linux now. 
#First gui ask for the path to ViennaPackage
################################################################################################
from tkinter import * #import the module tk with all the functions
import os
#first gui

HEIGHT=100
WIDTH=400
root= Tk()
root.title('ViennaRNA Package')# the title for the window

canvas = Canvas(root,height=HEIGHT, width=WIDTH).pack()
l=Label(root,text='Welcome to ViennaRNA!\nEnter your ViennaRna path')
l.place(rely=0.1,relx=0.3)
e=Entry(root, width =50)
e.pack()
#e.insert(0,"Enter your ViennaRna path")

def openVienna():
    global myPath
    myPath=e.get()
    myLabel = Label(root, text= "Your path is: "+myPath)
    myLabel.pack()
   
    
myButton1 = Button(root, text = "Open Program",command = openVienna)
myButton2 = Button(canvas, text= 'Next', padx=10, pady=5,command =root.destroy)
myButton1.pack()
myButton2.pack()
root.mainloop()
#the code needs validation for the path be correct
#variables for the size of the gui. Can be changes to the size wwe want
#############################################################################
#second gui ask for the executable that user wants to run

root = Tk()# create the root(window that will hold everything)
root.title('ViennaRNA Package')# the title for the window

canvas = Canvas(root,height=HEIGHT, width=WIDTH).pack()#we create the canvas where we will put the widgets.
#We may add frames and add widgets in the frames but right now on canvas

topLabel = Label(canvas, text= 'Choose your program!')# a label in canvas welcoming
topLabel.place(rely=0.1,relx=0.3)

#creating a list with tuples so if we want later to add more executables will be easier
opciones=[('RNAfold','RNAfold'),('RNAalifold','RNAalifold'),('RNAplfold','RNAplfold')]

r = StringVar()
r.set('RNAfold')


#we loop our list of tuples to create the radiobuttons and we place them to the left so they stay aligned
for text, mode in opciones:
    Radiobutton(canvas,text=text, variable=r, value =mode).pack(anchor=W)

#to add functionality to our okbutton we define our function clicked that we will call when we define myButton1
def clicked(value):
    global myChoice
    myLabel =Label(canvas,text= value+' selected')
    if value =='RNAfold':
        print("good morning")
    if value =='RNAalifold':
        print("good afternnon")
    if value =='RNAplfold':
        print("good night")
    myChoice=value
    myLabel.pack()
    
#defining buttons
myButton1 = Button(canvas, text = "Select", padx=10,pady=5, command = lambda:clicked (r.get()))
myButton2 = Button(canvas, text= 'Next', padx=10, pady=5,command =root.destroy)
#placing buttons
myButton1.pack()
myButton2.pack()

mainloop()

###############################################################################################################
#third gui

root= Tk()
root.title('ViennaRNA Package')# the title for the window

canvas = Canvas(root,height=HEIGHT, width=WIDTH).pack()
ll=Label(root,text='Enter the path to your RNA file!')
ll.place(rely=0.1,relx=0.3)
e=Entry(root, width =50)
e.pack()
#e.insert(0,"Enter your file's path")

def myFile():
    global rnafile
    rnafile=e.get()
    myLabel = Label(root, text= "Your path is: "+rnafile)
    myLabel.pack()
    os.system('"%s"'% myPath+'/'+myChoice+' < '+rnafile)

myButton5 = Button(root, text = "Enter your file",command=myFile)
myButton6 = Button(canvas, text= 'Close Window', padx=10, pady=5,command =root.destroy)
myButton5.pack()
myButton6.pack()
root.mainloop()

#to do: make the keyboard functional so user can also press enter


