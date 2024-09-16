# import random
# while True:
#     choice = input("Do You want to play a Dice Rolling Game ? Select One :- (Y/N)").lower()

#     if choice == 'y':
#         dice1 = random.randint(1,6)
#         dice2 = random.randint(1,6)
#         print(f'{dice1},{dice2}')
#         break
#     elif choice == 'n':
#         print("Thank You for playing, Bye")
#         break
#     else:
#         print("Invalid Choice")


#TODO: Modify the program so the user can specify how many dice they want to roll.


# import random

# while True:
#     choice = input("Do you want to play a Dice Rolling Game? Select One :- (Y/N): ").lower()

#     if choice == 'y':
#         num_dice = int(input("How many dice would you like to roll? "))

#         dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]  # Roll the specified number of dice
#         print(f'You rolled: {", ".join(map(str, dice_rolls))}')
#         break

#     elif choice == 'n':
#         print("Thank you for playing, Bye!")
#         break

#     else:
#         print("Invalid choice, please select 'Y' or 'N'.")


#TODO:Add a feature that keeps track of how many times the user has rolled the dice during the session. This will require a counter that increments each time the dice are rolled.

import random

# Initialize the roll counter
roll_counter = 0

while True:
    choice = input("Do you want to play a Dice Rolling Game? Select One :- (Y/N): ").lower()

    if choice == 'y':
        num_dice = int(input("How many dice would you like to roll? "))

        # Roll the specified number of dice
        dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]
        print(f'You rolled: {", ".join(map(str, dice_rolls))}')
        
        # Increment the roll counter
        roll_counter += 1
        print(f'Total rolls in this session: {roll_counter}')
        
    elif choice == 'n':
        print(f"Thank you for playing! You rolled the dice {roll_counter} times. Goodbye!")
        break

    else:
        print("Invalid choice, please select 'Y' or 'N'.")
