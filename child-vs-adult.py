age = input("What is your age? ")

# Remember! age is a string! If you want to compare it to a number, we need to
# convert it first to a number

age = int(age)
if age >= 18:
    print("You are an adult.")
else:
    print("You are a child.")
