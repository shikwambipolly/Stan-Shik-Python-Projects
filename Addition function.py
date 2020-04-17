def addition(a, b):
    sum = a + b
    return sum
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
answer = addition(int(number1), int(number2))
print("What is number1 + number2? "+ str(answer))

input("Press enter to exit")
