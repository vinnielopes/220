"""
Name: Vinicius Nunes Lopes
lab10.py
"""

def build_board():
        board = [1,2,3,4,5,6,7,8,9]
        return board

def display_board(board):
    print("-" * 7)
    counter = 0
    for i in range(1,4):
        print("|", end="")
        for j in range(3):
            print(board[counter], end="|")
            counter += 1
        print(end="\n")
    print("-" * 7)

def place_Spot(board, spot, marker):
    board[spot - 1] = marker

def legal_spot(board, spot):
    if (board[spot - 1] == "x" or board[spot - 1] == "o") or (spot < 1 or spot > 9):
        return False
    return True

def game_won(board):
    winCon = [[1,2,3], [4,5,6], [7,8,9],[1,4,7], [2,5,8],[3,6,9], [1,5,9],[3,5,7]]
    for condition in winCon:
        counterx = 0
        countery = 0
        for spot in condition:
            if board[spot - 1] == "x":
                counterx += 1
            if counterx == 3:
                return "X wins"
            if board[spot - 1] == "o":
                countery += 1
            if countery == 3:
                return "Y wins"

def game_over(board, turnCount):
    if(game_won(board) == "X wins" or game_won(board) == "Y wins") or (turnCount > 9):
        return True
    return False

def play_Game():
    # Build the board
    board = build_board()
    # Display the board
    display_board(board)

    turnCount = 0
    while not game_over(board, turnCount):
        spot = eval(input("Choose a number from the board:"))
        marker = input("Are you x or o? ")
        if legal_spot(board, spot) == True:
            place_Spot(board, spot, marker)
            turnCount += 1
        else:
            print("That is not a legal move! Try again!")
        display_board(board)

    if game_won(board) == "X wins":
        print("Player x wins!")
    elif game_won(board) == "Y wins":
        print("Player y wins!")
    elif game_won(board) == turnCount > 9:
        print("The game ended in a tie!")

def main():
    play_Game()
    pass


if __name__ == '__main__':
    main()
