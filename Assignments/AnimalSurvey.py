favorite_animal = input("What is your favorite animal?\n>")                     # Base question to determine fav. animal
print("So your favorite animal is a " + favorite_animal + ", cool!")            # Response to make it more interactive
animal_habitat = input("Where does this '" + favorite_animal + "' live?\n>")    # Habitat for later summary
print("Ah, '" + animal_habitat + "'. Sounds comfy!")                            # Response
input("What do they look like?\n>")                                             # Interactive only
print("Interesting...")
input("And what do they do?\n>")
print("Wow, that seems pretty cool actually.")
why = input("Why ARE they your favorite animal?\n>")                            # For summary
print("Ahhhh.")                                                                 # Response
food = input("What should this " + favorite_animal + " eat?\n>")                # For summary
print("I don't care much for " + food + ", as I am a computer system. But to each their own.")      # Interactive
print("So your favorite animal is the " + favorite_animal + " because " + why + ", they eat " + food + ", and they live at the '" + animal_habitat + "'.")     # Summary
print("Goodbye for now! I learned a lot about your favorite animal, the " + favorite_animal + "! I think it is quite interesting as well!") # Interactive goodbye