name = "Input Name"     # Fun interactive bit
gender = "Input Gender" # Useless but it makes people think they have more control than they actually do, adds fake depth. Also buggy for some reason?
interest = "Interest"   # Dont ignore cries for help
weapon = "Weapon"       # Only bat wins the game

import time 
import sys              # If you get errors, future Kaden, I'm so sorry lmao. Prob just replace guts of typewrite functions with the plain print (?)

def typewritefast(text):# Please work at school
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.027) 
        #print(text)

def typewrite(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
        #print(text)

def typewriteslow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.077) 
        #print(text) 

def typewriteslowest(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15) 
        #print(text)

def secret():
     typewriteslowest("???")

def basementbat(): # number 2 of the 2 possible ways to win
     try:     
          typewrite("Thankfully, you reach the stairs to the basement. You can already hear the sound of a creature down there, but don't want to turn back now.")
          fightorhide = int(input("You have two choices. \n 1. Fight \n 2. Hide \n\n> "))

          if fightorhide == 1:
               typewrite("\n\nYou approach the creature from behind, only a faint outline visible in the dark. You hit it hard over the head, dropping it to the floor. You quickly hide after.\n")
               endwin()
          elif fightorhide == 2:
               typewrite("You attempt to sneak past the creature and hide in a room. The door to the room creaks, however, and you are dead before you can even turn around to defend yourself.")
               enddead()

     except ValueError:
          typewritefast("\nERR: input 1 or 2. \nYou're so close! Don't give up now!")
          basementbat()

def basementstool():
     try:
          print("In the basement, there is obvious breathing as well. You may need to fight. You ready the heavy stool in your hands, but you can't tell where the breathing is.")
          fightorhide = int(input("\nFight or hide? \n\n 1. Fight \n 2. Hide\n\n> "))
          
          if fightorhide == 1:
               typewrite("\n\nYou swing the stool at a faint outline of a creature when you spot it. Upon contact, the welds of the stool fail, and it breaks apart. The creature recovers quickly and tears you apart.\n")
               enddead()
          
          elif fightorhide == 2:
               typewrite("\n\nBad choice. The creature hears you bump something with the unweildy stool.\n")
               enddead()
          
          else:
               typewriteslowest(": )")
               basementstool()

     except ValueError:
          typewriteslowest("No escape \n\n\n: ) \n\n ")
          basementstool()

def enddead():
     typewrite("\n\n\n\nThanks for playing! You got too far in the story to be redeemed, a full reset would be more practical than a checkpoint reset, as most (or all) ways lead to death.\n\n")

def endwin():
     typewrite("\n\nYou survived! Wow, didn't expect that. There are only TWO ways to win ;)\n THANKS FOR PLAYING!!!!")

def downlightoff():
     typewrite("\nYou faintly make out the twisted figure of some sort of beast. On the floor, there is a corpse.") 
     location = int(input("\nYou get the feeling you need to hide somewhere.\n 1. Basement \n 2. Shed \n\n> "))
     if location == 1:
          typewrite("You carefully head to the basement, the house filled with heavy breathing. Unfortunately, a creature resides down there, and you have no weapon.")
          enddead()
     elif location == 2:
          typewrite("You make your way outside as silently as possible. You really shouldn't have.")
          enddead()

def downstairsbad():
     typewrite("\nYou make your way downstairs, phone in hand. A heavy weight is in the air, feeling like a thick slurry. The house is unnaturally dark. Audible heavy panting is heard.\n\n")
     light = int(input("Turn on phone flashlight? \n 1. Y \n 2. N\n\n> ").upper())
     if light == 1:
          typewrite("The glint of inhuman eyes flash in the dark. You are dead.")
          redo1()
     elif light == 2:
          typewrite("You decide to not turn on the flashlight, that could give away where you are.")
          downlightoff()

