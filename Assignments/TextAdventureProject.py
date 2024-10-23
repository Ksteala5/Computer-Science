name = "Input Name"
gender = "Input Gender"
interest = "Interest"
def start():
    global name
    global gender
    global interest
    print("Welcome! This is the text adventure game made by Kaden Bartunek.")
    name = str(input("Choose your name:\n(How you want characters to refer to you)\n>")).capitalize()
    print("Welcome, "+name+"!")
    gender = str(input("Next, choose your gender. Please choose M, F, or O (Other):\n>")).lower()
    interest = str(input("Romantic interest? Input 'Boyfriend', 'Girlfriend', or 'Partner'.\n>")).lower()
    print("Perfect! Let's start!")
start()

def step1():
        choice1 = int(input(" You are sitting in your room, scrolling through Instagram reels on your phone.'" + name + "!' You"+
                            " hear your "+interest+" call your name. Do you: \n 1. Do nothing. \n 2. Call back. \n 3. Go downstairs.\n>"))
        if choice1 == 1:
            print("The reel you are watching must be important. You hear a crash downstairs after a minute.")
            choice2 = input("Do you\n 1. Investigate")
       
        elif choice1 == 2:
            choice2 = str(input("'Yeah?' You call back. Your "+interest+" calls back a moment later. They sound nervous, which isn't like them. 'I saw something outside! Can you come down?'\n 1. Yes\n 2. No\n>")).lower()
       
        elif choice1 == 3:
            print("You attempt to pocket your phone and go downstairs. They sounded urgent. Unfortunately, you fall down the stairs while still fumbling with your phone, breaking your neck. The End.")
       
        else:
            print("Please try again, something went wrong.")
            step1()

step1()