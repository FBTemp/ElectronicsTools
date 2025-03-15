"""
ElectronicsTools
Made by:
Fast-Blast and other open-source GitHub contributors.

ElectronicsTools:
https://github.com/FBTemp/ElectronicsTools
Fast-Blast:
https://linktr.ee/fast_blast
"""

# imports
import time as t
import subprocess as sp


#variables
settings = open("Config/settings.txt","r")


# variables
IN = ""
debug = ""
choice = ""


# functions
#read  specific line in settings file
def readSettings(line_number):
    settings.seek(0)  #make sure that we are at the beginning
    for _ in range(line_number - 1):
        settings.readline()  #skip the lines we don't need
    output = settings.readline().strip()  #read the line
    return output #returns the lin (0/1)

#skips a set amount of lines
def skip_line(amount):
    for x in range(int(amount)):
        print()

#sleeps only if debug mode is off
def sleep(time):
    if not debug:
        t.sleep(int(time))

#stops program
def stop():
    print("Stopping program...")
    #closing files
    settings.close()
    sleep(3)
    quit() #exit() will stop the program


# main code
#setup
print("Starting ElectronicsTools...") #tells user that the code is running
sleep(1)
debug = readSettings(12) #reads settings.txt row 12
if debug == "1": #sets debug mode on
    debug = True
    print("Debug mode on.")
elif debug == "0": #sets debug mode off
    debug = False
else: #signals mistake in settings.txt on row 12
    print("Settings file error.")
    print("settings.txt")
    print("Row 12")
    print("Read: \"" + debug + "\"")
sleep(2)

#input test
IN = input("Press enter to start, press any key and enter to stop. ")
if IN != "":
    stop()

#enter the while loop
exit = False
while not exit:
    print("Apps:")
    print("1 = Calculator")
    print("X = Exit")
    choice = input("Select an app: ")
    if choice == "1":
        sp.run(["python", "Apps/calculator.py"])
    elif choice == "X":
        exit = True

#exit the program
stop()