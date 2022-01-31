# Capston
#Karina can be radiobuttons or check buttons for first windows-------------------------------------------------------------------------------------------------------------
#This is a test and a draft
import tkinter as tk
import tkinter.messagebox
#creating the first window with options
HEIGHT = 400
WIDTH = 500
class MyGUI:
    def __init__(self):
        self.root = tk.Tk()# creates main windows widget
        #creates title
        self.root.title(' ViennaRNA Package')
        self.canvas = tk.Canvas(self.root,bg='DarkOlivegreen', height = HEIGHT, width = WIDTH,bd=1)
        self.canvas.pack()

        #creates frame
        self.top_frame = tk.Frame(self.root)
        self.top_frame.place (relx = 0.05, rely = 0.05, relwidth = 0.9,relheight = 0.2)
    
        #label in top frame
        self.label_topf = tk.Label(self.top_frame, text= 'Welcome! Choose an option!',font=('Cursive',11))
        self.label_topf.place(relx=0.1,rely=0.1, relwidth=0.9, relheight= 0.4)
    
        #middle frame radiobutton
        self.middle_frame =tk.Frame(self.root)
        self.middle_frame.place(relx =0.05, rely = 0.25, relwidth = 0.9, relheight=0.6)

        self.radio_var = tk.IntVar()#create an Int Var object to use with the Radiobuttons
        self.radio_var.set(1)#set the intVar object to 
        self.rb1 = tk.Radiobutton(self.middle_frame, text = 'RNAfold',variable=self.radio_var,value=1,font=('Arial',12))
        self.rb2 = tk.Radiobutton(self.middle_frame, text = 'RNAplfold', variable=self.radio_var, value=2,font=('Arial',12))
        self.rb3 = tk.Radiobutton(self.middle_frame, text = 'RNAlifold', variable=self.radio_var, value=3, font=('Arial',12))
        #pack radiobuttons
        self.rb1.place(relx=0.1, rely=0.1,relheight=0.35, relwidth= 0.9)
        self.rb2.place(relx=0.1, rely=0.3, relheight=0.35, relwidth=0.9)
        self.rb3.place(relx=0.1, rely=0.5, relheight=0.35, relwidth=0.9)
    
        #buttons for lower_frame
        self.lower_frame = tk.Frame(self.root)
        self.lower_frame.place(relx=0.05, rely = 0.7, relwidth = 0.9, relheight= 0.25)
        self.ok_button = tk.Button(self.lower_frame,text='OK',bd=5, command = self.show_choice)
        self.quit_button = tk.Button(self.lower_frame, text = 'Quit',bd=5, command = self.root.destroy)
        #pack buttons
        self.ok_button.place(relx =0.3,rely =0.2, relwidth = 0.4, relheight =0.3)
        self.quit_button.place(relx =0.3, rely= 0.6, relwidth= 0.4, relheight = 0.3)

        #enter the tkinter main loop
        tk.mainloop()

    def show_choice(self):
        tk.messagebox.showinfo('Selection', 'You selected option '+str(self.radio_var.get()))
    
    
my_gui = MyGUI()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
