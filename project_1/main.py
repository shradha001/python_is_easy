"""
Project #1: A Simple Game: Connect 4

"""
            
fields = [[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "]]   


def drawBoard(fields):
    for row in range(13):
        if row % 2 == 0:
            practical_row = int(row/2)
            for column in range(13):
                if column % 2 == 0:
                    practical_column = int(column/2)
                    if column != 12:
                        print(fields[practical_column][practical_row],end="") 
                    else:
                        print(fields[practical_column][practical_row]) 
                else:
                    print("|", end="")
        else:
            print("-------------")


def updateBoard(num, player):
    column = fields[num]
    index = ""
    reversed_column = column[::-1]
    for row in reversed_column:
        if row == " ":
            index = reversed_column.index(row)
            reversed_column[index] = "X" if player == 1 else "O"
            break
    if index == "":
        return False
    column = reversed_column[::-1]
    print(column)
    fields[num] = column
    drawBoard(fields)
    return True


def checkIfAnyWinner(board):
    print('Checking if any winner')


def askNextMovement(player):
    print('Asking for the next move')


print('Starting Connect4.....\n')

drawBoard(fields)

def startPlaying():
    print('Starting Connect 4')
    player = 1
    no_win = True
    while(no_win):
        print('Player ',player, "turn:\n")
        if player == 1:
            column_no = int(input("Enter the column number:\n"))
            updated_flag = updateBoard(column_no - 1, player)
            if updated_flag:
                player = 2
            else:
                print('movement disallowed!\n')
        else:
            column_no = int(input("Enter the column number:\n"))
            updated_flag = updateBoard(column_no - 1, player)
            if updated_flag:
                player = 1
            else:
                print('Movement disallowed')


startPlaying()
