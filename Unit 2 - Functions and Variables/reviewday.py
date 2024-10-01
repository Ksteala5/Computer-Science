#2 basic functions
#you know something is a function because it has () at the end
#stuff that goes in () are called parameters
#parameters are info function needs to run
#I say jump you say how high
print("Hello world") #Hello world is parameter
input("Are you human?/n>")              # \n is called an escape character
#Input is NOT always required, only use when needed

#Variables
#way to store data for later use in prgrm
#Syntax (grammar) 
#<name> = <value>
x=5   # x is variable name, 5 is value
#Snake naming convention - all lowercase, underscores for spaces
#Concise = Short and descriptive
username = "Kaden"          #String (many characters in a STRING)
fav_animal = "Raven"        #String
chipotles_visited = 6       #integer (Whole number)
percent_complete= 61.47     #float (decimal)
is_cool = True              #boolean (TRUE or FALSE)
first_letter = 'R'          #character (keyboard symbol)

chipotles_visited = 7       #REASSIGNING variable

#Arithmetic operators (sounds scary, just basic math)
# +  -   *   /   **  %   //
print(2+2)              #>8
print("2"+"2")          #>22
print("cat" + "dog")    #>catdog
print("cat"*3)          #catcatcat
print("cat"+3)          #ERR; CANNOT USE + for string and integer
print("cat"*"dog")      #ERR; CANNOT USE * for string and string

my_variable = 2+3       #Arithmetic op. can be done anywhere

# Make some Working programs
# ADD two numbers using input
x=input("number 1 \n>") #input ALWAYS returns string
x=int(x)
y=input("number 2 \n>")
y=int(y)
print(x+y)

#2. Conv. C to F using input
temp_c = input("Temperature in Celcius\n>") 
temp_c=int(temp_c)
temp_f = (temp_c * 1.8) + 32
print("It is " + temp_f + "degrees Farenheight.")

#Conversion funct.
str()
int()
float()
bool()
bin()

#Functions
#A LOT lik variables
#Have names
#Can be recalled from mem. by calling name
#store info
#Variables store value
#Functions store codde
# def <name>():
def potato():
    print("Tomato")

potato() #EVERY FUNCTION CALL NEEDS PARENTHESIS
         #EVEN IF NO PARAMETERS

def jump(how_high):
    how_high = str(how_high)     #String to integer (LAME)
    print("You jumped "+how_high+" inches high")

jump(14)


#SCOPE
#Global vs Local Variables
#GLOBAL: dfined at 0 indent
#LOCAL: dfined inside functions, also parameters are local vars
#Global can be used anywhere
todd = "coolguy"    #0 indent, global
#Local ONLY exist in context they were definded in
def other_function():
    global todd #In this function, todd refers to global
    smith = "notcoolguy"
    todd = "strangeguy"
    print(todd) #Strangeguy
    print(smith) #Notcool

print(todd) #strangeguy
print(smith) #LOCAL VARIABLE out of scope

#return functions
#functions cal aslo return values
#value returned is sent back to where function was called
#similar to varibles
#funct. does work and returns answer back
def add_2_numbers(x,y):
    solution = x+y
    return solution
print(add_2_numbers(10,5))
answer = add_2_numbers(10,16)
print(answer)

