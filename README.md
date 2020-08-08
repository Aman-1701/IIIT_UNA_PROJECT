#INSTALL python 3.7 64-bit before running from the PYTHON37 project in the folder

USE PYTHON 3.7 TO RUN THE PROGRAM AS IT USES TENSORFLOW VERSION==1.15 AND PYTESSERACT

Open cmd in the folder 

Now,
type =>>  pip install -r requirements.txt (for windows)
to install the packages

===>
	Input_Images
	Identified_LIcense_Plates_Images
	Output

Only the contents of above mentioned folders should be changed

To run the program=>>

The Input_Images folder contains sample input for the program
You can delete them and add another images which are needed to be processed

Now just double click on main.py

The complete program will run automatically

Output images will be created in Output folder
An OUTPUT_FILE.txt will be created to store the read files and the data
The detected license Plate will be stored in Identified_LIcense_Plates_Images folder


NOTE:- The program will some extra time to run for the first time
NOTE:- In OUTPUT_FILE.txt the data will be appended
		But in the folders the images will be overwritten if the program is run again

################

A project by->

Aman Verma

Jaywardhan Patil

Aniket Tiwari	

Shubham Pandit	
