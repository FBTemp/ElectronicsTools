# imports
import time as t

#variables
settings = open("settings.txt","r")
print(settings.read())

# variables
IN = "OUI OUI BAGUETTE"

# functions
def readSettings(line):
    print()
def skip_line(amount):
    for x in range(int(amount)):
        print()
def sleep(time):
    t.sleep(int(time))
def stop():
    print("Stopping program...")
    sleep(3)
    exit()

# main code
print("Starting ElectronicsTools...")
sleep(3)
IN = input("Press enter to start, press any key and enter to stop. ")
if IN != "":
    stop()
print("hello")