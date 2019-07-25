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
                    print("_",end="")
                elif column == 2:
                    print("|", end="")
                elif column == 3:
                    print("_", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")
                    
        elif face == True and row == 2:
            for column in range(20):
                if column == 0 or column == 4:
                    print("|", end="")
                elif column == 1 or column == 3: 
                    print(" ", end="")
                elif column == 2:
                    print("_", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")
       
       #neck
        elif neck == True and row == 3:
            for column in range(20):
                if column == 2:
                    print("|", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ",end="")

        #left hand
        elif left_hand == True and row == 4:
            for column in range(20):
                if column == 0:
                    print("/", end="")
                elif column == 1:
                    print(" ",end="")
                elif column == 2:
                    print("|", end="")
                elif column == 3:
                    print(" ",end="")
                elif right_hand == True and column == 4:
                    print("\\", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")

        #body
        elif body == True and row == 5:
            for column in range(20):
                if column == 2:
                    print("|", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ",end="")
  
        #left leg
        elif left_leg and row == 6:
            for column in range(20):
                if column == 0:
                    print("/", end="")
                elif column == 1:
                    print(" ",end="")
                elif column == 3:
                    print(" ",end="")
                # right leg
                elif right_leg and column == 4:
                    print("\\", end="")
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

drawHangman(False, False, False, False, False, False, False)
print("")
drawHangman(True, False, False, False, False, False, False)
print("")

drawHangman(True, True, False, False, False, False, False)
print("")

drawHangman(True, True, True, False, False, False, False)
print("")

drawHangman(True, True, True, True, False, False, False)
print("")

drawHangman(True, True, True, True, True, False, False)
print("")

drawHangman(True, True, True, True, True, True, False)
print("")

drawHangman(True, True, True, True, True, True, True)
print("")


