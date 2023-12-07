import random
import math
import csv

size = 20
turn = 0
coin = 16
emptyBuilding = "   "
gridList = []
rowList = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
columnList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
highscorefile = "Highscore.csv"
validation = True
score = 0

buildingList = ["R", "I", "C", "O", "*"]


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


def adjacentValidation(locationIndex, validation, size, turn, gridList):
    # Define variable
    multiples = []

    # Right side
    print(gridList)
    print(gridList[locationIndex])
    if locationIndex < size ** 2:

        if gridList[locationIndex] != emptyBuilding:

            for b in range(size - 1, size ** 2, size):
                multiples.append(b)

            # Check if location at right border
            if locationIndex - 1 not in multiples:
                validation = True
                return validation

            multiples.clear()

    # Left side
    if locationIndex > 0:

        if gridList[locationIndex - 2] != emptyBuilding:

            for c in range(0, size ** 2, size):
                multiples.append(c)

            # Check if location at left border
            if locationIndex - 1 not in multiples:
                validation = True
                return validation

            multiples.clear()

    # Up
    # Check if location at up border
    if locationIndex - 1 - size >= 0:

        if gridList[locationIndex - 1 - size] != emptyBuilding:
            validation = True
            return validation
    # Down
    # Check if location at up border
    if locationIndex - 1 + size < size ** 2:

        if gridList[locationIndex - 1 + size] != emptyBuilding:
            validation = True
            return validation

    if turn > 1 and (gridList[locationIndex - 1] == emptyBuilding or gridList[locationIndex + 1] == emptyBuilding or gridList[locationIndex - 1 + size] == emptyBuilding or gridList[locationIndex - 1 - size] == emptyBuilding):
        validation = False
        print("You must build next to an existing building.")

    return validation


