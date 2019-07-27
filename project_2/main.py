"""
Project #2: Hangman


+++++++++++++++   
  _____________ 0
 _|_          | 1
| _ |         | 2
  |           | 3
/ | \         | 4
  |           | 5
/   \         | 6

"""
 
from termcolor import colored, cprint

def drawHangman(face=False, neck=False, body=False, left_hand=False, right_hand=False, left_leg=False, right_leg=False):
    for row in range(10):
        if row == 0:
                for column in range(20):
                    if column >= 3:
                        if column == 19:
                            print("_")
                        else:
                            print("_", end="")
                    else:
                        print(" ",end="")
        
        #face
        elif face == True and row == 1:
            for column in range(20):
                if column == 0:
                    print(" ",end="")
                elif column == 1:
                    cprint("_",'red',end="")
                elif column == 2:
                    print("|", end="")
                elif column == 3:
                    cprint("_",'red', end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")
                    
        elif face == True and row == 2:
            for column in range(20):
                if column == 0 or column == 4:
                    cprint("|",'red', end="")
                elif column == 1 or column == 3: 
                    print(" ", end="")
                elif column == 2:
                    cprint("_",'red', end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")
       
       #neck
        elif neck == True and row == 3:
            for column in range(20):
                if column == 2:
                    cprint("|",'red', end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ",end="")

        #left hand
        elif left_hand == True and row == 4:
            for column in range(20):
                if column == 0:
                    cprint("/",'red', end="")
                elif column == 1:
                    print(" ",end="")
                elif column == 2:
                    cprint("|",'red', end="")
                elif column == 3:
                    print(" ",end="")
                elif right_hand == True and column == 4:
                    cprint("\\",'red', end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")

        #body
        elif body == True and row == 5:
            for column in range(20):
                if column == 2:
                    cprint("|",'red', end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ",end="")
  
        #left leg
        elif left_leg and row == 6:
            for column in range(20):
                if column == 0:
                    cprint("/",'red', end="")
                elif column == 1:
                    print(" ",end="")
                elif column == 3:
                    print(" ",end="")
                # right leg
                elif right_leg and column == 4:
                    cprint("\\",'red', end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")

        elif row == 9:
            for column in range(20):
                if column <= 10:
                    print(" ", end="")
                elif column == 19:
                    print("-")
                else:
                    print("-", end="")
        else:
            for column in range(20):
                if column == 19:
                    print("|")
                else:
                    print(" ", end="")  


# phrase should only be alphabets
def askHostToSayPhrase(repeatText = None):
    question = repeatText if repeatText is not None else "Type your secret word.\n"
    word = input(question)
    if type(word) == str and len(word) == 3:
        return word.lower()
    else:
        return askHostToSayPhrase("Hey, please make it atleast three words! Type again.\n")

#draw guessed letters or blanks
def drawGuessedLetters(guessed_letters):
    print("Word: ", end="")
    for letter in guessed_letters:
        print(letter, end="  ")
    print("\n")

# checks if the letter is guessed is right or not
def checkGuess(letter, phrase_letters):
    guess = False
    if letter in phrase_letters:
        guess = True
    return guess

# fill guessed letters      
def fillBlanks(letter, phrase_letters, guessed_letters):
    indices = [i for i, el in enumerate(phrase_letters) if el == letter]
    for index in indices:
        guessed_letters[index] = letter
    return guessed_letters

def guessLetter(repeatText = None):
    question = repeatText if repeatText is not None else "What's your guess?\n"
    word = input(question)
    if type(word) == str and len(word) == 1:
        return word.lower()
    else:
        return guessLetter("Hey, one letter at a time! Type again.\n")
    


def showMisses(misses):
    print("Misses: ", end="")
    for miss in misses:
        print(miss, end=",")
    print("\n")


def drawHangmanBasedOnWrongGuessed(committed_mistakes):
    if committed_mistakes == 0:
        drawHangman(False, False, False, False, False, False, False)
    if committed_mistakes == 1:
        drawHangman(True, False, False, False, False, False, False)
    if committed_mistakes == 2:
        drawHangman(True, True, False, False, False, False, False)
    if committed_mistakes == 3:
        drawHangman(True, True, True, False, False, False, False)
    if committed_mistakes == 4:
        drawHangman(True, True, True, True, False, False, False)
    if committed_mistakes == 5:
        drawHangman(True, True, True, True, True, False, False)
    if committed_mistakes == 6:
        drawHangman(True, True, True, True, True, True, False)
    if committed_mistakes == 7:
        drawHangman(True, True, True, True, True, True, True)


def startHangman():
    #ask player to guess
    phrase = askHostToSayPhrase()
    phrase_letters = [char for char in phrase]
    guessed_letters = ["__" for el in phrase_letters ]
    committed_mistakes = 0
    already_guessed_letters = []
    missed_letters = []

    # hide the secret word, clear the screen.
    print(chr(27) + "[2J") 

    no_win = True

    # ask player to start guessing, while loop to continue
    # until the player guessed it correct or
    # the mistakes are 7
    while(committed_mistakes < 7 and no_win):
        # draw guessed letters or blanks
        drawGuessedLetters(guessed_letters)

        if len(missed_letters) > 0:
            showMisses(missed_letters)
        # ask player to guess
        guessed_letter = guessLetter()
        
        
        # guessed letter should not be allowed
        if guessed_letter in already_guessed_letters:
            cprint("Hey, you already guessed it, try something else!", 'blue', attrs=['bold'])
            continue
        else:
            already_guessed_letters.append(guessed_letter)
        #check if the guessed letter is correct
        guessed = checkGuess(guessed_letter, phrase_letters)

        # if guesed correctly, fill the blanks with the letter
        # inform the player it's the right guess
        if guessed == True:
            guessed_letters = fillBlanks(guessed_letter, phrase_letters, guessed_letters)
            # todo: make a list of appreciation and pick randomly
            cprint("That's like a pro!", 'magenta', attrs=['bold'])

            #check if the word is completed
            if guessed_letters == phrase_letters:
                no_win = False

        # if guessed is incorrect, draw hangman
        # and increment the committed mistakes counter
        # inform the player it's a wrongguess
        else:
            committed_mistakes += 1
            missed_letters.append(guessed_letter)
            # draw hangman based on wrong guessed
            drawHangmanBasedOnWrongGuessed(committed_mistakes)
            # todo: make a list of wrong guessed messages and pick randomly
            cprint("Damn, you missed!", 'red', attrs=['bold'])

        print("----------------------------------------------------------------------------")
    
    if no_win == False:
            cprint("You Won! Great Job!", 'cyan', attrs=['bold'])
    
    if committed_mistakes == 7:
        drawHangmanBasedOnWrongGuessed(committed_mistakes)
        cprint("Oops, you lost. Better luck next time!", 'red', attrs=['bold'])

        


startHangman()

