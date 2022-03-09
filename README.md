![GitHub contributors](https://img.shields.io/github/contributors/kariBifs/capston?color=color)
<p align="center">
 <img src = "imagesread/viennaout.png" width =100>
</p>

Vienna GUI for RNAfold

The ViennaRNA - RNAfold graphical user interface is a
basic GUI to allow users to add sequences either as 
user input or from a file and output the PostScript
files that are generated. This is for local ViennaRNA
RNAfold program.

Before running vienna_guiV4.py script ensure the 
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
