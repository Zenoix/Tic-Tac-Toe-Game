# initialise variables
winner = None
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
game_in_progress = True
coords_approved = False
current_player = "X"


def print_board():
    print("-" * 9)
    print("|", board[0][2], board[1][2], board[2][2], "|")
    print("|", board[0][1], board[1][1], board[2][1], "|")
    print("|", board[0][0], board[1][0], board[2][0], "|")
    print("-" * 9)


def check_coords(coords_input):
    global coords_approved
    int_coords = []
    for coord in coords_input:
        if not coord.isdigit():
            print("You should enter numbers!")
            break
        elif not 0 < int(coord) < 4:
            print("Coordinates should be from 1 to 3!")
            break
        else:
            int_coords.append(int(coord))

    if len(int_coords) == 2:
        x, y = int_coords[0] - 1, int_coords[1] - 1

        if board[x][y] == " ":
            coords_approved = True
            board[x][y] = current_player
            print_board()
        else:
            print("This cell is occupied! Choose another one!")
            x, y = None, None


def check_for_game_win():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_in_progress
    row_1 = board[0][2] == board[1][2] == board[2][2] != " "
    row_2 = board[0][1] == board[1][1] == board[2][1] != " "
    row_3 = board[0][0] == board[1][0] == board[2][0] != " "

    if row_1 or row_2 or row_3:
        game_in_progress = False

    if row_1:
        return board[0][2]
    elif row_2:
        return board[0][1]
    elif row_3:
        return board[0][0]
    else:
        return None


def check_columns():
    global game_in_progress
    column_1 = board[0][0] == board[0][1] == board[0][2] != " "
    column_2 = board[1][0] == board[1][1] == board[1][2] != " "
    column_3 = board[2][0] == board[2][1] == board[2][2] != " "

    if column_1 or column_2 or column_3:
        game_in_progress = False

    if column_1:
        return board[0][0]
    elif column_2:
        return board[1][0]
    elif column_3:
        return board[2][0]
    else:
        return None


def check_diagonals():
    global game_in_progress
    diagonal_1 = board[0][2] == board[1][1] == board[2][0] != " "
    diagonal_2 = board[2][2] == board[1][1] == board[0][0] != " "

    if diagonal_1 or diagonal_2:
        game_in_progress = False

    if diagonal_1:
        return board[0][2]
    elif diagonal_2:
        return board[2][2]
    else:
        return None


def check_tie():
    global game_in_progress
    if " " not in board[0] and " " not in board[1] and " " not in board[2] and winner == None:
        game_in_progress = False
        return True
    else:
        return False


def player_turn():
    global coords_approved
    print("Enter the coordinates: ")
    str_coords = [coord for coord in input().split()]
    check_coords(str_coords)
    coords_approved = False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def play_game():
    while game_in_progress:
        player_turn()
        check_for_game_win()
        check_tie()
        flip_player()

    if winner == "X" or winner == "O":
        print(f"{winner} wins")
    elif winner == None:
        print("Draw")


play_game()
