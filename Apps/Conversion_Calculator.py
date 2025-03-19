"""
    WARNING: This app is currently giving wrong answers, will have to fix ratios by hand.

    Time wasted so far:
    18 minutes
    Continue at:
    Row 74
"""

def temperature_converter():
    # Display temperature conversion options
    print("Temperature Converter")
    print("1 = Celsius, 2 = Fahrenheit, 3 = Kelvin")

    fromUnit = int(input("From (unit): "))
    toUnit = int(input("To (unit): "))
    fromTemp = int(input("Temperature: "))

    # Convert from Celsius
    if fromUnit == 1:
        if toUnit == 2:
            result = (fromTemp * 9/5) + 32
            print("It is " + str(result) + "°F")
        elif toUnit == 3:
            result = fromTemp + 273.15
            print("It is " + str(result) + "°K")

    # Convert from Fahrenheit
    elif fromUnit == 2:
        if toUnit == 1:
            result = (fromTemp - 32) * 5/9
            print("It is " + str(result) + "°C")
        elif toUnit == 3:
            result = (fromTemp - 32) * 5/9 + 273.15
            print("It is " + str(result) + "°K")

    # Convert from Kelvin
    elif fromUnit == 3:
        if toUnit == 1:
            result = fromTemp - 273.15
            print("It is " + str(result) + "°C")
        elif toUnit == 2:
            result = (fromTemp - 273.15) * 9/5 + 32
            print("It is " + str(result) + "°F")
