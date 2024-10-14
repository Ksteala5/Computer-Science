# Logical Operators
# Arithmetic Operators + - * / // ** %
# Comparison Operators > < >= <= ==
# Logical Operators "and" "or" "not (!)"

def check_eligibility(age, experience): #Age has to be 18 or older, exp. is 1 year or more
    
    if age >= 18 and age <= 22 and experience >= 1:
        print("You are eligible!")

    else:
        print("Uneligible, try again next year?")

check_eligibility()