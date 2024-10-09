windspeed = input("What is the wind speed?\n>")
windspeed = int(windspeed)\

if windspeed < 74:
    print("Tropical storm.")
elif windspeed < 96:
    print("Cat 1 Hurricane.")
elif windspeed < 111:
    print("Cat 2 Hurricane.")
elif windspeed < 130:
    print("Cat 3 Hurricane.")
elif windspeed < 157:
    print("Cat 4 Hurricane.")
elif windspeed >= 157:
    print("Cat 5 Hurricane.")