"""
Tic-Tac-Toe is a game in which two players seek in alternate turns 
to complete a row, a column, or a diagonal with either three x's or 
three o's drawn in the spaces of a grid of nine squares.
"""

#Top Row (L = Left, M = Middle, R = Right)
L1 = 1
M1 = 2
R1 = 3
#Middle Row (L = Left, M = Middle, R = Right)
L2 = 4
M2 = 5
R2 = 6
#Bottom Row (L = Left, M = Middle, R = Right)
L3 = 7
M3 = 8
R3 = 9

def main():
    carry_on = True
    player = "X"

    while (carry_on):
        show_grid()
        choice = input(f"\n{player}'s turn to choose a square (1-9): ")

        if choice == "0":
            carry_on = False
            


def show_grid():
    print(f"{L1}|{M1}|{R1}\n-+-+-\n{L2}|{M2}|{R2}\n-+-+-\n{L3}|{M3}|{R3}")

if __name__ == "__main__":
    main()