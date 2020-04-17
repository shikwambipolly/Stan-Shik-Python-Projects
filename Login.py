name = input("Enter name here: ")
password = input("Enter password here: ")

while name == "Stanley":
    if password == "st.pauls":
        print("Login successful!!")
        break
    else:
        print("Incorrect passowrd, try again!!")
        break

while name != "Stanley":
    if password != "st.pauls":
        print("Incorrect Username or Password!!")
        break
    else:
        print("Incorrect Password or Username!!")
        break

input("Press enter to exit")