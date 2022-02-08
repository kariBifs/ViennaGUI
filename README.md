# Capston
#The order of the windows have changed in order to go better with the flow chat of the presentation and this connect to os. Look for the file with the output. It should be in 
#the folder where you have the .py and it will be a .ps it should have the name of the file that you used in the file path but extension .ps
#Note: should work for Windows and Linux now. Windows remember to put foward slashes in your paths
#First gui################################################################################################
from tkinter import * #import the module tk with all the functions
import os
#first gui

HEIGHT=50
WIDTH=300
root= Tk()
root.title('ViennaRNA Package')# the title for the window

canvas = Canvas(root,height=HEIGHT, width=WIDTH).pack()

e=Entry(root, width =50)
e.pack()
e.insert(0,"Enter your ViennaRna path")

def openVienna():
    global myPath
    myPath=e.get()
    myLabel = Label(root, text= "Your path is: "+myPath)
    myLabel.pack()
   
    
myButton = Button(root, text = "Open Program",command = openVienna)
myButton.pack()
root.mainloop()
#the code needs validation for the path be correct
#variables for the size of the gui. Can be changes to the size wwe want
#############################################################################
#second gui
HEIGHT=50
WIDTH=300

root = Tk()# create the root(window that will hold everything)
root.title('ViennaRNA Package')# the title for the window

canvas = Canvas(root,height=HEIGHT, width=WIDTH).pack()#we create the canvas where we will put the widgets.
#We may add frames and add widgets in the frames but right now on canvas

topLabel = Label(canvas, text= 'Welcome to ViennaRna!')# a label in canvas welcoming
topLabel.pack()#this will place label, we then can change to .grid() or .place() to be more specific

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
myButton1 = Button(canvas, text = "SELECT", padx=10,pady=5, command = lambda:clicked (r.get()))
myButton2 = Button(canvas, text= 'QUIT', padx=10, pady=5,command =root.destroy)
#placing buttons
myButton1.pack()
myButton2.pack()

mainloop()

###############################################################################################################
#third gui

HEIGHT=50
WIDTH=300
root= Tk()
root.title('ViennaRNA Package')# the title for the window

canvas = Canvas(root,height=HEIGHT, width=WIDTH).pack()

e=Entry(root, width =50)
e.pack()
e.insert(0,"Enter your file's path")

def myFile():
    global rnafile
    rnafile=e.get()
    myLabel = Label(root, text= "Your path is: "+rnafile)
    myLabel.pack()
    os.system('"%s"'% myPath+'/'+myChoice+' < '+rnafile)

    #print(e)
myButton = Button(root, text = "Enter your file",command=myFile)
myButton.pack()
root.mainloop()


