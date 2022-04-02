#Import modules for main GUI program
import vienna_config_windows
from vienna_config_windows import gs_path, find_gs
import os, sys, subprocess, shutil, time
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk, EpsImagePlugin


#Define functions for the GUI

#This function shows the widget
def display(widget1):
    widget1.grid()

#This function hides the widget
def remove(widget1):
    widget1.grid_remove()

      
#This function opens the browse window and allows only fasta
#and text files to be used. When file selected add to the
#textbox
def browse():    
    file = askopenfile(mode='rb', title='Choose a file',
    filetypes=(('fasta files','*.fa *.fasta *.fna *.ffn *.faa *.frn'),
               ('text files','*.txt')))
    
    global filepath
    filepath = ""
    if file:
        filepath = os.path.abspath(file.name)
        #print (filepath)
        browse_box.delete(0, 'end')
        browse_box.insert(0, filepath)
        
#This function opens browse window for alignment files only.
#This is specific to RNAalifold
def browse_aln():    
    file = askopenfile(mode='rb', title='Choose a file',
    filetypes=(('Clustal files','*.aln'), ('Stockholm', '*.sto *.stk'),
               ('fasta files','*.fa *.fasta *.fna *.ffn *.faa *.frn'),
               ('MAF files', '*.maf')))
    
    global filepath
    filepath = ""
    if file:
        filepath = os.path.abspath(file.name)
        #print (filepath)
        browse_box.delete(0, 'end')
        browse_box.insert(0, filepath)
        

#This function dictates what happens when the checkbutton widget
#is checked. When checked, hide large textbox and show the browse
#box and the browse button. When unchecked, hide browse box and
#browse button
def isChecked():
    if cb.get():
        
        remove(txt_seq)
        display(browse_box)
        browse_box.delete(0, 'end')
        display(browse_btn)

                                
    else:
        remove(browse_box)
        remove(browse_btn)
        display(txt_seq)
        
#This function will display widgets for RNAfold program
def fold_pl_select():
    if txt_seq.winfo_ismapped() == True and cb_file.winfo_ismapped() == True:
       remove(browse_box)
       remove(browse_btn2)
       remove(browse_btn)
       cb.set(0)
       print("textbox present")
       print("checkbox present")
       
    elif browse_box.winfo_ismapped() == True:
       remove(browse_box)
       remove(browse_btn2)
       remove(browse_btn)
       display(txt_seq)
       cb.set(0)
       display(cb_file)
          #cb_file.grid(row=6, column=1, columnspan=5, 
          #             sticky=W, padx=5, pady=5)
             
    else:
       cb.set(0)
       print("nothing to change")
          #cb_file.grid(row=6, column=1, columnspan=5, sticky=W, padx=5, pady=5)
          
#This function will display widgets for RNAalifold program
def aln_select():
    remove(txt_seq)
    remove(cb_file)
    
    display(browse_box)
    browse_box.delete(0, 'end')
    display(browse_btn2)
    


#This function will give output after the go button is pressed, 
#depending on input from text box or opening file
def go_event():
    if rbtn.get()==1:
       #if txt_seq is showing do the following
       if txt_seq.winfo_ismapped() == True:
          with open ("input.txt", "w") as usr_inp:
            usr_inp.write(txt_seq.get(1.0, "end-1c"))
          subprocess.run(["RNAfold.exe", "input.txt"])  
          #find the ps file
          find_file()
          #open the ps file on canvas      
          open_file()
            
       #else do this instead
       else:
          subprocess.run(["RNAfold.exe", filepath])
          #find the ps file
          find_file()
          
          #open the ps file on canvas      
          open_file()
          
    elif rbtn.get()==2:
       subprocess.run(["RNAalifold.exe", filepath])
       #find the ps file
       find_file()
       #display the output in terminal     
       #print (output)
       #open the ps file on canvas      
       open_file()
       
    else:   
       #if txt_seq is showing do the following
       if txt_seq.winfo_ismapped() == True:
          with open ("input.txt", "w") as usr_inp:
            usr_inp.write(txt_seq.get(1.0, "end-1c"))
          output = subprocess.run("RNAplfold.exe < input.txt", shell=True)
          #find the ps file
          find_file()
          #display the output in terminal  
          #print (output)
          #open the ps file on canvas      
          open_file()
            
       #else do this instead
       else:
          subprocess.run("RNAplfold.exe < %s" %filepath,
                        shell=True)
          #find the ps file
          find_file()
          #display the output in terminal     
          #print (output)
          #open the ps file on canvas      
          open_file()
          
                  
#This function will find all .ps files and convert to .pdf files
def find_file():
    #find all .ps files in tmp folder
    global find_ps
    find_ps = []
    list_dir = os.listdir()
    for x in list_dir:
       if x.endswith(".ps"):
          find_ps.append(x)
          
    #for confirmation purpose
    #print(find_ps)
    
    #This will sort the list by ascending time
    find_ps = sorted(find_ps, key=os.path.getmtime)
    return find_ps

