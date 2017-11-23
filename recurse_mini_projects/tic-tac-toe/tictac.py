"""functions to be used to make a tic-tac-toe game"""

def display_board(board, size):
    """get a lst board that represents a square board and an int size
    (dimension of the board) and print it to the terminal"""
    for row in range(0, size):
        if row == 0:
            print(" |", end="")
            for col_num in range(0, size):
                print(str(col_num) + "|", end="")

            print("")

        print(str(row) + "|", end="")
        for col in range(0, size):
            print(board[col + row*size] + "|", end="")

        print("")

def is_valid_play(play, board, size):
    """takes str play and verifies if its a valid one
    lst board and int size, return True if the play is valid and False otherwise"""
    try:
        iplay = int(play)
    except ValueError:
        return False
    curr_move_row = int(iplay/10)
    curr_move_col = iplay%10
    #row could be negative, but col is modulus, so it's positive for sure
    #check if the play is inside the board
    if curr_move_row < 0 or curr_move_row > size-1 or curr_move_col > size-1:
        return False
    curr_move_idx = curr_move_col + curr_move_row*size
    #check if that place is available
    return board[curr_move_idx] == " "

def update_board(play, board, size, player):
    """takes str play, lst board, int size and str player
    and updates the board so it has the play in it, returns lst new_board"""
    iplay = int(play)
    curr_move_row = int(iplay/10)
    curr_move_col = iplay%10
    curr_move_idx = curr_move_col + curr_move_row*size
    new_board = board[:]
    new_board[curr_move_idx] = player
    return new_board

def is_game_over(play, play_count, board, size):
    """takes str play, int play_count, lst board and int size
    and decides if play caused the game to be over, returns
    -[True, "Tie"] if the board completely full and no one won
    -[True, "Win"] if someone won
    -[False, "Bleh"] if the game is not over yet
    """
    #if there are not enough plays for the game to be over
    #we don't have to check if it is over
    if play_count < 2*size -1:
        return [False, "Bleh"]
    if did_player_win(play, board, size):
        return [True, "Win"]
    if play_count == size ** 2:
        return [True, "Tie"]
    return [False, "Bleh"]

def did_player_win(play, board, size):
    """ takes str play, lst board and int size
    and verifies if that play fulfills a winning condition
    returns True if the player won, False otherwise"""
    iplay = int(play)
    curr_move_row = int(iplay/10)
    curr_move_col = iplay%10
    curr_move_idx = curr_move_col + curr_move_row*size

    #check row
    won = True
    for pos in range(curr_move_row*size, curr_move_row*size + size):
        if board[curr_move_idx] != board[pos]:
            won = False
            break

    if won:
        return True
    won = True

    #check column
    for row in range(0, size):
        if board[curr_move_idx] != board[row*size + curr_move_col]:
            won = False
            break

    if won:
        return True
    won = True

    #check main diagonal, if the last play is in it
    if curr_move_col == curr_move_row:
        for row in range(0, size):
            if board[curr_move_idx] != board[row*size + row]:
                won = False
                break

        if won:
            return True
    won = True
    #check secondary diagonal, if the last play is in it
    if curr_move_col + curr_move_row == size - 1:
        for row in range(0, size):
            if board[curr_move_idx] != board[row * size + (size - 1 - row)]:
                won = False
                break

        return won
