"""
Resistor Calculator App
Made for ElectronicsTools.
Made by: Fast-Blast

ElectronicsTools:
https://github.com/FBTemp/ElectronicsTools
Fast-Blast:
https://linktr.ee/fast_blast

©2025 Fast-Blast. All rights reserved.
"""

# Display the calculator name
def printe(text):
    print("\33[1;49;33mResistor Calculator: \033[m" + text)
def inpute(text):
    return input("\33[1;49;33mResistor Calculator: \033[m" + text)

def color_code_calculator():
    # Display the calculator name
    printe("Color Code Calculator")
    
    # Ask the user to enter the number of bands in the resistor
    bands = inpute("Enter the number of bands in the color code (3/4): ")
    
    # If the resistor has 3 bands
    if int(bands) == 3:
        # Display available colors for band 1, 2, and 3
        printe("Available colors: black=1, brown=2, red=3, orange=4, yellow=5, green=6, blue=7, violet=8, grey=9, white=10.")
        printe("Color 3 also has gold=11 and silver=12.")
        
        # Ask the user to enter the color codes for band 1, 2, and 3
        color1 = int(inpute("Enter the color code for band 1: "))
        color2 = int(inpute("Enter the color code for band 2: "))
        color3 = int(inpute("Enter the color code for band 3: "))

        # Multiplier for band 3 numbers 11 and 12
        if color3 == 11:
            color3 = -1
        elif color3 == 12:
            color3 = -2
        
        # Calculate the resistance value and display it with a tolerance of 20%
        printe(str(((color1-1)*10+(color2-1))*(10**(color3-1))) + " Ω   ±20%")
    
    # If the resistor has 4 bands
    elif int(bands) == 4:
        # Display available colors for band 1, 2, 3, and 4
        printe("Available colors: black=1, brown=2, red=3, orange=4, yellow=5, green=6, blue=7, violet=8, grey=9, white=10.")
        printe("Band 3 also has gold=11 and silver=12.")
        printe("Band 4 only has brown=1, red=2, orange=3, yellow=4, green=5, blue=6, violet=7, grey=8, gold=9, silver=10.")
        
        # Ask the user to enter the color codes for band 1, 2, 3, and 4
        color1 = int(inpute("Enter the color code for band 1: "))
        color2 = int(inpute("Enter the color code for band 2: "))
        color3 = int(inpute("Enter the color code for band 3: "))
        color4 = int(inpute("Enter the color code for band 4: "))

        # Multiplier for band 3 numbers 11 and 12
        if color3 == 11:
            color3 = -1
        elif color3 == 12:
            color3 = -2
        
        # Map color codes to their corresponding tolerance values
        if color4 == 1:
            color4 = "1% (F)"
        elif color4 == 2:
            color4 = "2% (G)"
        elif color4 == 3:
            color4 = "0.05% (W)"
        elif color4 == 4:
            color4 = "0.02% (P)"
        elif color4 == 5:
            color4 = "0.5% (D)"
        elif color4 == 6:
            color4 = "0.25% (C)"
        elif color4 == 7:
            color4 = "0.1% (B)"
        elif color4 == 8:
            color4 = "0.01% (L)"
        elif color4 == 9:
            color4 = "5% (J)"
        elif color4 == 10:
            color4 = "10% (K)"
        
        # Calculate the resistance value and display it with the corresponding tolerance
        printe(str(((color1-1)*10+(color2-1))*(10**(color3-1))) + " Ω   ±" + str(color4))
def parallel_resistance_calculator():
    # Display the calculator name
    printe("Parallel Resistance Calculator")

    # Get inpute for the first resistor
    res1 = int(inpute("Enter the resistance of resistor 1 (in Ω): "))

    # Get inpute for the second resistor
    res2 = int(inpute("Enter the resistance of resistor 2 (in Ω): "))

    # Calculate and display the parallel resistance
    printe("Parallel resistance: " + str((res1*res2)/(res1+res2)) + "Ω")
def series_resistance_calculator():
    # Initialize an empty list to store resistance values
    SI = []
    # Initialize inpute variable
    inpt = ""
    printe("Series Resistance Calculator")
    # Loop until user inputs 'X'
    while inpt != "X":
        # Prompt user for inpute
        inpt = inpute("inpute resistance values one by one (in Ω), submit \"X\" to finish: ")
        # If inpute is not 'X', add it to the list
        if inpt != "X":
            SI.append(int(inpt))
    # Calculate and printe total resistance
    printe("Total resistance: " + str(sum(SI)) + "Ω")

printe("Setting up the resistor calculator...")
exit = False
while not exit:
    printe("Modes:\n            1 = Color Code Calculator\n            2 = Parallel Resistance Calculator\n            3 = Series Resistance Calculator\n            X = Exit")
    mode = inpute("Enter your choice: ")
    if mode == "1":
        color_code_calculator()
    elif mode == "2":
        parallel_resistance_calculator()
    elif mode == "3":
        series_resistance_calculator()
    elif mode == "X":
        exit = True
        printe("Exiting resistor calculator...")
