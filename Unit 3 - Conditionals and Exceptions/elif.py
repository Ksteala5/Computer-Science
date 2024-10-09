# the if statement has 2 buddies
# the first little buddy is the else statement

x=10 

if x>0: # not every if needs an else
    print("x is positive")

# Second lil buddy is elif
elif x <0:
    print("x is negative")

else: #else always needs an if
    print("x is 0")



light = input("What color is the light?\n>")

if light.lower() == "green":
    print("GO")

elif light.lower() == "yellow":
    print("STOP IF SAFE")

elif light.lower() == "red":
    print("STOP")

else:
    print("I DONT KNOW")
