import random
while True:
    choice = input("Do You want to play a Dice Rolling Game ? Select One :- (Y/N)").lower()

    if choice == 'y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f'{dice1},{dice2}')
        break
    elif choice == 'n':
        print("Thank You for playing, Bye")
        break
    else:
        print("Invalid Choice")



