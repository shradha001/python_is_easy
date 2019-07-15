"""
Homework Assignment #5: Basic Loops

Fizz Buzz Assignment
"""

def printFizzBuzz():
    for num in range(1, 101):
         # 1 is neither prime, nor divisible by 3 or 5, so printing it straight
        if num == 1:
            print(num)
            continue
        
        
        # creating a loop to gather prime number, a number cannot be divisible by another number greater than it's own
        # if it's divisible by any other number within this range, then it's not a prime
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        #printing prime numbers
        if is_prime:
            print("prime ==> ", num)

        # checking if a number is divisible by 3 and 5
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ==> ",num)
        else:
            # checking if a number is divisible by 3 only
            if num % 3 == 0:
                print("Fizz ==>",num)

            # checking if a number is divisible by 5
            elif num % 5 == 0:
                print("Buzz ==> ",num)

            # if not a prime, nor divisible by 3 or 5 or both, then simply print the number
            elif is_prime == False:
                print(num)
            
        
printFizzBuzz()