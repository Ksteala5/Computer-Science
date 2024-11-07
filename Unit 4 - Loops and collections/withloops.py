import random
# There are a couple of loops in python
# For loop lets us iterate thru a list
# Great for looping a certain amount
#What if we need to loop an UNCERTAIN amount of time????
#ex: enterig password
#Could get right first time
#Or after the millionth time
# or anything in between
real_pass = "ninjalowtaper"
entered_pass = ""
attempts = 0

while entered_pass != real_pass:
    #ask password
    entered_pass = input("Please enter the password\n> ")

    #Check if pw is correct
    if entered_pass == real_pass:
        print("Hello, Admin")
    else: 
        print("ACCESS DENIED")
        print("Try again.")
        attempts += 1
        print(str(attempts)+" attemps to enter password have been taken.")
print("Welcome!")

#With while loops, you need to be careful on inf loops
# when comp is in rest, it has nightmares abt inf loops
# inf loop happens when u enter loop that cant be escaped




# Dont create a black hole.
# Lets make a black hole

user_input = ""

while user_input != "exit":
    user_input = input("Enter Something!\n> ")
    print("Type exit to quit")
    print("You typed: "+user_input)

print("All done!")