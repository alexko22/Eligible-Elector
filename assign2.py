# Task 1: Get the user's age
age = int(input("How old are you?"))

# Task 2: Decide Eligibility
if (age >= 18):
    print("Congrats! You are eligible to vote! Go make a difference. ^_^")
else:
    # Calculating how many years until the user is 18 (able to vote)
    diff = 18 - age
    print("Yikes! You can't vote yet! You can vote in", + diff, "years :')")
