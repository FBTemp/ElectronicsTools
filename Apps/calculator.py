import time as t

print("Running Calculator...")
t.sleep(2)
print("Calculator is running.")
t.sleep(3)
exit = False #set exit to false to start the loop again
while exit == False:
    print("Calculator Menu:")
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("X = Exit")
    IN = input("Enter your choice: ")
    if IN == "1":
        print("Addition...")
        t.sleep(2)
        print("Result: " + str(float(input("Enter first number: ")) + float(input("Enter second number: "))))
        t.sleep(3)
    elif IN == "2":
        print("Subtraction...")
        t.sleep(2)
        print("Result: " + str(float(input("Enter first number: ")) - float(input("Enter second number: "))))
        t.sleep(3)
    elif IN == "3":
        print("Multiplication...")
        t.sleep(2)
        print("Result: " + str(float(input("Enter first number: ")) * float(input("Enter second number: "))))
        t.sleep(3)
    elif IN == "4":
        print("Division...")
        t.sleep(2)
        print("Result: " + str(float(input("Enter first number: ")) / float(input("Enter second number: "))))
        t.sleep(3)
    elif IN == "X":
        exit = True
        print("Exiting Calculator...")
        t.sleep(2)