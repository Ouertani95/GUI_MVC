# TP6_GUI_MVC

## About :

This package contains 5 modules for a yearbook application based on the MVC model :

- controller.py : main module that controls and runs the application
- model.py : represents the model of the application that manipulates the data
- view_obj.py : represents the view superclass from which derive all the application views
- gui.py : represents the GUI view of the application for user friendly usage
- cli.py : represents the interactive CLI view of the application for advanced usage cases


## Features :

**Main Feature** :
- *Search* a person inside the yearbook
- *Insert* a person to the yearbook
- *Delete* a person from the yearbook

## Installation :

To install this script use the following commands :

```bash
mkdir ~/Desktop/OUERTANI/
cd ~/Desktop/OUERTANI/
git clone https://github.com/Ouertani95/TP6_GUI_MVC
pip install -r requirements.txt
```
==> You're now good to go!

## Usage :

For information on using the script you can type the following commands :

```bash
cd ~/Desktop/OUERTANI/
python3 controller.py
# Choose a GUI or a CLI by typing 1 or 2
```

**GUI**

If you choose a GUI by typing 1 you will get an interface in which you have fields to type information about the person and then click on the corresponding button to initiate the chosen function.

At the end of the process a result window will be displayed.

**CLI**

If you choose a CLI by typing 2 you will get an interactive interface inside the terminal.
The following commands can be used : 
- help -v : get help about all the available functions for the application
- insert : initiates the insertion process by prompting for input of information
- delete : initiates the deletion process by prompting for name input
- search : initiates the search process by prompting for name input
==> At the end of each chosen function a message will be displayed with the results.

## Authors :

**Mohamed Ouertani**