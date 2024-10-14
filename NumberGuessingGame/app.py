# import random

# number = random.randint(1,100)

# playerNumber = int(input("Guess The Number between 1 and 100 : "))

# if playerNumber > number:
#     print("Too High , Guess Again")
# elif playerNumber < number:
#     print("Too Low, Guess Again")
# elif playerNumber == number:
#     print("Congratulations, You guessed the number")
    

# print(number)



import random

number = random.randint(1, 100)

while True:
    try:
        playerNumber = int(input("Guess the number between 1 and 100: "))
        if playerNumber > number:
            print("Too High, Guess Again")
        elif playerNumber < number:
            print("Too Low, Guess Again")
        else:
            print("Congratulations, You guessed the number!")
            break  # Exit the loop when the correct number is guessed
    except ValueError:
        print("Please Enter a valid Number! And Try Again")