import time
import sys


try:
    x = int(input("Enter your number: "))
except ValueError:
    print("You have not entered a number.")
    time.sleep(3)
    sys.exit()


pm = []

def pmchecker(x):
    status = ''
    for i in range(2,x):
        if x%i == 0:
            status = 'not_prime'
            break
    if status == '':
        return True
    else:
        return False

def pmlister(x):
    for i in range(4, x):
        if pmchecker(i) is True:
            pm.append(i)
    print(pm)


pmlister(x)