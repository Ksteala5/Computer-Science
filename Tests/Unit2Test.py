rand1 = input("Input a random word\n>") #Define 3 random words
rand2 = input("Input a second random word\n>")
rand3 = input("Input a thrid random word\n>")
print("You chose the words " + rand1 + ", " + rand2 + ", " + rand3 + ".") #Put in string

def add_three(a,b,c): #define function
    print(a + b + c)
    
add_three(int(input("First number\n>")),int(input("Second number\n>")),int(input("Third number\n>")))
#Forgot how to do it in separate lines, but both defining and making them into integers to add.

def data_three():
    word = str(input("Input a word\n>"))
    integer = int(input("Input an integer\n>"))
    flt = float(input("Input a float\n>"))
    intflt = str(integer+flt)
    print(word+intflt)

data_three()