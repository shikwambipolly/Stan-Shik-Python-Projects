Tn = input("Enter Tn :")
a = input("Enter a: ")
n = input("Enter n: ")
d = input("Enter d: ")

if Tn == "?":
    Tn = int(a) + (int(n) - int(1)) * int(d)
    print("Tn is equal to: " + str(Tn))
elif a == "?":
    a = int(Tn) - (int(n) - int(1)) * int(d)
    print("a is equal to: " + str(a))
elif n == "?":
    n = ((int(Tn) - int(a)) / int(d)) + int(1)
    print("n is equal to: " + str(n))
elif d == "?":
    d = (int(Tn) - int(a)) / (int(n) - int(1))
    print("d is equal to: " + str(d))

input("Press enter to exit")