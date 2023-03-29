import time

def intro():
    print("Welcome to the Python Shell")
    print("Type help for a list of commands")
    print("Type quit to exit the shell")
    time.sleep(2)
    name = input("What is your name? ")
    print(f"Hello, {name}!")
    time.sleep(2)
    print("Today you will learn Python")

def help():
    print("These are the basic commands that you might need:")
    print("Categories:")
    print("1. Basic math")
    print("2. Strings")
    print("3. Lists")
    print("4. Dictionaries")
    print("5. Functions")
    what_they_want_to_know = input(">")

    if what_they_want_to_know == "1":
        print("1. Basic math")
        print("The Math class is a collection of basic mathematical functions; the major commands are addition, subtraction, multiplication, division, and exponentiation.")
        print("This is how to use them:")
        print("1. Add two numbers")
        print('example: "print(1+2)"')
        print("2. Subtract two numbers")
        print('example: "print(1-2)"')
        print("3. Multiply two numbers")
        print('example: "print(1*2)"')
        print("4. Divide two numbers")
        print('example: "print(1/2)"')
        print("5. Exponentiate two numbers")
        print('example: "print(1**2)"')
        time.sleep(2)

    elif what_they_want_to_know == "2":
        print("2. Strings")
        print("The String class is a collection of data storage; the major commands are concatenation, slicing, and formatting.")
        print("This is how to use them:")
        print("1. Concatenate two strings")
        print('example: "print("Hello World")"')
        print("2. Slicing a string")
        print('example: "print("Hello World")[1:3]"')
        print("3. Formatting a string")
        print('example: "print("Hello World".format())"')
        time.sleep(2)

    elif what_they_want_to_know == "3":
        print("3. Lists")
        print("The List class is a collection of lists; the major commands are indexing and slicing.")
        print("This is how to use them:")
        print("1. Indexing a list")
        print('example: "print([1,2,3])"')
        print("2. Slicing a list")
        print('example: "print([1,2,3][1:3])"')
        time.sleep(2)

    elif what_they_want_to_know == "4":
        print("4. Dictionaries")
        print("The Dictionary class is a collection of key-value pairs; the major commands are indexing and adding new elements.")
        print("This is how to use them:")
        print('example: "my_dict = {"key1": "value1"}"')
        print('example: "my_dict["key2"] = "value2""')
        print('example: "print(my_dict["key1"])""')
        time.sleep(2)

    elif what_they_want_to_know == "5":
        print("5. Functions")
        print("A function is a block of code that performs a specific task.")
        print("This is how to use them:")
        print('example: "def my_function(): \n    print("Hello")"')

#Running all the functions
intro()

while True:
    shell_command = input("> ")
    
    if shell_command.lower() == "quit":
        print("Goodbye!")
        time.sleep(2)
        break
    
    exec(shell_command)
    
    if shell_command.lower() == "help":
        help()