def downstairsbat():
     try:
          typewrite("You grab your old wooden bat and head downstairs cautiously.") 
        
          somewhere = str(input("\nYou get the feeling you need to hide somewhere.\n 1. Basement \n 2. Shed \n\n> "))
          if somewhere == "1":
               typewrite("You carefully maneuver to the basement, the house familiar even in darkness. Heavy, deep breathing is heard around the house.")
               basementbat()

          elif somewhere == "2":
               typewrite("Should have stayed indoors. You got swarmed. You fought hard with the bat, black blood staining its splintering length, 20 creatures at your feet before you meet your inevitable demise.")
               enddead()

          else:
               print("\n\n1 or 2.\n\n")
     except ValueError:
          typewrite("No.")
          downstairsbat()

def downstairstrophy():
     typewrite("You grab the trophy at the base, and head downstairs. The glint of the metal catches the eye of a bloody and horrifying creature, which kills you.")
     redo2()

def downstairsstool():
     try:
          typewrite("\n\nYou decide to grab the heavy metal stool. Unfortunately, you aren't the strongest, so it feels quite unweildy. You head downstairs, careful not to "+
                "bang the stool and make noise on the way.\n")
          location = int(input("\nYou get the feeling you need to hide somewhere.\n 1. Basement \n 2. Shed \n\n> "))
          if location == 1:
               typewrite("You carefully maneuver to the basement, the house familiar even in darkness. Heavy, deep breathing is heard around the house.")
               basementstool()

          elif location == 2:
               typewrite("Should have stayed indoors. You got swarmed. Only a broken, red-stained stool remains on the ground.")
               enddead()

          
     except ValueError:
          typewrite("Your mental foolery wont work on me.")
          downstairsstool()

def downstairsgood(): # number 1 of the 2 possible ways to win
     try:
          typewrite("\nUpon arriving downstairs, you see your "+interest+" standing a distance from the window, and staring out. They seem frightened.")
          typewrite("They turn to look at you for a moment, before turning back to the window. 'Something weird is going on.'\n"+
                "You feel a notification from your phone, but ignore it.")
          
          location = int(input("\nYou get the feeling you need to hide somewhere.\n 1. Basement \n 2. Shed \n\n> "))
         
          if location == 1:
               typewrite("Good choice. You hide in the basement, locking the door to a room and hiding in the attached bathroom. You hear crashing around the house for hours, heavy breathing approaches your location at one point. You comfort your "+interest+"."+
               "It leaves after a minute.\n\n ")
               endwin()
          
          elif location==2:
               typewrite("You get swarmed by horrifying creatures, torn apart while standing.")
               redo1()

     except ValueError:
          print("\nPlease don't.\n")
          downstairsgood()

def weaponchoice():
    try: 
         typewrite("You have a few items that could be used as a weapon in your room.")
         weapon = str(input("\n 1. Wooden Bat \n 2. Metal Trophy \n 3. Metal Stool\n\n> "))
         if weapon=="1":
              downstairsbat()

         elif weapon=="2":
              downstairstrophy()

         elif weapon=="3":
              downstairsstool()

         else:
            print("\n Please choose 1, 2, or 3.")
    
    except ValueError:
         typewrite("\n\nNot funny. Next time, input a number like this: 1  OR  2. We already explained that."+
                   " Restart the story and read the rules this time.\n")
         start()

def redo1():
     try:     
          redo = int(input("\nReset? \n 1. Yes, reset \n 2. No, leave \n\n> "))
          if redo == 1:
               print("Yay!")
               go()
          elif redo == 2:
               print("Bye.")
          else:
               print("\n\nNot sure what that means... RESTART IT IS! HAHAHAHAHAHAAA (Stop putting in random numbers. Really.)\n\n")
               start()

     except ValueError:
          typewrite("\n\n\n\n\n\nI explained this. Get out.\n\n")

def redo2():
     try:     
          redo = int(input("\nReset? \n 1. Yes, reset \n 2. No, leave \n\n> "))
          if redo == 1:
               typewrite("\nYay!\n")
               weaponchoice()
          elif redo == 2:
               typewrite("\nBye.\n")
          else:
               print("Not sure what that means... RESTART IT IS! HAHAHAHAHAHAAA (Stop putting in random numbers. Really.)\n\n")
               start()

     except ValueError:
          print("\n\n\n\n\n\nGet out.\n\n")

