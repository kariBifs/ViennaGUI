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


#Window title and dimensions
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

#This function opens the browse window
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
#is checked and it is an if else statement
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
        

#This function will give output after the go button
#is pressed, depending on input from text box or
#opening file
def go_event():
    #if txt_seq is showing do the following
    if txt_seq.winfo_ismapped() == True:
      with open ("input.txt", "w") as usr_inp:
         usr_inp.write(txt_seq.get(1.0, "end-1c"))
      output = subprocess.check_output(["RNAfold", "input.txt"])
      #find the new ps file
      find_file()
      #display the output      
      print (output)
      #open the ps file on canvas      
      open_file()
      
      
    #else do this instead  
    else:
      output = subprocess.check_output(["RNAfold", filepath])
      #find the new ps file
      find_file()
      #display the output      
      print (output)
      #open the ps file on canvas      
      open_file()
      
        
#This function will find all .ps files
def find_file():
    #find all .ps files in tmp folder
    global find_ps
    find_ps = []
    list_dir = os.listdir()
    for x in list_dir:
       if x.endswith(".ps"):
          find_ps.append(x)
      
    #returns a list of all ps files
    return find_ps

#This function will open ps in different window
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

#Function to quit the program   
def quit_prg():
    if messagebox.askokcancel("Quit", 
        "Quitting with delete files\nDo you want to quit?"):
        os.chdir('..')
        shutil.rmtree(os.path.join(os.getcwd(),'tmp'))
        window.destroy()

#Welcome and enter sequence labels
prg_title = Label(window, text="Welcome to RNAfold Program",
       font=("Times New Roman", 14)).grid(
       row=0, columnspan=15, padx=5, pady=5)
lbl_seq = Label(window, text="Enter RNA sequence or upload file :",
       font=("Times New Roman", 12)).grid(
       row=1, columnspan=15, padx=5, pady=5)

#Text box and go button
global txt_seq, go_btn, inp_seq, quit_btn
txt_seq = Text(window, width=40, height=10)
txt_seq.grid(row=3, column=1, columnspan = 6, padx=5, pady=25)
inp_seq = txt_seq.get(1.0, "end-1c")

go_btn = Button(window, text="Go", command=go_event)
go_btn.grid(row=3, column=11, padx=5, pady=10)     


#Checkbutton on window
cb_file = Checkbutton(window, text="To upload file, check box", variable=cb, 
  command= isChecked)
cb_file.grid(row=4, column=1, padx=5, pady=5)  

#Quit button on window
quit_btn = Button(window, text="Quit", command=quit_prg)
quit_btn.grid(row=4, column=11, padx=5, pady=5)

#Delete tmp and close program
window.protocol("WM_DELETE_WINDOW", quit_prg)

#The following is needed to keep window running
window.mainloop()
