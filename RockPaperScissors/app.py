import random
choices = ('r','p','s')

while True:
    #user selection
    userSelection= input("Please Select your choice (r/p/s) : ").lower()
    #validate user choices
    if userSelection not in choices:
        print("Invalid Choice, please select any from (r/p/s)!")
        continue


    #computer selection
    computerSelection = random.choice(choices)

    symbols={'r':'🪨', 'p':'🔖','s':'✂️'}

    #print the selections

    print(f"You selected:  {symbols[userSelection]}")
    print(f"Computer selected : {symbols[computerSelection]}")



    # comparing the selection find the winner
    if (userSelection == computerSelection):
        print("Tie")
    elif(
    (userSelection == 'r' and computerSelection == 's') or \
    (userSelection == 's' and computerSelection == 'p') or \
    (userSelection == 'p' and computerSelection == 'r')):
        print("Congrtualaitons! You Won")
    else :
        print("Sorry, You lost!")

    wantToContinue = input("Do you want to continue playing? (Yes/No) : ").lower()
    if wantToContinue == 'no':
        break