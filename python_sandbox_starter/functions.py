# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create a Function
def sayHello(name = 'Sam') :
    print(f'Hello, {name}')


# Return Values
def getSum(num1, num2) :
    result = num1+num2
    return result

num = (getSum(2,4))



getSum = lambda num1, num2: num1 + num2



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

