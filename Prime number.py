num = int(input("Enter your number: "))
factors = []

for number in range(2, num):
    if num%number == 0:
        factors.append(number)

if factors == []:
    print("Your number is a prime number.")
else:
    print(factors)
    print("Your number is not a prime number.")
