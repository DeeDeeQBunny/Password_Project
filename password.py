# import random
import random

# boolean to keep game running
running = True

# password variable
password = random.randint(1000, 9999)

# while loop
while running:
    # input for the password
    answer = int(input("What is the password?"))

    # checks if the password if correct
    if answer == password:
        # if it is, print a message
        print("The password was correct. Welcome.")
        running = False
    # another condition...
    elif answer < password:
        # ...print a different message
        print("The password is incorrect(too low). Try again.")
    # otherwise...
    else:
        # ...print another different message
        print("The password is incorrect(too high). Try again.")