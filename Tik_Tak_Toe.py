# Display The Board
def display(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def heuristic(board):
    win = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),  # Horizontal
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),  # Vertical
        (0, 4, 8),
        (2, 4, 6),  # Diagonal
    ]
    for a, b, c in win:
        if board[a] == board[b] == board[c] == "X":
            return 1
        if board[a] == board[b] == board[c] == "O":
            return -1
    return 0


board = [" "] * 9
player = "X"

for turn in range(9):
    display(board)
    print("Player", player)

    try:
        position = int(input("Enter Position(1-9): ")) - 1
    except ValueError:
        print("Invalid Input! Please enter a number between 1 and 9.")
        continue

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid Position! ...Try Again.....")
        continue

    board[position] = player
    score = heuristic(board)

    if score == 1:
        display(board)
        print("Player X wins!")
        break

    if score == -1:
        display(board)
        print("Player O wins!")
        break

    # Switch turn
    if player == "X":
        player = "O"
    else:
        player = "X"
else:
    # Triggers if loop finishes 9 turns without a break
    display(board)
    print("Game Draw!")
