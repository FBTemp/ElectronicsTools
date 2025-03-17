#imports
import random as rd
import time as t

# initialise list of winning messages
win = ["You win!", "Congratulations!", "Great job!", "You did great!", "Nice work!", "You're a winner!", "You did it!", "You're amazing!", "You're unstoppable!", "You're a true champion!", "Spectacular!"]

# generates a random color for text
def RandomColors(text, weight):
    # if you are reading this, you have to make this code prettier

    # initialise color lists
    R = ["\33[0;49;31m", "\33[1;49;31m", "\33[2;49;31m", "\33[3;49;31m", "\33[4;49;31m", "\33[5;49;31m", "\33[6;49;31m", "\33[7;49;31m"]
    G = ["\33[0;49;32m", "\33[1;49;32m", "\33[2;49;32m", "\33[3;49;32m", "\33[4;49;32m", "\33[5;49;32m", "\33[6;49;32m", "\33[7;49;32m"]
    Y = ["\33[0;49;33m", "\33[1;49;33m", "\33[2;49;33m", "\33[3;49;33m", "\33[4;49;33m", "\33[5;49;33m", "\33[6;49;33m", "\33[7;49;33m"]
    N = ["\33[0;49;34m", "\33[1;49;34m", "\33[2;49;34m", "\33[3;49;34m", "\33[4;49;34m", "\33[5;49;34m", "\33[6;49;34m", "\33[7;49;34m"]
    P = ["\33[0;49;36m", "\33[1;49;36m", "\33[2;49;36m", "\33[3;49;36m", "\33[4;49;36m", "\33[5;49;36m", "\33[6;49;36m", "\33[7;49;36m"]
    C = ["\33[0;49;37m", "\33[1;49;37m", "\33[2;49;37m", "\33[3;49;37m", "\33[4;49;37m", "\33[5;49;37m", "\33[6;49;37m", "\33[7;49;37m"]

    # initialise variables
    OUT = []
    txt = list(text)
    y = 0

    # add random color to each character in the text
    for x in range(len(txt)):
        random = rd.randint(0, 5)
        if random == 0:
            OUT.append(R[weight] + txt[y])
        elif random == 1:
            OUT.append(G[weight] + txt[y])
        elif random == 2:
            OUT.append(Y[weight] + txt[y])
        elif random == 3:
            OUT.append(N[weight] + txt[y])
        elif random == 4:
            OUT.append(P[weight] + txt[y])
        elif random == 5:
            OUT.append(C[weight] + txt[y])
        y += 1

    # joins and returns the output
    return ''.join(OUT) + "\033[0m"

# prints the name of the program in random colors
print(RandomColors("Guess the number!", 1))

# get max and min numbers
min = input(RandomColors("Enter the minimum number (R for random): ", 0))
max = input(RandomColors("Enter the maximum number (R for random): ", 0))

# check if the user wants a random number
if min == 'r' or min == 'R':
    min = rd.randint(1, 100)
if max == 'r' or max == 'R':
    max = rd.randint(min, 100)

# make sure that min and max are integers
min = int(min)
max = int(max)

# print the range

# generate a random number between min and max
print(RandomColors("Generating a random number between " + str(min) + " and " + str(max) + "...", 0))
number = rd.randint(min, max)
t.sleep(1)

# guess the number
guess = 0
while guess != number:
    guess = int(input(RandomColors("Guess the number: ", 0)))
    if guess > number: # if the guess is too high
        print(RandomColors("Too high!", 0))
    elif guess < number: # if the guess is too low
        print(RandomColors("Too low!", 0))

# print a random winning message
message = rd.choice(win)
for i in range(20):
    print(RandomColors(message, 7))
    t.sleep(0.1)