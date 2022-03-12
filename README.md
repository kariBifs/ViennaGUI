![GitHub contributors](https://img.shields.io/github/contributors/kariBifs/capston?color=color)
![GitHub language](https://img.shields.io/badge/language-Python-red)
<p align="center">
 <img src = "imagesread/viennaout.png" width =100>
 <br>
  <strong>GUI for ViennaRNA</strong>.</p>

#**About the Project**
-------------
<br>
GUI for ViennaRNA is a
basic GUI that allows users to add sequences either as 
user input or from a file.The user is allowed to select one of the three programs (RNAfold, RNAalifold, RNAplfold).
The PostScript files generated are also displayed in a GUI. 
This is for local ViennaRNA.
<br>
##**Motivation**
<br>
To make locally installed ViennaRNA package user-friendly.
<br>
##**Built with**
<br>
-Python 3
-tkinter
-Ghostscript
-Pillow
<br>
##**Build Status**
<br>
This app only works on Linux. Adaptation to Windows and MacOS will be added. RNAplfold functionality will also be added soon.
<br>
#**Getting Started**
-------------
**Installation**
<br>
Before running vienna_guiV5.py script ensure the 
following have been installed:

- ViennaRNA package
- Python 3
- tkinter
- Pillow
- Ghostscript

Ensure that all executables have been updated prior to
running the script and that the vienna_config_v1.py file
is in the same directory.

***********************Warning***************************
The ViennaRNA - RNAfold GUI creates a tmp folder in the
active directory. After quit or close the tmp folder will be 
removed. If you need to save any files please do so prior
to quitting or closing the program.
<!--how to use?-->
<br>

**Contribute**
If you have suggestions to improve this project or find some issues with it, please fork the repo and create a pull request.
