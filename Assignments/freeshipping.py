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
    cost = int(cost)
    age = int(age)
    if prime == "yes" or cost >= 25:
        stepone = "pass"
    else:
        stepone = "fail"
    if age >= 18 or consent == "yes":  
        steptwo = "pass"
    else:
        steptwo = "fail"
    if stepone == "pass" and steptwo == "pass":
        print("You get free shipping!")
    else:
        print("No free shipping lmao")
FreeShipping("no", 65, 18, "no")
