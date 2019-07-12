"""
Homework Assignment #3: "If" Statements

"""

# compare three values, return true only if 2 or more values are equal
def compare(a, b, c):
    value = False
    # checking if a is string type, convert to int
    if type(a) == str:
        a = int(a)
    
    # checking if a is string type, convert to int
    if type(b) == str:
        b = int(b)
    
    # checking if a is string type, convert to int
    if type(c) == str:
        c = int(c)
    
    if a == b or a == c or b == c:
        value = True
    return value

comparisonValue = compare(1, 2, "2")
print("Comparison value: ", comparisonValue)