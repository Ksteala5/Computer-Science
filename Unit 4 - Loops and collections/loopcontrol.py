#Loop control statements
# allow you to change how loops operate
#Allow you to quit, skip, or even do nothing
# break, continue, pass

# break
# break exits a loop prematurely, before it was supposed to end
# happens immediately when ran
# program continues where loop ends

# example

bag_of_fruit = ["apple", "orange", "bug", "kiwi", "watermelon", "mango"]

for fruit in bag_of_fruit:
    if fruit == "bug":
        print("Ew, a bug. *You toss the bug out.*")
    else:
        print("You ate a(n) "+ fruit)
print(" ")
#break would end it at bug
        

# continue
# skips current loop
# it does exit the entire loop, just moves on to nex iteration

#example
orders = [15,30,35,23,100,3,10,22]

#Discount apllying program
#only apply discount for orders above $20

for order in orders:
    if order<20:
        continue
    print("$"+ str(order)+ " order didcounted 5% to $" + str(order*.95))

#Pass 
# does nothing!!!!!!!!!
# used as placeholder usually
# Text-Adventure project
    
def enter_forest():
    pass

def swim_river():
    pass

def eat_icecream():
    pass