def go():                         # Wanted to test out nested if statements... yikes        
        try:
            typewrite("You are sitting in your room, scrolling through Instagram reels on your phone.'" + name + "!' You"+
                                " hear your "+interest+" call your name. Do you: \n 1. Do nothing. \n 2. Call back. \n 3. Go downstairs.")
            choice1 = int(input("\n\n> "))
            if choice1 == 1:
                typewrite("The reel you are watching must be important. You hear a crash downstairs after a minute, followed by a scream.\n")
                choice2 = int(input("\nDo you\n 1. Investigate \n 2. Watch another reel \n 3. Look for a weapon.\n\n> "))
               
                if choice2 == 1:
                     downstairsbad() #Death
             
                elif choice2 == 2:
                     typewritefast("You watch another reel. As you are watching, a notification pops up. It reads: 'WARNING: THIS IS A PUBLIC SERVICE ANNOUNCMENT.")
                     typewritefast(" Creatures have been spotted around your area. They are of unknown origin and seem to be extremely hostile. Stay indoors, may God have mercy on us all.'\n\n")
                     typewrite("It lists many areas where the creatures have appeared. You decide to grab a weapon and head downstairs.\n\n")
                     weaponchoice()

                elif choice2 == 3:
                     weaponchoice() #1 way to live
                
                else:
                     print("ERR: Please choose 1 or 2.")

########################################################################################################################################## CHOICE 2 #######################################################################################################################################                 

            elif choice1 == 2:
                typewrite("'Yeah?' You call back. Your "+interest+" calls back a moment later. They sound nervous, which isn't like them."+
                                    " 'I saw something outside! Can you come down?'\n 1. Yes\n 2. No\n")
                choice2 = int(input("\n> "))
                if choice2 == 1:
                     print("'Yeah, I'll be right down!' You respond. You pocket your phone and make your way downstairs.")
                     downstairsgood()
                elif choice2 == 2:
                     typewrite("\nYou ignore the cry for help. The reel you are watching must be important. You hear a crash downstairs after a minute, followed by a scream.\n")
                     typewriteslowest("\n\nYou know what you did.\n\n")
                     typewriteslowest("Footsteps slowly ascend the stairs to your room.\nNowhere to run.")
                     redo1()

                else:
                    print("Something went wrong. Please retry")
                    go()

########################################################################################################################################## CHOICE 3 #######################################################################################################################################

            elif choice1 == 3:
                    typewrite("You attempt to pocket your phone and go downstairs. They sounded urgent. "+
                          "Unfortunately, you fall down the stairs while still fumbling with your phone, breaking your neck. Tough luck, retry?")
                    redo1()
            
            elif choice1 ==13211:
                    print("[[https://www.youtube.com/watch?v=C6jEJraEu6Q&ab_channel=DameAndThatGame]]")
                    secret()

            else:
                 print("Please try again, something went wrong.")
                 go()

        except ValueError: 
             print("\n\nNot funny. Next time, input a number like this: 1  OR  2. We already explained that."+
                   " Restart the story and read the rules this time.\n")
             start()

####################################################################################################################################START OF STORY#####################################################################################################################

def start():
    global name
    global gender
    global interest
    
    typewrite("\n\nWelcome! This is the text adventure game made by ")
    typewriteslow("Kaden Bartunek.\n")
    name = str(input("Choose your name:\n(How you want characters to refer to you)\n> ")).capitalize()
    typewrite("Welcome, "+name+"!\n")
    
    gender = str(input("\nNext, choose your gender. Please choose M, F, or O (Other):\n\n> ")).lower()
    if gender == "m" or "f" or "o" or "m " or "f " or "o ":
        typewrite("Romantic interest? Please type 'B'(boyfriend), 'G'(girlfriend), or 'P'(partner).")
        interest = str(input("\n> ")).lower()
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
            typewrite("\n\n\nPerfect! Let's start! If you have options, answer with the corresponding number. Do not type out 'one', for example. Type '1' instead.\n\n\n")
        else:
             print("Please retry. Something went wrong. Sorry!")
             start()
    else:
         print("Choose ONLY M, F, or O.")
    go()
start()