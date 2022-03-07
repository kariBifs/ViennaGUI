#!/usr/bin/env python

#import modules
import os, sys, shutil 
import subprocess

#Find RNAfold executable
find_exe = shutil.which("RNAfold")

#Remove the comment for debugging
#print (find_exe)
#print os.path.dirname(find_exe)

#Get the directory of executable
exe_path = os.path.dirname(find_exe)

#Check if directory is in PATH, if not add to PATH
if os.path.isdir(exe_path) == True:
   print ("ViennaRNA - RNAfold..........ok")
   
else:
   sys.path.insert(1, exe_path)
   print ("ViennaRNA - RNAfold..........added")

#Check Ghostscript is installed, if not suggest installation and exit:
if shutil.which("gs") is not None:
   print ("Ghostscript..................ok")
else:
   print ("Ghosescript not found, try\n\nsudo apt install ghostscript")
   sys.exit()

#Check if modules tkinter and pillow are installed, else exit
try:
   import tkinter
   import PIL
except ModuleNotFoundError as msg:
   print (msg)
   sys.exit()   

   
#Create tmp directory and change to the new directory,
#else change into tmp directory if already there
current_path = os.getcwd()
temp_dir = "tmp"
new_path = os.path.join(current_path, temp_dir)

if os.path.isdir(new_path) == False:
   os.mkdir(new_path)
   print ("tmp directory...........created")
   os.chdir(new_path)
   
else:
   print("tmp directory............ok")
   os.chdir(new_path)

