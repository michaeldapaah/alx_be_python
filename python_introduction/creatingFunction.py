# Notes under functions 

# function definition
#to define a function, use the keyword 'def' followed by the function name and parentheses
# you can also define parameters inside the parentheses
# function body is indented under the function definition
# to call a function, use the function name followed by parentheses

def greet(name, age = None):# This is an example of keyword argument (None is a keyword)
    """Prints a greeting message."""
    print(f"Hello, {name}!")

greet("Alice") 


#Lamda functions are a way to create small anonymous functions in Python.
# Lambda functions are especially useful when you need to pass a simple function as an argument to another function, like in the map(), filter(), or reduce() functions.
# However, they are limited to single expressions and cannot contain multiple lines of code or complex logic

add = lambda x, y: x + y
result = add(5, 3)
print(result)  # Output: 8

    