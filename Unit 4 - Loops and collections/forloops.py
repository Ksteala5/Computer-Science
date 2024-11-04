import random
# For loops
# This is a big deal
# allows programmer to repeat, or loop


# Write a program that prints the numbers 1-10
# Each on a new line

fav_foods = ["Eggs Benedict", "Fried Chicken", "Mac n Cheese", "Chipotle Burrito Bowl"]

# for <var> in <list>:

for i in range(90,101):
    print(i)

for food in fav_foods:
    print(food)
    #Runs all of the lines inside the for loop
    #When it reaches the bottom of the list, it runs again
    #and moves on o thee next item in the list
    #Ends when no list items


#**Print a Countdown**: Create a countdown from 10 to 1 using forloop
    
for i in range(10,0,-1):
    print(i)


nums = [1,2,3,4,5]
sum = 0

for n in nums:
    sum = sum+n
print(sum)


ints = [1,2,3,4,5]
listy=[]

for i in ints:
    listy.append(i*i)

print(listy)

#count vowels
stringy = input("Please Enter a String\n> ")
numvowels = 0
for s in stringy:
    if s.lower() in ["a", "e", "i", "o", "u"]:
        numvowels = numvowels + 1
print(numvowels)

#Print Multiplication Table

try:
    multi = int(random.randint(0,111111111111))
    for i in range(0,multi+1):
        print(str(multi)+ " x "+str(i)+ " = " + str(multi*i))
except ValueError:
    print("kys")

#list names and say hi
names = ["Peter", "John", "Paul", "Luke"]
for name in names:
    print("Hello, "+name+ "!")
