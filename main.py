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
import os


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
operating_system = os.name
print("Starting ElectronicsTools...") #tells user that the code is running
debug = readSettings(12) #reads settings.txt row 12
if debug == "1": #sets debug mode on
    debug = True
    print("\33[0;49;33mDebug mode on.")
    print(f"The operating system is: {operating_system}\033[m")
elif debug == "0": #sets debug mode off
    debug = False
else: #signals mistake in settings.txt on row 12
    print("\33[7;49;31mSettings file error.")
    print("settings.txt")
    print("Row 12")
    print("Read: \"" + debug + "\"\033[m")
sleep(3)

#input test
if not debug:
    IN = input("Press enter to start, press any key and enter to stop. ")
    if IN != "":
        stop()

#get all of the apps
apps_path = "Apps"
files = [f for f in os.listdir(apps_path) if os.path.isfile(os.path.join(apps_path, f))]
files.sort() #sort files alphabetically

#make app names more readable by replacing "_" with " " and removing ".py" extension from each file name
apps = [app.replace(".py", "") for app in files]
apps = [app.replace("_", " ") for app in apps]

#debug information
if debug:
    print("\33[0;49;33mFiles: " + str(files))
    print("Apps: " + str(apps))
    print("# of apps: " + str(len(apps)) + "\033[m")


#main loop
exit = False
while not exit:
    print("Choose an app:")
    for i, app in enumerate(apps): #prints all of the apps with their numbers
        print("\33[0;49;94m" + str(i+1) + " = " + app)
    print("X = exit\033[m")
    choice = input("Your choice: ")
    if choice.isdigit() and int(choice) <= len(apps): #if the input is a number between 1 and the number of apps
        app = files[int(choice) - 1] #get the app name from the files list
        print("\nRunning \33[1;49;94m" + app + "\033[m...")
        sleep(1)
        if operating_system == "posix": #unix-based systems
            sp.run(["python3", "Apps/" + app]) #run the app
        else: #windows-based systems
            sp.run(["python", "Apps/" + app]) #run the app
    elif choice == "X":
        exit = True

#exit the program
stop()
