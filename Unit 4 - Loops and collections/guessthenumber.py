import random
number = random.randint(1,100)
numberguess = ""
while numberguess != number:
    numberguess = input("Guess a number.\n> ")
  
    if int(numberguess) == number:
        print("Correct!")
    elif int(numberguess)>number:
        print("Too high.")
    elif int(numberguess)<number:
        print("Too low.")
    else:
        print("How did you get here")

print("Great job!")