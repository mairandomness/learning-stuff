
def display_board(board, n):
    for j in range (0, n):
        if j == 0:
            print(" |", end="")
            for x in range(0, n):
                print(str(x) + "|", end="")
            print("")
        print(str(j) + "|", end="")
        for i in range(0, n):
            print(board[i + j*n] + "|", end="")
        print("")

def is_valid_play(play, board, n):
    #takes str play and verifies if its a valid one
    #I'm sorry this function turned out so ugly
    try:
        iplay = int(play)
    except Exception:
        return False
    curr_move_row = int(iplay/10)
    curr_move_col = iplay%10
    if curr_move_row<0 or curr_move_row > n-1 or curr_move_col > n-1:
        return False
    curr_move_idx = curr_move_col + curr_move_row*n
    if board[curr_move_idx] == " ":
        return True
    else:
        return False

def update_board(play, board, n, player):
    iplay = int(play)
    curr_move_row = int(iplay/10)
    curr_move_col = iplay%10
    curr_move_idx = curr_move_col + curr_move_row*n
    new_board = board[:]
    new_board[curr_move_idx] = player
    return new_board

def is_game_over(play, play_count, board, n):
    if play_count < 2*n -1:
        return [False,"Bleh"]
    if did_player_win(play, board, n):
        return [True, "Win"]

    if play_count == n**2:
        return [True, "Tie"]
    else:
        return [False, "Bleh"]

def did_player_win(play, board, n):
    iplay = int(play)
    curr_move_row = int(iplay/10)
    curr_move_col = iplay%10
    curr_move_idx = curr_move_col + curr_move_row*n

    #check row
    won = True
    for pos in range(curr_move_row*n, curr_move_row*n + n):
        if board[curr_move_idx] != board[pos]:
            won = False
            break
    if won == True:
        return True
    won = True

    #check column
    for row in range(0,n):
        if board[curr_move_idx] != board[row*n + curr_move_col]:
            won = False
            break

    if won == True:
        return True
    won = True

    #check main diagonal, if the last play is in it
    if curr_move_col == curr_move_row:
        for row in range(0,n):
            if board[curr_move_idx] != board[row*n + row]:
                won = False
                break

        if won == True:
            return True
    won = True
    #check secondary diagonal, if the last play is in it
    if curr_move_col + curr_move_row == n - 1:
        for row in range(0,n):
            if board[curr_move_idx] != board[row*n + (n-1 - row)]:
                won = False
                break
        if won == True:

            return True
    else:
        return False
