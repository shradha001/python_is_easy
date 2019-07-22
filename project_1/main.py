"""
Project #1: A Simple Game: Connect 4

"""
            
fields = [[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "]]   


def alterColumns():
    tmp_fields = [[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "]]   
    for i in range(7):
        for j in range(len(fields[i])):
            tmp_fields[j][i] = fields[i][j]

    return tmp_fields

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
    fields[num] = column
    drawBoard(fields)
    return True

def checkIfFourInRow():
    winner = False
    for column in fields:
        counter = 0
        length = len(column)
        for i in range(1, length):
            if column[i - 1] != " " and column[i] != " " and column[i - 1 ] == column[i]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                winner = column[i - 1]
                return winner    
    return winner

def checkIfFourInColumn(tmp_fields):
    winner = False
    for column in tmp_fields:
        counter = 0
        length = len(column)
        for i in range(1, length):
            if column[i - 1] != " " and column[i] != " " and column[i -1 ] == column[i]:
                 counter += 1
            else:
                counter = 0
            if counter == 3:
                winner = column[i - 1]
                return winner
    return winner

def checkIfFourInForwardDiagonal(tmp_fields, player):
    for i in range(0, len(tmp_fields)):
        for j in range(0, len(tmp_fields[i])):
            try:
                if tmp_fields[i][j] == player and tmp_fields[i + 1][j - 1] == player and tmp_fields[i + 2][j - 2] == player and tmp_fields[i + 3][j - 3] == player:
                    return True
            except IndexError:
                next

    return False


def checkIfFourInBackwardDiagonal(tmp_fields, player):
    for i in range(0, len(tmp_fields)):
        for j in range(0, len(tmp_fields[i])):
            try:
                if tmp_fields[i][j] == player and tmp_fields[i + 1][j + 1] == player and tmp_fields[i + 2][j + 2] == player and tmp_fields[i + 3][j + 3] == player:
                    return True
            except IndexError:
                next
    return False

def isValidMove(column_no):
    if column_no >=1 and column_no <=7:
        return True
    else:
        return False


drawBoard(fields)

def startPlaying():
    print('Starting Connect 4 Game... Get ready!')
    player = 1
    no_win = True
    winner = ""
    while(no_win):
        print('Player ',player, "turn:\n")
        column_no = int(input('Enter the column number:\n'))
        if isValidMove(column_no) == False:
            print('Hey, this is not a right move. Try again.\n')
        else:
            updated_flag = updateBoard(column_no - 1, player)
            if updated_flag:
                print("")
                current_player = player
                tile = "X" if player == 1 else "0"
                player = 2 if player == 1 else 1
                winner = checkIfFourInRow()
                if winner:
                    no_win = False
                else:
                    tmp_fields = alterColumns()
                    winner = checkIfFourInColumn(tmp_fields)
                    if winner:
                        no_win = False
                    elif checkIfFourInBackwardDiagonal(tmp_fields, tile):
                        winner = current_player
                        no_win = False
                    elif checkIfFourInForwardDiagonal(tmp_fields, tile):
                        winner = current_player
                        no_win = False                   
            else:
                print('Hey, this is not a right move. Try again.\n')


    print('Winner is ',winner)

startPlaying()
