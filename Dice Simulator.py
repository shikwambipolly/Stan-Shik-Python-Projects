import random

di1 = [1, 2, 3, 4, 5, 6]
di2 = [1, 2, 3, 4, 5, 6]

while 0 == 0:
    di1face = random.choice(di1)
    di2face = random.choice(di2)
    print("First di is " + str(di1face) + ". Second di is " + str(di2face) + ". Total is " + str(int(di1face) + int(di2face)))
    action = input("Roll again? y or n: ")
    if action == "n":
        break

print("Press enter to exit")