#This GUI is for Linux only, for Windows and Mac use
#the installer instead

#Import modules for main GUI program
import vienna_config_v1
import os, sys, subprocess, shutil
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


#Main GUI window title and dimensions
#The GUI uses grid as the geometry manager
window = Tk()
window.title ("ViennaRNA Package")

#Variable for checkbutton
cb = IntVar()

#Define functions for the GUI

#This function shows the widget on the window 
def display(widget1):
    widget1.grid(row=3, column=1, columnspan = 6, padx=5, pady=25)

#This function hides the widget on the window
def remove(widget1):
    widget1.grid_remove()

#This function opens the browse window and allows only fasta
#and text files to be used. When file selected add to the
#textbox
def browse():    
    file = askopenfile(mode='rb', title='Choose a file',
    filetypes=(('fasta files','*.fa *.fasta'),
               ('text files','*.txt')))
    
    global filepath
    filepath = ""
    if file:
        filepath = os.path.abspath(file.name)
        #print (filepath)
        browse_box.insert(0, filepath)
        

#This function dictates what happens when the checkbutton widget
#is checked. When checked, hide large textbox and show the browse
#box and the browse button. When unchecked, hide browse box and
#browse button
def isChecked():
    if cb.get():
        global browse_box
        remove(txt_seq)
        browse_box = Entry(window)
        browse_box.grid(row=3, column=1, columnspan=6, padx=5, pady=5)
        global browse_btn
        browse_btn =  Button(window, text="Browse", command=browse)
        browse_btn.grid(row=3, column=6, padx=5, pady=5)
                                
    else:
        remove(browse_box)
        remove(browse_btn)
        display(txt_seq)
        

#This function will give output after the go button is pressed, 
#depending on input from text box or opening file
def go_event():
    #if txt_seq is showing do the following
    if txt_seq.winfo_ismapped() == True:
      with open ("input.txt", "w") as usr_inp:
         usr_inp.write(txt_seq.get(1.0, "end-1c"))
      output = subprocess.check_output(["RNAfold", "input.txt"])
      #find the ps file
      find_file()
      #display the output in terminal  
      print (output)
      #open the ps file on canvas      
      open_file()
      
      
    #else do this instead  
    else:
      output = subprocess.check_output(["RNAfold", filepath])
      #find the ps file
      find_file()
      #display the output in terminal     
      print (output)
      #open the ps file on canvas      
      open_file()
      
        
#This function will find all .ps files within tmp folder
def find_file():
    global find_ps
    find_ps = []
    list_dir = os.listdir()
    for x in list_dir:
       if x.endswith(".ps"):
          find_ps.append(x)
      
    #returns a list of all ps files
    return find_ps

#This function will open ps file in a different window
def open_file():
    ps_window = Toplevel(window)
    #Toplevel window title and dimensions
    ps_window.title("Output")
    
    ps_loc = ""
    print(find_ps)
    for y in find_ps:
       ps_loc = os.path.join(os.getcwd(),y)
        
    #Open the ps file    
    img_open = Image.open(ps_loc)
    img_open = img_open.resize((600, 600), Image.ANTIALIAS)
    global img
    img = ImageTk.PhotoImage(img_open)
    
    #Create a blank canvas
    ps_canvas = Canvas(ps_window, width= 600, height = 600, bg= "white", 
    highlightthickness=0)
    
    #Paste the ps file onto the canvas
    ps_canvas.create_image(0, 0, anchor="nw", image=img)
    ps_canvas.grid()

#Function to quit the program and check if user is sure they want to quit
def quit_prg():
    if messagebox.askokcancel("Quit", 
        "Quitting with delete files\nDo you want to quit?"):
        #change out of directory
        os.chdir('..')
        #remove tmp directory
        shutil.rmtree(os.path.join(os.getcwd(),'tmp'))
        #remove main GUI window
        window.destroy()

#Additional details for main GUI window
#Welcome and enter sequence labels on main GUI window
prg_title = Label(window, text="Welcome to RNAfold Program",
       font=("Times New Roman", 14)).grid(
       row=0, columnspan=15, padx=5, pady=5)
lbl_seq = Label(window, text="Enter RNA sequence or upload file :",
       font=("Times New Roman", 12)).grid(
       row=1, columnspan=15, padx=5, pady=5)

#Text box and go button on main GUI window
global txt_seq, go_btn, inp_seq, quit_btn
txt_seq = Text(window, width=40, height=10)
txt_seq.grid(row=3, column=1, columnspan = 6, padx=5, pady=25)
inp_seq = txt_seq.get(1.0, "end-1c")

go_btn = Button(window, text="Go", command=go_event)
go_btn.grid(row=3, column=11, padx=5, pady=10)     


#Checkbutton on main GUI window
cb_file = Checkbutton(window, text="To upload file, check box", variable=cb, 
  command= isChecked)
cb_file.grid(row=4, column=1, padx=5, pady=5)  

#Quit button on main GUI window to delete tmp and close program
quit_btn = Button(window, text="Quit", command=quit_prg)
quit_btn.grid(row=4, column=11, padx=5, pady=5)

#When closing by clicking X, delete tmp and close program
window.protocol("WM_DELETE_WINDOW", quit_prg)

#The following is needed to keep main GUI window running
window.mainloop()
