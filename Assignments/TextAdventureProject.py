name = "Input Name"
gender = "Input Gender"
interest = "Interest"
def start():
    global name
    global gender
    global interest
    
    print("\n\nWelcome! This is the text adventure game made by Kaden Bartunek.\n ")
    name = str(input("Choose your name:\n(How you want characters to refer to you)\n> ")).capitalize()
    print("Welcome, "+name+"!")
    
    gender = str(input("Next, choose your gender. Please choose M, F, or O (Other):\n>")).lower()
    interest = str(input("Romantic interest? Please type 'B'(boyfriend), 'G'(girlfriend), or 'P'(partner).\n> ")).lower()
    if interest == "b":
         interest = "boyfriend"
    elif interest == "g":
         interest = "girlfriend"
    elif interest == "p":
         interest = "partner"
    else:
         print("Choose only b, g, or f.\n\n\n")
         start()
    if interest == "boyfriend" or "girlfriend" or "partner":
        print("\n\n\nPerfect! Let's start! If you have options, answer with the corresponding number. Do not type out 'one', for example. Type '1' instead.\n\n\n")
    else:
         print("Please retry. Something went wrong. Sorry!")
         start()
start()

def step1():
        try:
            choice1 = int(input("You are sitting in your room, scrolling through Instagram reels on your phone.'" + name + "!' You"+
                                " hear your "+interest+" call your name. Do you: \n 1. Do nothing. \n 2. Call back. \n 3. Go downstairs.\n\n>"))
            if choice1 == 1:
                print("The reel you are watching must be important. You hear a crash downstairs after a minute, followed by a scream.")
                choice2 = int(input("Do you\n 1. Investigate \n 2. Watch another reel \n 3."))                              #ADD CHOICESSSSS!!!!!!!!

            elif choice1 == 2:
                choice2 = int(input("'Yeah?' You call back. Your "+interest+" calls back a moment later. They sound nervous, which isn't like them."+
                                    " 'I saw something outside! Can you come down?'\n 1. Yes\n 2. No\n>")).lower()
                if choice2 == 1:
                     print("'Yeah, I'll be right down!' You respond.")                                                         #FINISH THIS

            elif choice1 == 3:
                print("You attempt to pocket your phone and go downstairs. They sounded urgent. "+
                      "Unfortunately, you fall down the stairs while still fumbling with your phone, breaking your neck. Tough luck, retry?")
                redo = str(input("\nRetry? \nY \nN \n\n> ")).upper()
                if redo == "Y":
                     print("Yay!")
                     step1()
                elif redo == "N":
                     print("Lame, whatever. Bye.")
                else:
                     print("Not sure what that means... RESTART IT IS! HAHAHAHAHAHAAA")
                     start()

            else:
                 print("Please try again, something went wrong.")
                 step1()

        except ValueError: 
             print("\n\nNot funny. Next time, input a number like this: 1  OR  2. We already explained that."+
                   " Restart the story and read the rules this time.\n")
             start()
step1()