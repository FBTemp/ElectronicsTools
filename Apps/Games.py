import subprocess as sp
import os

print("Welcome to ElectronicsTools Games! Here, you may find various games to cure your boredom while waiting for that new Arduino board to arrive.")

#get all of the games
games_path = "AppFiles/Games"
files = [f for f in os.listdir(games_path) if os.path.isfile(os.path.join(games_path, f))]
files.sort() #sort files alphabetically

#make game names more readable by replacing "_" with " " and removing ".py" extension from each file name
games = [game.replace(".py", "") for game in files]
games = [game.replace("_", " ") for game in games]

#main loop
exit = False
while not exit:
    print("Choose an app:")
    for i, game in enumerate(games): #prints all of the apps with their numbers
        print("\33[0;49;94m" + str(i+1) + " = " + game)
    print("X = exit\033[m")
    choice = input("Your choice: ")
    if choice.isdigit() and int(choice) <= len(games): #if the input is a number between 1 and the number of apps
        game = files[int(choice) - 1] #get the app name from the files list
        print("\nRunning \33[1;49;94m" + game + "\033[m...")
        sp.run(["python", "AppFiles/Games/" + game]) #run the game
    elif choice == "X":
        exit = True