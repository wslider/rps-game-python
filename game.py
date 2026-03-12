import random
inputs = ['rock', 'paper', 'scissors']

# get user input 
    # check against input list
    # if valid input - start game

user_choice = None

while user_choice not in inputs:
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    print(f"You chose {user_choice}")
    if user_choice not in inputs:
        print("Invalid input — try again.")
     
# generate computer input 
    # use random number to select input from list

computer_choice = inputs[random.randint(0,2)]
print(f"Computer chose {computer_choice}")

# if elif and else statements for possible results
    # print 
        # tie (if both are equal)
        # user wins
        # computer wins

if user_choice == computer_choice:
    print("It's a TIE!")
elif (
    (user_choice == 'rock'     and computer_choice == 'scissors') or
    (user_choice == 'paper'    and computer_choice == 'rock')     or
    (user_choice == 'scissors' and computer_choice == 'paper')
):
    print("You WIN!")
else:
    print("Computer WINS!")









