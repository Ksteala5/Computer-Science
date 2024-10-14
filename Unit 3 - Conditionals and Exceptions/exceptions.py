# Exception Handling
# Write a program that asks for two numbers and divides them

# if = try
# else = except
def div2():
    try:    # We always enter the try block, there is no condition.
        x = int(input("Input first number:\n>"))
        y = int(input("Input second number: \n>"))
        print(x/y)

    except ZeroDivisionError:
        print("Division by 0 is not possible. Try Again")
        div2()

    except ValueError:
        print("Please enter a valid numerical symbol.")
        div2()

    except: # If anything in try causes an error, 
            # The try block stops immediately and then the except is ran
            # Rest of try gets skipped
            # If try exectutes without error, except is skipped
            # The only way to get into the except is to "throw" an error
        print("Hate. Let me tell you how much I've come to hate you since you've arrived.")
        div2()

div2()