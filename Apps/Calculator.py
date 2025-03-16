"""
Calculator App
Made for ElectronicsTools.
Made by: Fast-Blast

ElectronicsTools:
https://github.com/FBTemp/ElectronicsTools
Fast-Blast:
https://linktr.ee/fast_blast

©2025 Fast-Blast. All rights reserved.
"""

# tells the user that they outputs and inputs are from the calculator app
def printe(text):
    print("\33[1;49;32mCalculator: \033[m" + text)
def inpute(text):
    return input("\33[1;49;32mCalculator: \033[m" + text)

# main program
printe("Running Calculator...")
exit = False #set exit to false to start the loop again
while not exit:
    # print calculator menu options:
    printe("Calculator Menu:\n            1 = Addition\n            2 = Subtraction\n            3 = Multiplication\n            4 = Division\n            X = Exit")
    IN = inpute("Enter your choice: ")
    # addition mode
    if IN == "1":
        printe("Addition...")
        printe("Result: " + str(float(inpute("Enter first number: ")) + float(inpute("Enter second number: "))))
    # subtraction mode
    elif IN == "2":
        printe("Subtraction...")
        printe("Result: " + str(float(inpute("Enter first number: ")) - float(inpute("Enter second number: "))))
    # multiplication mode
    elif IN == "3":
        printe("Multiplication...")
        printe("Result: " + str(float(inpute("Enter first number: ")) * float(inpute("Enter second number: "))))
    # division mode
    elif IN == "4":
        printe("Division...")
        printe("Result: " + str(float(inpute("Enter first number: ")) / float(inpute("Enter second number: "))))
    # exit calculator app
    elif IN == "X":
        exit = True
        printe("Exiting Calculator...")