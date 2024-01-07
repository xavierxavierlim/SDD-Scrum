# Library files for importing
import random
import math
import csv

size = 20
turn = 1
coin = 5
emptyBuilding = "   "
gridList = []
highscorefile = "Leaderboards.csv"  # File to store high scores
savefile = "Savefile.txt"  # File to save game
datafile = open(highscorefile, "a")
datafile.close()
rowList = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]  # 20 rows
columnList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]  # 20 columns

validation = True
score = 0

# Residential (R), Industrial (I), Commercial (C), Park (O), Road (*)
buildingList = ["R", "I", "C", "O", "*"]
buildingNameList = ["a Residential", "an Industry",
                    "a Commercial", "a Park", "a Road"]


def createMap(size, gridList):
    # Create List for number of rows and columns
    rowList = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
               "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
    columnList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    index = 0

    # This is the horizontal borders you see in the map
    border_horizontal = "  " + ("+-----" * size) + "+"

    # Lettering for the rows
    rowLetters = " "

    for a in range(size):
        rowLetters += "    {:1s} ".format(rowList[a])

    # Print the rows and columns of the map itself
    print(rowLetters)
    for x in range(size):
        print(border_horizontal)
        print("{:>2}".format(columnList[x]), end="")

        for y in range(size):
            print("| {:^3s} ".format(gridList[index]), end="")
            index += 1

        print("|")

    print(border_horizontal)


def adjacentEmptyValidation(locationIndex, validation, size, turn, gridList):
    # Define variable
    multiples = []

    # Right side

    if locationIndex < size ** 2:

        if gridList[locationIndex] != emptyBuilding:

            for b in range(size - 1, size ** 2, size):
                multiples.append(b)

            # Check if location at right border
            if locationIndex - 1 not in multiples:

                return

            multiples.clear()

    # Left side
    if locationIndex > 0:

        if gridList[locationIndex - 2] != emptyBuilding:

            for c in range(0, size ** 2, size):
                multiples.append(c)

            # Check if location at left border
            if locationIndex - 1 not in multiples:

                return

            multiples.clear()

    # Up
    # Check if location at up border
    if locationIndex - 1 - size >= 0:

        if gridList[locationIndex - 1 - size] != emptyBuilding:

            return
    # Down
    # Check if location at up border
    if locationIndex - 1 + size < size ** 2:

        if gridList[locationIndex - 1 + size] != emptyBuilding:

            return

    count = 0
    for i in range(len(gridList)):
        if gridList[i] == emptyBuilding:
            count += 1

    if (count == size ** 2):
        return

    # Check if location entered is adjacent to an existing building
    if gridList[locationIndex - 1] == emptyBuilding:
        validation = False
        print("You must build next to an existing building.")

    return validation


def calculateScores(size, turn, gridList):
    # Use the same adjacency check from AdjacentValidation
    # Define variable
    # Will define if adjacent side is near a corner
    adjacent = [emptyBuilding, emptyBuilding, emptyBuilding, emptyBuilding]
    multiples = []
    score = 0

    # Loop for each element in gridList
    for index in range(len(gridList)):

        # Right side
        if index + 1 < size ** 2:

            for b in range(size - 1, size ** 2, size):
                multiples.append(b)

            # Check if location at right border
            if index not in multiples:
                adjacent[0] = gridList[index + 1]

            multiples.clear()

        # Left side
        if index >= 0:

            for c in range(0, size ** 2, size):
                multiples.append(c)

            # Check if location at left border
            if index not in multiples:

                adjacent[1] = gridList[index - 1]

            multiples.clear()

        # Up
        # Check if location at up border
        if index - size > 0:

            adjacent[2] = gridList[index - size]

        # Down
        # Check if location at up border
        if index + size < size ** 2:

            adjacent[3] = gridList[index + size]

        # Calculate point for residential by checking the adjacent buildings
        if gridList[index] == "R":
            if adjacent[0] == "I" or adjacent[0] == "R" or adjacent[0] == "C":
                score += 1

            if adjacent[1] == "I" or adjacent[1] == "R" or adjacent[1] == "C":
                score += 1

            if adjacent[2] == "R" or adjacent[2] == "C":
                score += 1

            if adjacent[3] == "R" or adjacent[3] == "C":
                score += 1

            if adjacent[0] == "O":
                score += 1

            if adjacent[1] == "O":
                score += 1

            if adjacent[2] == "O":
                score += 1

            if adjacent[3] == "O":
                score += 1

        # Calculate point for industrial
        elif gridList[index] == "I":
            score += 1

        # Calculate points for commercial by checking the adjacent buildings
        elif gridList[index] == "C":
            if adjacent[0] == "C":
                score += 1

            if adjacent[1] == "C":
                score += 1

            if adjacent[2] == "C":
                score += 1

            if adjacent[3] == "C":
                score += 1

        # Calculate points for park by checking the adjacent buildings
        elif gridList[index] == "O":
            if adjacent[0] == "O":
                score += 1

            if adjacent[1] == "O":
                score += 1

            if adjacent[2] == "O":
                score += 1

            if adjacent[3] == "O":
                score += 1

        # Calculate points for road by checking the adjacent buildings
        elif gridList[index] == "*":
            if adjacent[0] == "*":
                score += 1
            if adjacent[1] == "*":
                score += 1

    return score


