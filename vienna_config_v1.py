#!/usr/bin/env python

#import modules
import os, sys, shutil 
import subprocess

#Find RNAfold
find_exe = shutil.which("RNAfold")

#Remove the comment for debugging
#print os.path.dirname(find_exe)

#Get the directory of executable
exe_path = os.path.dirname(find_exe)

#Check if directory is in PATH
if os.path.isdir(exe_path) == True:
   print ("ViennaRNA - RNAfold..........ok")
   
else:
   sys.path.insert(0, exe_path)
   print ("ViennaRNA - RNAfold..........added")

#Check Ghostscript is installed:
if shutil.which("gs") is not None:
   print ("Ghostscript..................ok")
else:
   print ("Ghosescript not found, try\n\nsudo apt install ghostscript")
   sys.exit()

#Check is modules are installed
try:
   import tkinter
   import PIL
except ModuleNotFoundError as msg:
   print (msg)
   sys.exit()   

   
#Create tmp directory if it does not exist
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

