def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(board):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c]:
            return True

    return False


def play_game():
    board = ["1", "2", "3", "4", "5",
             "6", "7", "8", "9"]

    current_player = "X"

    for turn in range(9):
        display_board(board)

        print("Player", current_player)

        choice = int(input("Enter a number (1-9): "))

        while choice < 1 or choice > 9 or board[choice - 1] in ["X", "O"]:
            print("Invalid choice. Try again.")
            choice = int(input("Enter a number (1-9): "))

        board[choice - 1] = current_player

        if check_winner(board):
            display_board(board)
            print("Player", current_player, "wins!")
            return

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    display_board(board)
    print("It's a draw!")


play_game()