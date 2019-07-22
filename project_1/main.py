"""
Project #1: A Simple Game: Connect 4

"""
            
fields = [[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "]]   


def createColumnMatrix():
    column_matrix = [[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "]]   
    for i in range(7):
        for j in range(len(fields[i])):
            column_matrix[j][i] = fields[i][j]

    return column_matrix

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
    print("\n")

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

def checkIfFourInColumn(column_matrix):
    winner = False
    for column in column_matrix:
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

def checkIfFourInForwardDiagonal(column_matrix, player):
    for i in range(0, len(column_matrix)):
        for j in range(0, len(column_matrix[i])):
            try:
                if column_matrix[i][j] == player and column_matrix[i + 1][j - 1] == player and column_matrix[i + 2][j - 2] == player and column_matrix[i + 3][j - 3] == player:
                    return True
            except IndexError:
                next

    return False


def checkIfFourInBackwardDiagonal(column_matrix, player):
    for i in range(0, len(column_matrix)):
        for j in range(0, len(column_matrix[i])):
            try:
                if column_matrix[i][j] == player and column_matrix[i + 1][j + 1] == player and column_matrix[i + 2][j + 2] == player and column_matrix[i + 3][j + 3] == player:
                    return True
            except IndexError:
                next
    return False

def isValidMove(column_no):
    if column_no >=1 and column_no <=7:
        return True
    else:
        return False


def startConnect4():
    player = 1
    no_win = True
    winner = ""
    while(no_win):
        column_no = int(input('Player ' + str(player) + ' turn, enter the column number:\n'))
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
                    column_matrix = createColumnMatrix()
                    winner = checkIfFourInColumn(column_matrix)
                    if winner:
                        no_win = False
                    elif checkIfFourInBackwardDiagonal(column_matrix, tile):
                        winner = current_player
                        no_win = False
                    elif checkIfFourInForwardDiagonal(column_matrix, tile):
                        winner = current_player
                        no_win = False                   
            else:
                print('Hey, this is not a right move. Try again.\n')


    print('Winner is ',winner)

print('Starting Connect 4 Game... Get ready!\n')
drawBoard(fields)
startConnect4()
