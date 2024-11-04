import random
# Python has 4 types of collections 
#Tuple 
# set
# list
# dictionary

#Today we focus on lists
# A list is a way to store more than one value in single variables
# The values in the list are called items
# Items can be accessed by their index (pos. on list) indices
#INDEX                   0        1                  2               3                   4              
best_minecraft_weapons = ["Mace","Netherite sword", "Netherite axe","Ender Crystals", "Diamond sword"]
best_years = [1776, 1985, 1994, 1957, 2016]
myint = 3

#len() LENGTH

print("There are "+ str(len(best_minecraft_weapons))+ " best MC weapons")

print(best_years[myint])
print(best_minecraft_weapons[0])
print(best_minecraft_weapons[len(best_minecraft_weapons)-1])

#List items can change
best_minecraft_weapons[3] = "Shield"
print(best_minecraft_weapons)

#List functions!
# .pop()        removes an item at a given pos.
best_minecraft_weapons.pop(1) #Remove Netherite sword

# .remove()     Removes an item by value - removes first instance of the value
best_minecraft_weapons.remove("Mace") #If the value doesn't exist, error

# .append()     ADDS the value as a new item to the end of the list
best_minecraft_weapons.append("Diamond Axe")

numbers = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)]
print(numbers)

# .sort() Sorts from smallest to largest

numbers.sort()
print(numbers)

# max() prints largest in list
print(max(numbers))
# min() prints smallest in list
print(min(numbers))









#Strings... are just..... lists of characters?! :O
print("Osowski"[2])