#This function will open ps file in a different window
def open_file():
    #ps_window = Toplevel(window)
    #Toplevel window title and dimensions
    #ps_window.title("Output")
    
    #This block of code modified by Karina#
    #empty variable and list
    ps_loc = ""
    ps_loc_list = []
    
    #For debugging purposes
    #print(find_ps)
    
    #For loop that loops through list and gets
    #path for the ps files in tmp folder
    for y in find_ps:
       ps_loc = os.path.join(os.getcwd(),y)
       
       #For debugging purposes
       #print(ps_loc)
       
       #Adds the path to ps_loc_list
       ps_loc_list.append(ps_loc)
      
    #For debugging purposes to ensure all paths
    #were added to list
    print(ps_loc_list)
    
    #For loop to go through the ps_loc_list and open
    #ps files. 
    #Ana modification: if Ghostscript is not in 
    #the environment variables, edit the gs binary    
    for p in ps_loc_list: 
        
       if find_gs == None:
          #Uncomment to check the path
          #print (gs_path[0])
          bin_gs = os.path.join(gs_path[0],'gswin64c')
          #For debugging purpose, uncomment if needed
          #print (bin_gs)
          EpsImagePlugin.gs_windows_binary = bin_gs
          img_open = Image.open(p)
          #img_w, img_h = img_open.size
          img_open.show()
       
       #Code does this if gs is in environment variable
       #for windows
       else:
       #Open the ps file    
          img_open = Image.open(p)
          #img_w, img_h = img_open.size 
          img_open.show()          
    
    #Rest is commented out to check if the above works
    #prior to removal
    #global img
    #img = ImageTk.PhotoImage(img_open)
    
    #Create a blank canvas
    #ps_canvas = Canvas(ps_window, width = img_w, height = img_h, 
    #                   bg= "white", highlightthickness=0)
    
    #Paste the ps file onto the canvas
    #ps_canvas.create_image(0, 0, anchor="nw", image=img)
    #ps_canvas.grid()
    

#Function to quit the program and check if user is sure they want to quit
def quit_prg():
    if messagebox.askokcancel("Quit", 
        "Quitting will delete files\nDo you want to quit?"):
        #change out of directory
        os.chdir('..')
        #remove tmp directory
        shutil.rmtree(os.path.join(os.getcwd(),'tmp'))
        #remove main GUI window
        window.destroy()


#Window title and dimensions
window = Tk()
window.title ("ViennaRNA Package")

#Variables for checkbutton and radio button
cb = IntVar()
rbtn = IntVar()

#Welcome and enter sequence labels
prg_title = Label(window, text="Welcome to Vienna RNA Program",
       font=("Times New Roman", 14)).grid(
       row=0, columnspan=15, padx=5, pady=5)
       
prg_choice1 = Radiobutton(window, text="RNAfold", variable=rbtn,
       value=1, command=fold_pl_select)
prg_choice1.grid(row=1, column=3)
       
prg_choice2 = Radiobutton(window, text="RNAalifold", variable=rbtn,
       value=2, command=aln_select)
prg_choice2.grid(row=1, column=4, padx=3, pady=3)

prg_choice3 = Radiobutton(window, text="RNAplfold", variable=rbtn,
       value=3, command=fold_pl_select) 
prg_choice3.grid(row=1, column=5)
rbtn.set(1)

lbl_seq = Label(window, text="Enter RNA sequence: ",
       font=("Times New Roman", 12)).grid(
       row=2, columnspan=15, padx=5, pady=5)


#Text box and go button on main GUI window
global txt_seq, go_btn, inp_seq, quit_btn
global cb_file, browse_box, browse_btn, browse_btn2

txt_seq = Text(window, width=40, height=10)
txt_seq.grid(row=4, column=1, columnspan=5, padx=5, pady=25)
inp_seq = txt_seq.get(1.0, "end-1c")

go_btn = Button(window, text="Go", command=go_event)
go_btn.grid(row=4, column=7, padx=5, pady=10)     


#Checkbutton and browse on main GUI window
cb_file = Checkbutton(window, text="To upload file, check box", variable=cb, 
                      command= isChecked)
cb_file.grid(row=6, column=1, columnspan=5, sticky=W, padx=5, pady=5)  
cb.set(0)

browse_box = Entry(window, width = 40)
browse_box.grid(row=3, column=1, columnspan=6, padx=5, pady=5)
remove(browse_box)

browse_btn =  Button(window, text="Browse", command=browse)
browse_btn.grid(row=3, column=7, sticky=W, padx=5, pady=5)
remove(browse_btn)

browse_btn2 = Button(window, text="Browse", command=browse_aln)
browse_btn2.grid(row=3, column=7, sticky=W, padx=5, pady=5)
remove(browse_btn2)


#Quit button on window
quit_btn = Button(window, text="Quit", command=quit_prg)
quit_btn.grid(row=6, column=7, padx=5, pady=5)

#Delete tmp and close program
window.protocol("WM_DELETE_WINDOW", quit_prg)

#The following is needed to keep window running
window.mainloop()
