# This program checks if user's input is valid using a given deterministic finite automaton
# Automaton is read from an given input file and the output is printed to the console
# This program is written by Pavlidis Pavlos for a task at Theory of Calculation and Automaton course, November 2018


from __future__ import print_function

import sys


def readfile():
    # This function reads the data from the input file and stores them
    # inputs : -
    # output : returns file's data

    file = sys.argv[1]
    with open(file, 'r') as f:
        number_of_statements = f.readline().rstrip('\n')
        initial_statements = f.readline().rstrip('\n')
        number_of_final_statements = f.readline().rstrip('\n')
        final_statements = [int(x) for x in f.readline().split()]
        number_of_arrows = f.readline().rstrip('\n')

        lines = []
        for line in f:  # read rest of lines
            lines.append([x for x in line.split()])

        node_names = set([])
        for inner in lines:
            node_names.add(inner[0])

        for inner in node_names:
            possibleMoves[inner] = []

        for inner in lines:
            possibleMoves[inner[0]].append([inner[1], inner[2]])

        return number_of_statements, initial_statements, number_of_final_statements, final_statements, number_of_arrows, node_names


def validate_input(input_letters, initial_statements, final_statements, possible_moves):
    # This function check if user's input will lead him to a final node or not
    # inputs :
    # input_letters : user's input
    # initial_statements : the initial state of our automaton
    # final_statements : if user's input lead him to one of this nodes, then his input is valid
    # possible_moves : All possible moves in our automaton (all arrows)
    # output : returns false if user's input is invalid

    currentPosition = initial_statements

    for letter in input_letters:

        validLetter = False;
        for moves in possible_moves[currentPosition]:
            # if there is a possible move from current position for this input letter
            if letter == moves[0]:
                currentPosition = moves[1]
                validLetter = True

        if not validLetter:
            return False

    # check if user's input lead him to a node that belongs to finalState
    for finalState in final_statements:
        if finalState == int(currentPosition):
            return True

    return False


if __name__ == "__main__":
    possibleMoves = {}

    numberOfStatements, initialStatements, numberOfFinalStatements, finalStatements, numberOfArrows, nodeNames = readfile()
    input_letters = []

    while True:
        inputText = ""
        chooseOption = input('Press 1 if you want to input a string or 2 if you want to input characters one at a '
                             'time. If you want to exit please press enter: ')

        if chooseOption == "":
            break

        if chooseOption == '1':
            inputText = input('Enter a character or a string. If you want to exit please press enter: ')
            if inputText == "":
                break

        elif chooseOption == '2':
            print("Hit enter without any letter to finish character input: ")
            while True:
                tempInput = input('')
                if tempInput == "":
                    break
                inputText = inputText + tempInput
        else:
            print("You gave invalid input. Please try again!!! ")
            continue

        if len(inputText) > 0:
            inputLetters = [x for x in inputText]
            if not (validate_input(inputLetters, initialStatements, finalStatements, possibleMoves)):
                print("Invalid input \n")
            else:
                print("Valid input \n")

    print("Program has been terminated")
