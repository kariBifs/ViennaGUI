#!/usr/bin/env python

#import modules
import os, sys, shutil 
import subprocess
from itertools import chain

paths_search = ["C:\\Program Files", "C:\\Program Files (x86)"]

#Find the executable
find_exe = shutil.which("RNAfold.exe")

#Remove the comment for debugging
#print os.path.dirname(find_exe)

#Get the directory of executable
exe_path = os.path.dirname(find_exe)
exe_path_list = []

        
if exe_path is None:
    for path, dirs, files in chain.from_iterable(
       os.walk(path) for path in paths_search):
         if 'RNAfold.exe' in files:
           exe_path_list.append(path)
    print(exe_path_list)
    sys.path.append(exe_path_list[0])
    
#Check if directory is in PATH
if os.path.isdir(exe_path) == True:
   print ("ViennaRNA - RNAfold..........ok")
   
else:
   sys.path.append(exe_path)
   print ("ViennaRNA - RNAfold..........added")

#Check if ghostscript is installed
find_gs = shutil.which("gswin64.exe")
gs_path = []

if find_gs == None:
    for path, dirs, files in chain.from_iterable(
      os.walk(path) for path in paths_search):
        if 'gswin64.exe' in files:
           gs_path.append(path)
    print (gs_path)
    sys.path.append(gs_path[0])
    print ("Ghostscript...............added")
   
else:
   print ("Ghostscript...............ok")
   

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