def calculateCoins(size, turn, gridList):
    # Use the same adjacency check from AdjacentValidation
    # Define variable
    # Will define if adjacent side is near a corner
    adjacent = [emptyBuilding, emptyBuilding, emptyBuilding, emptyBuilding]
    multiples = []
    coin = 0

    # Loop for each element in gridList
    for index in range(len(gridList)):

        # Right side
        if index + 1 < size ** 2:

            for b in range(size - 1, size ** 2, size):
                multiples.append(b)

            # Check if location at right border
            if index not in multiples:
                adjacent[0] = gridList[index + 1]

            multiples.clear()

        # Left side
        if index >= 0:

            for c in range(0, size ** 2, size):
                multiples.append(c)

            # Check if location at left border
            if index not in multiples:

                adjacent[1] = gridList[index - 1]

            multiples.clear()

        # Up
        # Check if location at up border
        if index - size > 0:

            adjacent[2] = gridList[index - size]

        # Down
        # Check if location at up border
        if index + size < size ** 2:

            adjacent[3] = gridList[index + size]

        # Calculate coin for industrial by checking the adjacent buildings
        if gridList[index] == "I":
            if adjacent[0] == "R":
                coin += 1

            if adjacent[1] == "R":
                coin += 1

            if adjacent[2] == "R":
                coin += 1

            if adjacent[3] == "R":
                coin += 1

        # Calculate points for commercial by checking the adjacent buildings
        elif gridList[index] == "C":
            if adjacent[0] == "R":
                coin += 1

            if adjacent[1] == "R":
                coin += 1

            if adjacent[2] == "R":
                coin += 1

            if adjacent[3] == "R":
                coin += 1

    return coin


