
# python-functions-cw_2
# Problem 1:
#
# Create a function that will ask the user for a number. Use the function to get two numbers from the user, then pass the two numbers to a function. Add, subtract, multiple, and divide the numbers.

# !! : "Create a function that will ask the user for a number". This is not a function 
userInput1 = int(input("Enter a number"))
userInput2 = int(input("Enter a number"))
operation = (userInput1, userInput2) # !! : This is not the correct syntax to call a function 

print(userInput1 + userInput2)
# /Addition

# !! : "Add, subtract, multiple, and divide the numbers." This problem does not call for conditionals 

if operation == '+':
    print ('{10}+ {10} = ' .f(userInput1, userInput2))
print(userInput1 + userInput2)

elif operation == '-':
print ('{10}+ {10} = ' .f(userInput1, userInput2))
print(userInput1 - userInput2)

elif operation == '*':
print ('{10}+ {10} = ' .f(userInput1, userInput2))
print(userInput1 * userInput2)

elif operation == '/':
print ('{10}/ {10} = ' .f(userInput1, userInput2))
print(userInput1 / userInput2)

