"""
Homework Assignment #11(pirple.com): Error Handling
From assignment 3: "If" Statements

"""

# compare three values, return true only if 2 or more values are equal
# integer value of boolean True is 1
# integer value of boolean False is 0
def compare(a = None, b = None, c = None):
    try:
        value = False
        a = int(a)
        b = int(b)       
        c = int(c)   
        print("Valid values.")     
        if a == b or a == c or b == c:
            value = True
    except ValueError:
        print("ValueError: Only, numbers are allowed.")
    except TypeError:
        print("TypeError: Please enter only numbers.")
    except Exception:
        print(Exception)
        print("Exception, Only numbers are allowed!")
    finally:
        print("Values ", a, b, c)
        return value

# all integers
print("Result: ",compare(1, 2, 3))
print("\n")

# numbers in str
print("Result: ",compare("2", "3", "4"))
print("\n")

# alphabets
print("Result: ",compare("a", "b", "c"))
print("\n")

# one boolean
print("Result: ",compare(True))
print("\n")

# three boolean values
print("Result: ",compare(True, True, False))
print("\n")

# integer with list
print("Result: ",compare(1, 2, [True]))
print("\n")

# str with boolean
print("Result: ",compare("2", "2", True))
print("\n")

# equal numbers in str
print("Result: ",compare("2", "2", "2"))
print("\n")

# empty str
print("Result: ",compare("-1", ""))
print("\n")

# three empty str
print("Result: ",compare("", "", ""))
print("\n")

#floats
print("Result: ",compare("1.1", "1","1.1"))