def highscores(highscorefile):
    highScoreList = []

    # Display Highscores
    print("\n{:^31}".format(str(size)+" x "+str(size)))
    print("--------- HIGH SCORES ---------\
         \nPos Player                Score\
         \n--- ------                -----")

    # Look through datafiles for highscores
    with open(highscorefile, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            # Check if the value in the first column of the current row is equal to the 'size' variable
            if int(row[0]) == size:
                # Create a list containing values from the second and third columns of the current row
                highScoreLine = [row[1], row[2]]
                highScoreList.append(highScoreLine)

        # Sort from highest to lowest in score
        highScoreList.sort(key=lambda x: x[1], reverse=True)
        file.close()

        # Display the highScores
        for x in range(len(highScoreList)):
            if x < 10:
                print("{:>2}. {:<20}{:>7}".format(
                    str(x+1), str(highScoreList[x][0]), str(highScoreList[x][1])))
            else:
                break


def writeHighscore(highscorefile, size, finalScore):
    highScoreList = []

    # Look through datafiles for highscores
    with open(highscorefile, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            # Check according to size
            # Check if the value in the first column of the current row is equal to the 'size' variable
            if int(row[0]) == size:
                # Create a list containing values from the second and third columns of the current row
                highScoreLine = [row[1], row[2]]
                highScoreList.append(highScoreLine)
        # Sort from highest to lowest in score
        highScoreList.sort(key=lambda x: x[1], reverse=True)
        file.close()

    for x in range(len(highScoreList)):
        # Check if highscore is achieved
        if finalScore >= int(highScoreList[x][1]) and x < 10:
            print("Congratulations! You made the high score board at position {}!".format(
                str(x+1)))
            while True:
                try:
                    name = input("Please enter your name(max 20 chars): ")
                except:
                    print("Please input another name.")
                    continue
                if len(name) > 20:
                    print("Your name is too long, please input another name.")
                    continue
                else:
                    break

            newHighScore = [name, str(finalScore)]
            highScoreList.append(newHighScore)
            # Sort the list in descending order
            highScoreList.sort(key=lambda x: x[1], reverse=True)
            # Update the file with the new highscore
            with open(highscorefile, "a", newline="") as file:
                file.write(str(size)+"\t"+name+"\t"+str(finalScore)+"\n")
                file.close()

            break

    # Check if highScoreList is empty
    if len(highScoreList) == 0:
        print("Congratulations! You made the high score board at position 1!")
        while True:
            try:
                name = input("Please enter your name(max 20 chars): ")
            except:
                print("Please input another name.")
                continue
            if len(name) > 20:
                print("Your name is too long, please input another name.")
                continue
            else:
                break

        newHighScore = [name, str(finalScore)]
        highScoreList.append(newHighScore)
        # Actually start writing to write code into file
        with open(highscorefile, "a", newline="") as file:
            file.write(str(size)+"\t"+name+"\t"+str(finalScore)+"\n")
            file.close()

    # Display the highScores
    # Remove any values if position is above 10
    while len(highScoreList) > 10:
        highScoreList.pop()

    print("--------- HIGH SCORES ---------\
         \nPos Player                Score\
         \n--- ------                -----")
    for x in range(len(highScoreList)):
        print("{:>2}. {:<20}{:>7}".format(
            str(x+1), str(highScoreList[x][0]), str(highScoreList[x][1])))


# Main Menu
print("Welcome, mayor of Ngee Ann City!\
     \n----------------------------")

while True:
    print("\n1. Start new game\
           \n2. Load save game\
           \n3. Show high scores\
           \n\
           \n0. Exit")

    while True:
        # Ask for an input from the player
        playerChoice = input("Your choice? ")

        # quit game
        if playerChoice == "0":
            quit()

        # Load Saved Game
        elif playerChoice == "2":
            try:
                datafile = open(savefile, "r")

                for line in datafile:
                    tempList = line.split("|")

                tempList = [x.strip(' ') for x in tempList]
                size = int(tempList[0])
                turn = int(tempList[1])
                gridList = tempList[2].split(",")
                for x in range(len(gridList)):
                    if gridList[x] == "EMPTY":
                        gridList[x] = "   "

                break
            except:
                print("No such file has been saved yet.")

        # Show highscores
        elif playerChoice == "3":
            highscores(highscorefile)
        # Check the input the player has put in
        # Check if the player starts a new game
        elif playerChoice == "1":
            turn = 1
            gridList = []

            # Create an element for each tile in map in gridList
            for x in range(size ** 2):
                gridList.append(emptyBuilding)

            break

        else:
            print("Please input another value.")

    # Loop Turns until player wants to stop or Game Ends
    while True:
        print("\nTurn", turn)

        # End of game Sequence
        if (all(item is not emptyBuilding for item in gridList) and emptyBuilding not in gridList) or coin <= 0:

            # Print final message
            print("\nFinal layout of Ngee Ann City: ")

            # Create Map
            createMap(size, gridList)

            # Calculate final scores
            finalScore = calculateScores(size, turn, gridList)
            print("Final calculated score: " + str(finalScore))

            # Display HighScores
            writeHighscore(highscorefile, size, finalScore)

            break

        # Print the map
        print("Coins: " + str(coin))
        print("Current score: " + str(score))
        createMap(size, gridList)

        # Create the randomiser for the houses
        if playerChoice == "1" or playerChoice == "2":
            randint1 = random.randint(0, len(buildingList) - 1)
            randint2 = random.randint(0, len(buildingList) - 1)

            building1 = buildingList[randint1]
            building2 = buildingList[randint2]
            building_name1 = buildingNameList[randint1]
            building_name2 = buildingNameList[randint2]

        # Print the instructions
        print("1. Build {:1s}\
             \n2. Build {:1s}\
             \n3. Save game\
             \n4. Destroy building\
             \n0. Exit to main menu".format(building_name1 + " (" + building1 + ")", building_name2 + " (" + building2 + ")"))

        # Ask input from player
        playerChoice = input("Please enter your choice? ")

        # check if player wants to build
        if playerChoice == "1" or playerChoice == "2":
            # Check where to build
            # Input validation
            while True:
                try:
                    location = input("Where do you want to build a building? ")

                except:
                    print("Please enter a valid input.")
                    continue

                if rowList.count(location[0]) == 0:
                    print("Please enter a valid input.")
                    continue

                elif location[1].isnumeric() == False:
                    print("Please enter a valid input.")
                    continue

                elif location[1] == "0":
                    print("Please enter a valid input.")
                    continue

                else:
                    break

            # Translate input to location on map
            if len(location) == 2:
                locationIndex = (rowList.index(
                    location[0]) + 1) + ((int(location[1]) - 1) * size)

            elif len(location) == 3:
                locationIndex = (rowList.index(
                    location[0]) + 1) + ((int(location[1:3]) - 1) * size)

            # Validate placement
            # If location is adjacent.
            validation = adjacentEmptyValidation(
                locationIndex, validation, size, turn, gridList)

            # If location is occupied
            if gridList[locationIndex - 1] != emptyBuilding:
                print("This location is already occupied.")
                validation = False

            while validation == False:
                location = input("Where do you want to build a building? ")
                if len(location) == 2:
                    locationIndex = (rowList.index(
                        location[0]) + 1) + ((int(location[1]) - 1) * size)

                elif len(location) == 3:
                    locationIndex = (rowList.index(
                        location[0]) + 1) + ((int(location[1:3]) - 1) * size)
                validation = adjacentEmptyValidation(
                    locationIndex, validation, size, turn, gridList)

                if gridList[locationIndex - 1] != emptyBuilding:
                    print("This location is already occupied.")
                    validation = False
                    continue

            # Place the building on mapGrid
            if (playerChoice == "1"):
                gridList[locationIndex - 1] = building1

            else:
                gridList[locationIndex - 1] = building2
            score += calculateScores(size, turn, gridList)
            coin += calculateCoins(size, turn, gridList)
            coin -= 1
            turn += 1

        # Save the game
        elif playerChoice == "3":
            # open savefile for writing
            tempVariable = ""
            for x in range(len(gridList)):

                if gridList[x] == emptyBuilding:
                    tempVariable += "EMPTY"

                else:
                    tempVariable += gridList[x]

                if x != len(gridList) - 1:
                    tempVariable += ","

            datafile = open(savefile, "w")

            # Write all necessary save data needed to run game
            datafile.write("{:<1d}|{:<2d}|{:<700s}".format(
                size, turn, tempVariable))
            datafile.close()
            print("Game Saved!")

        elif playerChoice == "4":
            if turn <= 1:
                # Check if there are no buildings built yet
                print("No buildings have been built yet!")
                continue

            else:
                while True:
                    try:
                        location = input(
                            "Where do you want to remove the building? ")
                    # Handle invalid input
                    except:
                        print("Please enter a valid input.")
                        continue
                    # Check if the row input is valid
                    if rowList.count(location[0]) == 0:
                        print("Please enter a valid input.")
                        continue
                    # Check if the column input is numeric
                    elif location[1].isnumeric() == False:
                        print("Please enter a valid input.")
                        continue
                    # Check if the column input is greater than 0
                    elif location[1] == "0":
                        print("Please enter a valid input.")
                        continue

                    else:
                        break

                if len(location) == 2:
                    locationIndex = (rowList.index(
                        location[0]) + 1) + ((int(location[1]) - 1) * size)

                elif len(location) == 3:
                    locationIndex = (rowList.index(
                        location[0]) + 1) + ((int(location[1:3]) - 1) * size)

                validation = True
                count = 0
                for i in range(len(gridList)):
                    if gridList[i] == emptyBuilding:
                        count += 1

                # Check if all the buildings are empty
                if count == size ** 2:
                    print(
                        "No such building anymore can be built. Please build a building first.")
                    continue

                # Check if there is no building to destroy at the specified location
                if gridList[locationIndex - 1] == emptyBuilding:
                    print("There is no building to destroy in this location " +
                          location + ". Please try again.")
                    validation = False

                while validation == False:
                    location = input(
                        "Where do you want to remove the building? ")
                    if len(location) == 2:
                        locationIndex = (rowList.index(
                            location[0]) + 1) + ((int(location[1]) - 1) * size)

                    elif len(location) == 3:
                        locationIndex = (rowList.index(
                            location[0]) + 1) + ((int(location[1:3]) - 1) * size)
                    # Check if there is no building to destroy at the specified location
                    if gridList[locationIndex - 1] == emptyBuilding:
                        print("There is no building to destroy in this location " +
                              location + ". Please try again.")
                        validation = False
                        continue

                    else:
                        validation = True
                # Update the game state after removing a building
                score -= calculateScores(size, turn, gridList)
                gridList[locationIndex - 1] = emptyBuilding
                score += calculateScores(size, turn, gridList)
                coin -= 1
                turn += 1

        # Exit to main menu
        elif playerChoice == "0":
            print("-------------------------")
            print(" Returning to main menu! ")
            print("-------------------------")
            break

         # For input validation
        else:
            print("Please enter a valid input.")
