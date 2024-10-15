# Nested if statements


prime = True
cost = 20
age = 17
consent = False

# if (prime == True or cost >= 25) and (age >= 18 or consent == True):

if prime: 
    if age >= 18:
        print("Yay, free shipping!")
    elif consent:
        print("Yay, free shipping!")
    else:
        print("Lmao no free shipping.")

elif cost >= 25:
        if age >= 18:
            print("Yay, free shipping!")
        elif consent:
            print("Yay, free shipping!")
        else:
            print("Lmao no free shipping.")

else:
     print("NOPE LMAOO")


# Decide if we need an umbrella
# You need if raining and going outside
     


raining = input("Is it raining? \n>")


if raining.lower() == "yes":
    outside = input("Are you going outside?\n>")
    
    if outside.lower("yes"):
        print("BRING UMBRELLA")
    else:
        print("No umbrella needed")
else:
    print("No umbrella")