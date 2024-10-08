# If statements evaluate boolean expressions!
# They make decisions about which code to run next
#
# Take a temperature
# print "<temp> is hot" if >= to 80
# other, print "<temp> is not hot"
temp=input("So, you think it's hot? Whats the tempurature in F?\n>")
temp=int(temp)

#if <boolean expression>:
#This should remind of writing a function
if temp>= 80:
    print(str(temp)+ "°F is hot!")

else:     #Otherwise..
    print(str(temp)+"°F isn't hot...")

# Not all if statements need an else, none actually NEED an else, optional.
# All else statements MUST have a corrosponding if statement
# ELSE CANNOT EXIST alone.
# An if can only have ONE else
    


    # Create a program that asks for a password

# if password is correct, print ACCESS GRANTED
# password is skibidi68
permpass="skibidi68"
password=input("INSERT PASSWORD:\n>")

if password == permpass:
    print("ACCESS GRANTED. WELCOME, MY KITTEN SIGMA ALPHA WOLF")
else:
    print("ACCESS DENIED YOU GOOBER")

# Activity 2, electric boogaloo
tally_score = 0
q1=int(input("input '7'\n>"))
q2=int(input("input '6842'\n>"))
q3=int(input("input a WHOLE number LESS than 0\n>"))
q4=int(input("input a WHOLE number GREATER than 0\n>"))
q5=int(input("what is 2+2-2/2?\n>"))

if q1 == 7:
    tally_score = tally_score +1
else:
    tally_score = tally_score +0

if q2 == 6842:
    tally_score = tally_score +1
else:
    tally_score = tally_score +0
if q3 < 0:
    tally_score = tally_score +1
else:
    tally_score = tally_score +0

if q4 > 0:
    tally_score = tally_score +1
else: 
    tally_score = tally_score +0

if q5 == 3:
    tally_score = tally_score +1
else: 
    tally_score = tally_score +0

tally_score = str(tally_score)
print("Your score is " + tally_score + ".")

# String functions are a group of functions that modify strings
# .lower()
# .lower() changes string to all lowercase
# .upper() changes all string to uppercase

# .capitalize() changes the entire string to lowercase, then capitalizes the first letter of the string.
# Hello World > Hello world

# .title() changes the entire string to titlecase
# hello world > Hello World

# .swapcase() inverts the capitalization of each character
# Hello World > hELLO wORLD


x= "Lord of the Rings".lower()

print(x)