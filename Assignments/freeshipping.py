# Create a func. called free shipping
# That tells u if u qual for free shipping or no
# U only get free shipping if 
# ur a Prime member OR order is at least $25
# AND at least 18 yrs old, or have parent consent
# Function has 4 params
# prime (boolean), cost (float), age (int), consent (bool)
# YOU CAN USE MORE THAN 1 LOGIC OPERATOR IN A CONDITION
# Use parenthasis to group if neeed

def FreeShipping(prime, cost, age, consent):
    try:
        cost = int(input("How much was the order?"))
        prime = input("Do you have a Prime subscription, Y or N?\n>").lower()
    except ValueError:
        print("Please Input ") #OPEN EXCEPTIONS.PY AND CONT