row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['', '', '']


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


def user_choise():
    choise = input("Please enter a number (1-9)")
    while not choise.isdigit() or (int(choise) not in range(1, 10)):
        if not choise.isdigit():
            print("Sorry, your choise is not valid")
        else:
            print("Your choise is not within range 1-9")
        choise = input("Please enter a number (1-9)")


user_choise()
display(row1, row2, row3)
