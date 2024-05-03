import random
while True:
    possible_choice = "ROCK"   , "PAPER " ,  "SCISSOR" 
    user_choice  = input("choose between ROCK PAPER AND SCISSOR") 
    computer_choice = random.choice(possible_choice)
    print("you choose" , user_choice)
    print("computer choose",computer_choice)

    if user_choice == computer_choice:
        print(f"its a Tie")
    elif user_choice == "ROCK":
        if computer_choice == "SCISSOR":
            print("ROCK SMASHES SCISSOR AND WINNER IS ROCK")
        else:
            print("PAPER HOLDS THE ROCK AND WINNER IS PAPER")

    elif user_choice == "PAPER" :
        if computer_choice == "SCISSOR" :
            print("SCISSOR CUTS THE PAPER AND WINNER IS SCISSOR")
        else:
            print("PAPER HOLDS THE ROCK AND WINNER IS PAPER")
    elif user_choice == "SCISSOR" :
        if computer_choice == "ROCK" :
            print("ROCK SMASHES SCISSOR AND WINNER IS ROCK")
        else:
            print("SCISSOR CUTS THE PAPER AND WINNER IS SCISSOR")
        
        exit = input("\nWould you like to play game? Y/N")
    if exit=="N":
        break
print("THANKS FOR PLAYING  VISIT SOON !!!" )