import random
def end():
    print("\n\n\nWow\n\n\n")
def drop_item():
    roll = random.randint(0,10000)
    if roll < 7000:
        print("COMMON")
    elif roll<9000:
        print("UNCOMMON")
    elif roll<9990:
        print("RARE")
    elif roll<9999:
        print("LEGENDARY")
        end()
    elif roll<10000:
        print("UNREAL")
        end()
    drop_item()

drop_item()