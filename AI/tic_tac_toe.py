import random

board = [" " for i in range(9)]

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check_winner(player):
    winning_positions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    for position in winning_positions:
        if board[position[0]] == board[position[1]] == board[position[2]] == player:
            return True
    return False

def board_full():
    return " " not in board

print("Board Positions")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:
    print_board()

    move = int(input("Enter your position (1-9): ")) - 1

    if board[move] == " ":
        board[move] = "X"
    else:
        print("Position already taken.")
        continue

    if check_winner("X"):
        print_board()
        print("Congratulations! You win!")
        break

    if board_full():
        print_board()
        print("Match Draw!")
        break

    available = []
    for i in range(9):
        if board[i] == " ":
            available.append(i)

    ai_move = random.choice(available)
    board[ai_move] = "O"
    print("AI placed O.")

    if check_winner("O"):
        print_board()
        print("AI wins!")
        break

    if board_full():
        print_board()
        print("Match Draw!")
        break

