import tictac as t

#get a board size
good_input = False
while not good_input:
    n = input("Enter a number from 3 to 9 for the size of your tic-tac-toe board:")
    try:
        n = int(n)
        if 2<n<10:
            good_input = True
    except Exception:
        pass

#set the board, let's store it as a list
board = [" "] * n ** 2
t.display_board(board, n)

play_count = 0
#if the game is not won and board is not full, keep asking for plays
while True:
    valid_play = False
    #try to get a valid input from player X
    while not valid_play:
        play_x = int(input("Player X, input the position you want to play as a two digit number, row and column:"))
        valid_play = t.is_valid_play(play_x, board, n)
    board = t.update_board(play_x, board, n, "X")
    play_count +=1
    t.display_board(board,n)
    #check if game is over
    #if it is break from the loop
    result = t.is_game_over(play_x, play_count, board,n)
    if result[0] and (result[1] == "Win"):
        print("GAME OVER. PLAYER X WON!!!")
        break
    elif result[0] and (result[1] == "Tie"):
        print("GAME OVER. IT'S A TIE.")
        break

    #if it's not over
    #try to get a valid input from player O
    valid_play = False
    while not valid_play:
        play_o = int(input("Player O, input the position you want to play as a two digit number, row and column:"))
        valid_play = t.is_valid_play(play_o, board, n)
    board = t.update_board(play_o, board, n, "O")
    play_count +=1
    t.display_board(board,n)
    #check if game is over
    #if it is, break from the loop
    result = t.is_game_over(play_o, play_count, board,n)
    if result[0] and (result[1] == "Win"):
        print("GAME OVER. PLAYER O WON!!!")
        break
    elif result[0] and (result[1] == "Tie"):
        print("GAME OVER. IT'S A TIE.")
        break
