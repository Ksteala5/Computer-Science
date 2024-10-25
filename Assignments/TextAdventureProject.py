def downstairsbad():
     print("\nYou make your way downstairs, phone in hand. A heavy weight is in the air, feeling like a thick slurry. The house is unnaturally dark. Audible heavy panting is heard.\n\n")
     light = int(input("Turn on phone flashlight? \n 1. Y \n 2. N\n\n> ").upper())
     if light == 1:
          print("The glint of inhuman eyes flashes in the dark. You are dead.")
          redo1()

def downstairsbat():
     print("You grab your old wooden bat and head downstairs cautiously.")

def downstairstrophy():
     print()

def downstairsstool():
     print()

def downstairsgood():
     print("\nUpon arriving downstairs, you see your "+interest+" standing a distance from the window, and staring out. They seem frightened.")
     print("They turn to look at you for a moment, before turning back to the window. 'Something weird is going on.'\n"+
           "You feel a buzz from your phone, but ignore it.")

def weaponchoice():
    global weapon
    try: 
         weapon = int(input("You have a few items that could be used as a weapon in your room. \n 1. Wooden Bat \n 2. Metal Trophy \n 3. Metal Stool\n\n> "))
         if weapon==1:
              weapon = "bat"
              print("You pick up the "+weapon+" and head downstairs.")
              downstairsbat()

         elif weapon==2:
              weapon = "trophy"
              print("You pick up the "+weapon+" and head downstairs.")
              downstairstrophy()

         elif weapon==3:
              weapon = "stool"
              print("You pick up the "+weapon+" and head downstairs.")
              downstairsstool()

         else:
            print("\n Please choose 1, 2, or 3.")
    
    
    except ValueError:
         print("\n\nNot funny. Next time, input a number like this: 1  OR  2. We already explained that."+
                   " Restart the story and read the rules this time.\n")
         start()

def redo1():
     try:     
          redo = int(input("\nReset? \n 1. Y \n 2. N \n\n> "))
          if redo == 1:
               print("Yay!")
               go()
          elif redo == 2:
               print("Lame, whatever. Bye.")
          else:
               print("Not sure what that means... RESTART IT IS! HAHAHAHAHAHAAA (Stop putting in random numbers. Really.)\n\n")
               start()

     except ValueError:
          print("\n\n\n\n\n\nGet out.\n\n")

name = "Input Name"
gender = "Input Gender"
interest = "Interest"
weapon = "Weapon"
def start():
    global name
    global gender
    global interest
    
    print("\n\nWelcome! This is the text adventure game made by Kaden Bartunek.\n ")
    name = str(input("Choose your name:\n(How you want characters to refer to you)\n> ")).capitalize()
    print("Welcome, "+name+"!")
    
    gender = str(input("Next, choose your gender. Please choose M, F, or O (Other):\n\n> ")).lower()
    if gender == "m" or "f" or "o":
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
    else:
         print("Choose ONLY M, F, or O.")
start()

     
def go():
        try:
            choice1 = int(input("You are sitting in your room, scrolling through Instagram reels on your phone.'" + name + "!' You"+
                                " hear your "+interest+" call your name. Do you: \n 1. Do nothing. \n 2. Call back. \n 3. Go downstairs.\n\n> "))
            if choice1 == 1:
                print("The reel you are watching must be important. You hear a crash downstairs after a minute, followed by a scream.\n")
                choice2 = int(input("\nDo you\n 1. Investigate \n 2. Watch another reel \n 3. Look for a weapon.\n\n> "))
               
                if choice2 == 1:
                     downstairsbad()
             
                elif choice2 == 2:
                     print("You watch another reel. As you are watching, a notification pops up. It reads: 'Warning: This is a public service announcement. Creatures"+
                           " have been spotted around your area. They are of unknown origin and seem to be extremely hostile. Stay indoors, may God have mercy on us all.'"+
                           " It lists many areas where the creatures have appeared. You decide to grab a weapon and head downstairs.\n\n")
                     weaponchoice()

                elif choice2 == 3:
                     weaponchoice()
                
                else:
                     print("Please choose 1 or 2.")
                     
            elif choice1 == 2:
                choice2 = int(input("'Yeah?' You call back. Your "+interest+" calls back a moment later. They sound nervous, which isn't like them."+
                                    " 'I saw something outside! Can you come down?'\n 1. Yes\n 2. No\n> "))
                if choice2 == 1:
                     print("'Yeah, I'll be right down!' You respond. You pocket your phone and make your way downstairs.")
                     downstairsgood()
                elif choice2 == 2:
                     print("You ignore the cry for help. The reel you are watching must be important. You hear a crash downstairs after a minute, followed by a scream.\n")

            elif choice1 == 3:
                    print("You attempt to pocket your phone and go downstairs. They sounded urgent. "+
                          "Unfortunately, you fall down the stairs while still fumbling with your phone, breaking your neck. Tough luck, retry?")
                    redo1()

            else:
                 print("Please try again, something went wrong.")
                 go()

        except ValueError: 
             print("\n\nNot funny. Next time, input a number like this: 1  OR  2. We already explained that."+
                   " Restart the story and read the rules this time.\n")
             start()
go()