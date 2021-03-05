
while True:
    player_or_computer = input("Would you like to play the computer (cpu) or player2 (p2): " )
    if player_or_computer == "cpu" or player_or_computer=="p2":
        break
    print("Your choice was invalid!")
    


while True:
    number_of_sticks = int(input("select your sticks between (0-21)"))
    if number_of_sticks>=0 and number_of_sticks<=21:
        print("Get ready to play")
        break
    print("Your choice was invalid!")



##starting the game
while number_of_sticks>0:
    #turns            
    for whose_turn in range(1,3):
        if whose_turn ==1:
            print("It's Player 1 turn")
        elif whose_turn ==2:
            print("It's cpu turn")
        if number_of_sticks==2:
            max_sticks=2
        if number_of_sticks==1:
            max_sticks=1
        if number_of_sticks>2:
            max_sticks=3

       
        while True:         
            print("How many sticks are you taking off? (1-{max_sticks})".format(max_sticks=min(3,max_sticks)))
            sticks_taken = int(input("Enter your choice: "))
            if sticks_taken>=1 and sticks_taken<=max_sticks:
                print("You have taken off", sticks_taken, "sticks")
                break
            else:
                print ("you did wrong choice, please pick 1,2, or 3 ")
                

        number_of_sticks-=sticks_taken
        print("and there are", number_of_sticks, "left")
        if number_of_sticks==0:
            break
            
if whose_turn==1:
    print("Congrats Player 2!!! You are the winner!!!")
if whose_turn==2:
    print("Congrats Player 1!!! You are the winner!!!")
    
    
while True:   
    play_again=input("Would you like to play again? Please enter (0) for YES or (1) for NO: ")
    if play_again==0:
        print("Would you like to play the computer (cpu) or player2 (p2)")
    else: play_again==1
    print("Thanks for playing! Have a good day!")
    break