def length_converter():
    # works like temperature_converter but for length
    print("Length Converter")
    print("1 = Millimeters, 2 = Centimeters, 3 = Meters, 4 = Kilometers, 5 = Inches, 6 = Feet, 7 = Yards, 8 = Miles")
    fromUnit = int(input("From (unit): "))
    toUnit = int(input("To (unit): "))
    fromDist = int(input("Distance: "))
    if fromUnit == 1:
        if toUnit == 2:
            result = fromDist / 10
            print("Distance is " + str(result) + "cm")
        elif toUnit == 3:
            result = fromDist / 1000
            print("Distance is " + str(result) + "m")
        elif toUnit == 4:
            result = fromDist / 1000000
            print("Distance is " + str(result) + "km")
        elif toUnit == 5:
            result = fromDist / 25.4
            print("Distance is " + str(result) + "in")
        elif toUnit == 6:
            result = fromDist * 0.0032808399
            print("Distance is " + str(result) + "ft")
        elif toUnit == 7:
            result = fromDist * 0.0010936133
            print("Distance is " + str(result) + "yd")
        elif toUnit == 8:
            result = fromDist / 160934.4
            print("Distance is " + str(result) + "mi")
    elif fromUnit == 2:
        if toUnit == 1:
            result = fromDist * 10
            print("Distance is " + str(result) + "mm")
        elif toUnit == 3:
            result = fromDist / 100
            print("Distance is " + str(result) + "m")
        elif toUnit == 4:
            result = fromDist / 1000
            print("Distance is " + str(result) + "km")
        elif toUnit == 5:
            result = fromDist / 2.54
            print("Distance is " + str(result) + "in")
        elif toUnit == 6:
            result = fromDist / 3.28084
            print("Distance is " + str(result) + "ft")
        elif toUnit == 7:
            result = fromDist / 1.09361
            print("Distance is " + str(result) + "yd")
        elif toUnit == 8:
            result = fromDist / 1.60934
            print("Distance is " + str(result) + "mi")
    elif fromUnit == 3:
        if toUnit == 1:
            result = fromDist * 1000
            print("Distance is " + str(result) + "mm")
        elif toUnit == 2:
            result = fromDist * 100
            print("Distance is " + str(result) + "cm")
        elif toUnit == 4:
            result = fromDist
            print("Distance is " + str(result) + "km")
        elif toUnit == 5:
            result = fromDist / 0.0254
            print("Distance is " + str(result) + "in")
        elif toUnit == 6:
            result = fromDist * 3.28084
            print("Distance is " + str(result) + "ft")
        elif toUnit == 7:
            result = fromDist * 1.09361
            print("Distance is " + str(result) + "yd")
        elif toUnit == 8:
            result = fromDist / 1.60934
            print("Distance is " + str(result) + "mi")
    elif fromUnit == 4:
        if toUnit == 1:
            result = fromDist * 1000000
            print("Distance is " + str(result) + "mm")
        elif toUnit == 2:
            result = fromDist * 100000
            print("Distance is " + str(result) + "cm")
        elif toUnit == 3:
            result = fromDist / 1000
            print("Distance is " + str(result) + "m")
        elif toUnit == 5:
            result = fromDist / 0.0254
            print("Distance is " + str(result) + "in")
        elif toUnit == 6:
            result = fromDist * 39370.1
            print("Distance is " + str(result) + "ft")
        elif toUnit == 7:
            result = fromDist * 116079.2
            print("Distance is " + str(result) + "yd")
        elif toUnit == 8:
            result = fromDist / 160934.4
            print("Distance is " + str(result) + "mi")
    elif fromUnit == 5:
        if toUnit == 1:
            result = fromDist * 25.4
            print("Distance is " + str(result) + "mm")
        elif toUnit == 2:
            result = fromDist / 2.54
            print("Distance is " + str(result) + "cm")
        elif toUnit == 3:
            result = fromDist * 0.0254
            print("Distance is " + str(result) + "m")
        elif toUnit == 4:
            result = fromDist * 0.0000254
            print("Distance is " + str(result) + "km")
        elif toUnit == 6:
            result = fromDist / 0.393701
            print("Distance is " + str(result) + "ft")
        elif toUnit == 7:
            result = fromDist * 0.000568181
            print("Distance is " + str(result) + "yd")
        elif toUnit == 8:
            result = fromDist * 0.000000621371
            print("Distance is " + str(result) + "mi")
    elif fromUnit == 6:
        if toUnit == 1:
            result = fromDist * 39.3701
            print("Distance is " + str(result) + "mm")
        elif toUnit == 2:
            result = fromDist / 0.3048
            print("Distance is " + str(result) + "cm")
        elif toUnit == 3:
            result = fromDist / 3.28084
            print("Distance is " + str(result) + "m")
        elif toUnit == 4:
            result = fromDist * 0.0003048
            print("Distance is " + str(result) + "km")
        elif toUnit == 5:
            result = fromDist / 0.0254
            print("Distance is " + str(result) + "in")
        elif toUnit == 7:
            result = fromDist / 0.333333
            print("Distance is " + str(result) + "yd")
        elif toUnit == 8:
            result = fromDist / 0.000568181
            print("Distance is " + str(result) + "mi")
    elif fromUnit == 7:
        if toUnit == 1:
            result = fromDist * 1760
            print("Distance is " + str(result) + "mm")
        elif toUnit == 2:
            result = fromDist / 0.9144
            print("Distance is " + str(result) + "cm")
        elif toUnit == 3:
            result = fromDist / 1.09361
            print("Distance is " + str(result) + "m")
        elif toUnit == 4:
            result = fromDist * 0.00176
            print("Distance is " + str(result) + "km")
        elif toUnit == 5:
            result = fromDist / 2.54
            print("Distance is " + str(result) + "in")
        elif toUnit == 6:
            result = fromDist / 0.000568181
            print("Distance is " + str(result) + "ft")
        elif toUnit == 8:
            result = fromDist / 0.0000160934
            print("Distance is " + str(result) + "mi")
    elif fromUnit == 8:
        if toUnit == 1:
            result = fromDist * 160934.4
            print("Distance is " + str(result) + "mm")
        elif toUnit == 2:
            result = fromDist / 1000
            print("Distance is " + str(result) + "cm")
        elif toUnit == 3:
            result = fromDist / 1.60934
            print("Distance is " + str(result) + "m")
        elif toUnit == 4:
            result = fromDist * 0.001
            print("Distance is " + str(result) + "km")
        elif toUnit == 5:
            result = fromDist * 0.393701
            print("Distance is " + str(result) + "in")
        elif toUnit == 6:
            result = fromDist * 5280
            print("Distance is " + str(result) + "ft")
        elif toUnit == 7:
            result = fromDist * 1760
            print("Distance is " + str(result) + "yd")
