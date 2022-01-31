# Capston
#Karina can be radiobuttons or check buttons for first windows-------------------------------------------------------------------------------------------------------------
#This is a test and a draft
import tkinter as tk
from tkinter import *
import tkinter.messagebox
#creating the first window with options
HEIGHT = 400
WIDTH = 500

def main():
        opcion_window()

def opcion_window():
    root = tk.Tk()# creates main windows widget
    #creates title
    root.title(' ViennaRNA Package')
    canvas = tk.Canvas(root,bg='DarkOlivegreen', height = HEIGHT, width = WIDTH,bd=1)
    canvas.pack()

    #creates frame
    top_frame = tk.Frame(root)
    top_frame.place (relx = 0.05, rely = 0.05, relwidth = 0.9,relheight = 0.2)
    
    #label in top frame
    label_topf = tk.Label(top_frame, text= 'Welcome! Choose an option!',font=('Cursive',11))
    label_topf.place(relx=0.1,rely=0.1, relwidth=0.9, relheight= 0.4)
    
    #middle frame radiobutton
    middle_frame =tk.Frame(root)
    middle_frame.place(relx =0.05, rely = 0.25, relwidth = 0.9, relheight=0.6)

    r = IntVar()#create an Int Var object to use with the Radiobuttons
    r.set(1)#set the intVar object to 
    rb1 = tk.Radiobutton(middle_frame, text = 'RNAfold',variable=r,value=1,font=('Arial',12))
    rb2 = tk.Radiobutton(middle_frame, text = 'RNAplfold', variable=r, value=2,font=('Arial',12))
    rb3 = tk.Radiobutton(middle_frame, text = 'RNAlifold', variable=r, value=3, font=('Arial',12))
    #pack radiobuttons
    rb1.place(relx=0.1, rely=0.1,relheight=0.35, relwidth= 0.9)
    rb2.place(relx=0.1, rely=0.3, relheight=0.35, relwidth=0.9)
    rb3.place(relx=0.1, rely=0.5, relheight=0.35, relwidth=0.9)
    
    #buttons for lower_frame
    lower_frame = tk.Frame(root)
    lower_frame.place(relx=0.05, rely = 0.7, relwidth = 0.9, relheight= 0.25)
    ok_button = tk.Button(lower_frame,text='OK',bd=5, command = show_choice(r))
    quit_button = tk.Button(lower_frame, text = 'Quit',bd=5, command = root.destroy)
    #pack buttons
    ok_button.place(relx =0.3,rely =0.2, relwidth = 0.4, relheight =0.3)
    quit_button.place(relx =0.3, rely= 0.6, relwidth= 0.4, relheight = 0.3)

    #enter the tkinter main loop
    tk.mainloop()

def show_choice(r):
    tk.messagebox.showinfo('Selection', 'You selected option '+str(r.get()))
   
    
main()

 #function to create the window that ask for file
 #direct the file entered to the address for VIENNA it has to vienna option using if, elif, else
 #example:
 #if option 1:
 #path to vienna(C:\Users\kbrig\OneDrive\Escritorio\Vienna\downloads)>RNAfold < path to file entered in window
 #open the file created by Vienna and 
            

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
