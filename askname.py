"""
A program that asks for the name of the user

This shows you how to use the builtin 'input' function. The first
parameter is the text it is going to write on the screen before asking
the user (but you could also just use print).

The return value of this function is a string, what the user typed.
"""

username = input("What is your name? ")
if username == "Christian":
    print("你好 {}".format(username))
elif username == "Mathieu":
    print("Bonjour {}!".format(username))
else:
    print("Hello {}!".format(username))