def weight_converter():
    # works the same way as length_converter, but for weight
    print("Weight Converter")
    print("1 = Milligram, 2 = Gram, 3 = Kilogram, 4 = Pound, 5 = Ounce")
    fromUnit = int(input("From (unit): "))
    toUnit = int(input("To (unit): "))
    fromWegt = int(input("Weight: "))
    if fromUnit == 1:
        if toUnit == 2:
            result = fromWegt / 1000
            print("Weight is " + str(result) + "g")
        elif toUnit == 3:
            result = fromWegt / 1000000
            print("Weight is " + str(result) + "kg")
        elif toUnit == 4:
            result = fromWegt / 453.592
            print("Weight is " + str(result) + "lb")
        elif toUnit == 5:
            result = fromWegt / 28.3495
            print("Weight is " + str(result) + "oz")
    elif fromUnit == 2:
        if toUnit == 1:
            result = fromWegt * 1000
            print("Weight is " + str(result) + "mg")
        elif toUnit == 3:
            result = fromWegt / 1000
            print("Weight is " + str(result) + "kg")
        elif toUnit == 4:
            result = fromWegt / 453.592
            print("Weight is " + str(result) + "lb")
        elif toUnit == 5:
            result = fromWegt / 28.3495
            print("Weight is " + str(result) + "oz")
    elif fromUnit == 3:
        if toUnit == 1:
            result = fromWegt * 1000000
            print("Weight is " + str(result) + "mg")
        elif toUnit == 2:
            result = fromWegt * 1000
            print("Weight is " + str(result) + "g")
        elif toUnit == 4:
            result = fromWegt / 0.453592
            print("Weight is " + str(result) + "lb")
        elif toUnit == 5:
            result = fromWegt / 0.035274
            print("Weight is " + str(result) + "oz")
    elif fromUnit == 4:
        if toUnit == 1:
            result = fromWegt * 453.592
            print("Weight is " + str(result) + "mg")
        elif toUnit == 2:
            result = fromWegt * 1000
            print("Weight is " + str(result) + "g")
        elif toUnit == 3:
            result = fromWegt / 2.20462
            print("Weight is " + str(result) + "kg")
        elif toUnit == 5:
            result = fromWegt * 16
            print("Weight is " + str(result) + "oz")
    elif fromUnit == 5:
        if toUnit == 1:
            result = fromWegt * 28.3495
            print("Weight is " + str(result) + "mg")
        elif toUnit == 2:
            result = fromWegt * 28.3495
            print("Weight is " + str(result) + "g")
        elif toUnit == 3:
            result = fromWegt / 35.274
            print("Weight is " + str(result) + "kg")
        elif toUnit == 4:
            result = fromWegt / 16
            print("Weight is " + str(result) + "lb")
def volume_converter():
    # works the same way as weight_converter, but for volume
    print("Volume Converter")
    print("1 = Milliliters, 2 = Liters, 3 = Gallons, 4 = Quarts, 5 = Cups")
    fromUnit = int(input("From (unit): "))
    toUnit = int(input("To (unit): "))
    fromVol = int(input("Volume: "))
    if fromUnit == 1:
        if toUnit == 2:
            result = fromVol / 1000
            print("Volume is " + str(result) + "L")
        elif toUnit == 3:
            result = fromVol / 3785.41
            print("Volume is " + str(result) + "G")
        elif toUnit == 4:
            result = fromVol / 1000
            print("Volume is " + str(result) + "qt")
        elif toUnit == 5:
            result = fromVol / 236.588
            print("Volume is " + str(result) + "cups")
    elif fromUnit == 2:
        if toUnit == 1:
            result = fromVol * 1000
            print("Volume is " + str(result) + "ml")
        elif toUnit == 3:
            result = fromVol / 1000
            print("Volume is " + str(result) + "gallons")
        elif toUnit == 4:
            result = fromVol / 33.814
            print("Volume is " + str(result) + "qt")
        elif toUnit == 5:
            result = fromVol / 236.588
            print("Volume is " + str(result) + "cups")
    elif fromUnit == 3:
        if toUnit == 1:
            result = fromVol * 3785.41
            print("Volume is " + str(result) + "ml")
        elif toUnit == 2:
            result = fromVol * 1000
            print("Volume is " + str(result) + "L")
        elif toUnit == 4:
            result = fromVol / 3785.41
            print("Volume is " + str(result) + "qt")
        elif toUnit == 5:
            result = fromVol / 236.588
            print("Volume is " + str(result) + "cups")
    elif fromUnit == 4:
        if toUnit == 1:
            result = fromVol * 946.853
            print("Volume is " + str(result) + "ml")
        elif toUnit == 2:
            result = fromVol * 33.814
            print("Volume is " + str(result) + "L")
        elif toUnit == 3:
            result = fromVol / 3785.41
            print("Volume is " + str(result) + "gallons")
        elif toUnit == 5:
            result = fromVol / 236.588
            print("Volume is " + str(result) + "cups")
    elif fromUnit == 5:
        if toUnit == 1:
            result = fromVol * 236.588
            print("Volume is " + str(result) + "ml")
        elif toUnit == 2:
            result = fromVol * 236.588
            print("Volume is " + str(result) + "L")
        elif toUnit == 3:
            result = fromVol / 3785.41
            print("Volume is " + str(result) + "gallons")
        elif toUnit == 4:
            result = fromVol / 946.853
            print("Volume is " + str(result) + "qt")

# simple selection menu loop
exit = False
while not exit:
    print("Choose what you want to convert:")
    print("1 = Temperature")
    print("2 = Length")
    print("3 = Weight")
    print("4 = Volume")
    print("X = Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        temperature_converter()
    elif choice == "2":
        length_converter()
    elif choice == "3":
        weight_converter()
    elif choice == "4":
        volume_converter()
    elif choice == "X":
        exit = True
        print("Exiting converter...")
