"""
Tic-Tac-Toe is a game in which two players seek in alternate turns 
to complete a row, a column, or a diagonal with either three x's or 
three o's drawn in the spaces of a grid of nine squares.
"""

def main():
    #Set starting players Icon and Loop Variable
    carry_on = True
    player = "X"

    #Top Row (L = Left, M = Middle, R = Right)
    L1 = "1"
    L1_open = True
    M1 = "2"
    M1_open = True
    R1 = "3"
    R1_open = True
    #Middle Row (L = Left, M = Middle, R = Right)
    L2 = "4"
    L2_open = True
    M2 = "5"
    M2_open = True
    R2 = "6"
    R2_open = True
    #Bottom Row (L = Left, M = Middle, R = Right)
    L3 = "7"
    L3_open = True
    M3 = "8"
    M3_open = True
    R3 = "9"
    R3_open = True

    while carry_on: #Main Game Loop
        show_grid(L1,M1,R1,L2,M2,R2,L3,M3,R3)

        while True: #Make sure we are given an Integer for option choices
            try:
                choice = int(input(f"\n{player}'s turn to choose a square (1-9): "))
                break
            except:
                print("Only single digit numbers between 1 and 9 accepted, try again.")

        if choice == 1 and L1_open: #Update L1
            L1 = player
            L1_open = False
            carry_on = check_score(player,L1,M1,R1,L2,M2,R2,L3,M3,R3)
            player = change_player(player)
        elif choice == 2 and M1_open: #Update M1
            M1 = player
            M1_open = False
            carry_on = check_score(player,L1,M1,R1,L2,M2,R2,L3,M3,R3)
            player = change_player(player)
        elif choice == 3 and R1_open: #Update R1
            R1 = player
            R1_open = False
            carry_on = check_score(player,L1,M1,R1,L2,M2,R2,L3,M3,R3)
            player = change_player(player)
        elif choice == 4 and L2_open: #Update L2
            L2 = player
            L2_open = False
            carry_on = check_score(player,L1,M1,R1,L2,M2,R2,L3,M3,R3)
            player = change_player(player)
        elif choice == 5 and M2_open: #Update M2
            M2 = player
            M2_open = False
            carry_on = check_score(player,L1,M1,R1,L2,M2,R2,L3,M3,R3)
            player = change_player(player)
        elif choice == 6 and R2_open: #Update R2
            R2 = player
            R2_open = False
            carry_on = check_score(player,L1,M1,R1,L2,M2,R2,L3,M3,R3)
            player = change_player(player)
        elif choice == 7 and L3_open: #Update L3
            L3 = player
            L3_open = False
            carry_on = check_score(player,L1,M1,R1,L2,M2,R2,L3,M3,R3)
            player = change_player(player)
        elif choice == 8 and M3_open: #Update M3
            M3 = player
            M3_open = False
            carry_on = check_score(player,L1,M1,R1,L2,M2,R2,L3,M3,R3)
            player = change_player(player)
        elif choice == 9 and R3_open: #Update R3
            R3 = player
            R3_open = False
            carry_on = check_score(player,L1,M1,R1,L2,M2,R2,L3,M3,R3)
            player = change_player(player)
        else:
            print(f"Option not available\n")

    print("") 
    show_grid(L1,M1,R1,L2,M2,R2,L3,M3,R3)
    print(f"\nGood game. Thanks for playing!")
            

            
            


def show_grid(L1,M1,R1,L2,M2,R2,L3,M3,R3): #Print out the game board
    print(f"{L1}|{M1}|{R1}")
    print(f"-+-+-")
    print(f"{L2}|{M2}|{R2}")
    print(f"-+-+-")
    print(f"{L3}|{M3}|{R3}")

def check_score(player,L1,M1,R1,L2,M2,R2,L3,M3,R3): #Check to see if there is a winner
    if L1 == player and M1 == player and R1 == player: #Row 1 Check
        winner = True
    elif L2 == player and M2 == player and R2 == player: #Row 2 Check
        winner = True
    elif L3 == player and M3 == player and R3 == player: #Row 3 Check
        winner = True
    elif L1 == player and M2 == player and R3 == player: #Diagonal 1 Check
        winner = True
    elif L3 == player and M2 == player and R1 == player: #Diagonal 2 Check
        winner = True
    elif L1 == player and L2 == player and L3 == player: #Left Column Check
        winner = True
    elif M1 == player and M2 == player and M3 == player: #Middle Column Check
        winner = True
    elif R1 == player and R2 == player and R3 == player: #Right Column Check
        winner = True
    elif (L1 == "X" or L1 == "O") and (L2 == "X" or L2 == "O") and (L3 == "X" or L3 == "O") and (M1 == "X" or M1 == "O") and (M2 == "X" or M2 == "O") and (M3 == "X" or M3 == "O") and (R1 == "X" or R1 == "O") and (R2 == "X" or R2 == "O") and (R3 == "X" or R3 == "O"): #Check if all are filled
        tie = True
        winner = False
    else:
        winner = False
        tie = False
    
    #Once winner is confirm to be true or false provide a response and either close or resume the game
    if winner == True or tie == True:
        carry_on = False
        if winner:
            print(f"\n{player} WINS!")
        elif tie:
            print(f"\nGame ended in a TIE!")
    elif winner == False or tie == False:
        carry_on = True

    return carry_on


def change_player(player_symbol): #Change player Icon
    if player_symbol == "X":
        next_player = "O"
    elif player_symbol == "O":
        next_player = "X"
    return next_player

if __name__ == "__main__":
    main()