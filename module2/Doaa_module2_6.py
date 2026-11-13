import random

def display_board(board):
    print("\n2048 GAME")
    for row in board:
        for number in row:
            if number == 0:
                print(".", end="\t")
            else:
                print(number, end="\t")
        print()


def add_tile(board):
    empty = []

    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                empty.append((r, c))

    if empty:
        r, c = random.choice(empty)

        if random.randint(1, 10) == 1:
            board[r][c] = 4
        else:
            board[r][c] = 2


def move_left(board):
    new_board = []
    score = 0

    for row in board:
        numbers = []

        for number in row:
            if number != 0:
                numbers.append(number)

        new_row = []
        i = 0

        while i < len(numbers):
            if i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:
                new_number = numbers[i] * 2
                new_row.append(new_number)
                score += new_number
                i += 2
            else:
                new_row.append(numbers[i])
                i += 1

        while len(new_row) < 4:
            new_row.append(0)

        new_board.append(new_row)

    return new_board, score


def move_board(board, direction):
    new_board = [row[:] for row in board]

    if direction == "D":
        new_board = [row[::-1] for row in new_board]

    elif direction == "W" or direction == "S":
        new_board = [list(row) for row in zip(*new_board)]

        if direction == "S":
            new_board = [row[::-1] for row in new_board]

    new_board, score = move_left(new_board)

    if direction == "D":
        new_board = [row[::-1] for row in new_board]

    elif direction == "W":
        new_board = [list(row) for row in zip(*new_board)]

    elif direction == "S":
        new_board = [row[::-1] for row in new_board]
        new_board = [list(row) for row in zip(*new_board)]

    return new_board, score


def play_game():
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    score = 0

    add_tile(board)
    add_tile(board)

    while True:
        display_board(board)
        print("Score:", score)
        print("W = Up, S = Down, A = Left, D = Right")

        direction = input("Enter your move: ").upper()

        if direction not in ["W", "A", "S", "D"]:
            print("Invalid input. Try again.")
            continue

        new_board, points = move_board(board, direction)

        if new_board == board:
            print("No movement possible in this direction.")
            continue

        board = new_board
        score += points

        if any(2048 in row for row in board):
            display_board(board)
            print("You win! You reached 2048!")
            print("Final score:", score)
            break

        add_tile(board)

        if all(0 not in row for row in board):
            possible_move = False

            for move in ["W", "A", "S", "D"]:
                test_board, points = move_board(board, move)

                if test_board != board:
                    possible_move = True
                    break

            if not possible_move:
                display_board(board)
                print("Game Over!")
                print("Final score:", score)
                break


play_game()