"""
Homework Assignment #7: Dictionaries and Sets

"""

# song dictionary
song = {
    "name" : "What Hurts the Most",
    "artist": "Rascal Flatts",
    "album": "Me and My Gang",
    "recorded": 2005,
    "released": 2006,
    "duration": 3.33,
    "genre": "country",
    "label": "Lyric Street"
}

def printSongMetadata():
    print("\n*** Song Metadata ***\n")
    for key in song:
        print(key, ":", song[key])
    print("\n*** End ***\n")

def askQuestion():
    key = input("\nGreat, let\'s start the game, guess the key?\n")
    value = input("\nWhat you think is the value of " + key + "?\n")
    if key and value:
        key = key.lower()
        value = value.lower()
        if key in song and song[key].lower() == value:
            return True
    return False

def startGuessingGame():
    if askQuestion():
        print("Bingo! You guessed it right...")
    else:
        print("Oops... You missed!")
        repeat = input("\nWanna try again? Say 'yes' to continue or say 'no'.\n")
        if repeat.lower() == "yes":
            startGuessingGame()
        else:
            print("\nSee you again!")
    

# print song metadata
printSongMetadata()

print("Starting game....\n")

# start the guessing game
startGuessingGame()