def calculateScores(size, turn, gridList, score):
    # Use the same adjacency check from AdjacentValidation
    # Define variable
    # Will define if adjacent side is near a corner
    adjacent = [emptyBuilding, emptyBuilding, emptyBuilding, emptyBuilding]
    multiples = []
    residentialScore = 0
    residentialScoreList = []
    industrialScore = 0
    industrialScoreList = []
    commercialScore = 0
    commercialScoreList = []
    parkScore = 0
    parkScoreList = []
    roadScore = 0
    roadScoreList = []

    # Loop for each element in gridList
    for index in range(len(gridList)):

        # Right side
        if index + 1 < size ** 2:

            for b in range(size - 1, size ** 2, size):
                multiples.append(b)

            # Check if location at right border
            if index not in multiples:
                adjacent[0] = gridList[index + 1]

            else:
                adjacent[0] = "COR"

            multiples.clear()

        # Left side
        if index >= 0:

            for c in range(0, size ** 2, size):
                multiples.append(c)

            # Check if location at left border
            if index not in multiples:

                adjacent[1] = gridList[index - 1]

            else:
                adjacent[1] = "COR"

            multiples.clear()

        # Up
        # Check if location at up border
        if index - size > 0:

            adjacent[2] = gridList[index - size]

        else:
            adjacent[2] = "COR"

        # Down
        # Check if location at up border
        if index + size < size ** 2:

            adjacent[3] = gridList[index + size]

        else:
            adjacent[3] = "COR"

        # Calculate point for beach
        if gridList[index] == "R":

            '''if adjacent[0] == "COR" or adjacent[1] == "COR":
                residentialScore += 3

            else:
                residentialScore += 1

            beachScoreList.append(beachScore)
            beachScore = 0'''

            residentialScore = 0

        # Calculate point for factories
        if gridList[index] == "I":

            '''industrialScoreList.append(1)

            if len(industrialScoreList) <= 4:

                for x in range(len(industrialScoreList)):
                    industrialScoreList[x] = len(industrialScoreList)'''
            industrialScore = 0

        # Calculate points for houses
        if gridList[index] == "C":

            '''for x in adjacent:

                if x == "FAC":
                    houseScore = 1
                    break

                elif x == "HSE" or x == "SHP":
                    houseScore += 1

                elif x == "BCH":
                    houseScore += 2

                else:
                    continue

            houseScoreList.append(houseScore)
            houseScore = 0'''
            commercialScore = 0

        if gridList[index] == "O":
            '''variable.clear()

            for x in adjacent:

                if adjacent.count(x) > 1 and x != "COR" and x != emptyBuilding:

                    if variable.count(x) == 0:
                        variable.append(x)
                        shopScore += 1

                    else:
                        continue

                elif x == "COR" or x == emptyBuilding:
                    continue

                else:
                    shopScore += 1

            shopScoreList.append(shopScore)
            shopScore = 0'''
            parkScore = 0

        # Calculate points for Highway
        if gridList[index] == "*":
            '''number = 0

            highwayScoreList.append(1)

            if gridList[index - 1] == "HWY":

                if adjacent[0] == "COR" or adjacent[1] == "COR":
                    continue

                else:
                    number = highwayScoreList[-2] + 1

                    for x in range(highwayScoreList[-2] + 1):
                        highwayScoreList[-x] = number'''
            roadScore = 0

    # Total Score
    score = residentialScore + industrialScore + \
        commercialScore + parkScore + roadScore
    return score


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
            print('Not implemented.')

        # Show highscores
        elif playerChoice == "3":
            print('Not implemented.')

        # Check the input the player has put in
        # Check if the player starts a new game
        elif playerChoice == "1":
            turn = 0
            gridList = []

            # Create an element for each tile in map in gridList
            for x in range(size ** 2):
                gridList.append(emptyBuilding)

            break

        else:
            print("Please input another value.")

    # Loop Turns until player wants to stop or Game Ends
    while True:

        # Print turn number
        if playerChoice == "1" or playerChoice == "2":  # or playerChoice == "Freebuild":
            turn += 1
        print("\nTurn", turn)

        # End of game Sequence
        if turn == size ** 2 + 1:

            # Print final message
            print("\nFinal layout of Ngee Ann City: ")

            # Create Map
            createMap(size, gridList)

            break

        # Print the map
        print("Coins: " + str(coin))
        print("Current score: " + str(calculateScores(size, turn, gridList, score)))
        createMap(size, gridList)

        # Create the randomiser for the houses
        if playerChoice == "1" or playerChoice == "2":  # or playerChoice == "Freebuild":
            randint1 = random.randint(0, len(buildingList) - 1)
            randint2 = random.randint(0, len(buildingList) - 1)

            building1 = buildingList[randint1]
            building2 = buildingList[randint2]

        # Print the instructions
        print("1. Build a {:1s}\
             \n2. Build a {:1s}\
             \n3. Save game\
             \n0. Exit to main menu".format(building1, building2))

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
                    location[0]) + 1) + ((int(location[1]) - 2) + (int(location[2]) - 1) * size)
            print(locationIndex)
            # Validate placement
            # If location is adjacent.
            validation = adjacentValidation(
                locationIndex, validation, size, turn, gridList)

            # If location is occupied
            if gridList[locationIndex - 1] != emptyBuilding:
                print("This location is already occupied.")
                validation = False

            while validation == False:
                location = input("Where do you want to build a building? ")
                locationIndex = (rowList.index(
                    location[0]) + 1) + ((int(location[1]) - 2) + (int(location[2]) - 1) * size)
                validation = adjacentValidation(
                    locationIndex, validation, size, turn, gridList)

                if gridList[locationIndex - 1] != emptyBuilding:
                    print("This location is already occupied.")
                    validation = False
                    continue

            # Place the building on mapGrid
            gridList[locationIndex - 1] = building1

        # Save the game
        elif playerChoice == "3":
            print("Not implemented.")

        # Exit to main menu
        elif playerChoice == "0":
            print("-------------------------")
            print(" Returning to main menu! ")
            print("-------------------------")
            break

         # For input validation
        else:
            print("Please enter a valid input.")
