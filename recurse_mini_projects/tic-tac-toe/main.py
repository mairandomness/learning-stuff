"""Main file for the tic-tac-toe game"""

import tictac as t

def main():
    """ main function """
    #get a board size
    good_input = False
    while not good_input:
        size = input("Enter a number from 3 to 9 for the size of your tic-tac-toe board:")
        try:
            size = int(size)
            if 2 < size < 10:
                good_input = True
        except ValueError:
            pass

    #set the board, let's store it as a list
    board = [" "] * size ** 2
    t.display_board(board, size)
    play_count = 0

    #if the game is not won and board is not full, keep asking for plays
    while True:
        valid_play = False

        #try to get a valid input from player X
        while not valid_play:
            msg = "Player X, input the position of your play as a two digit number, row and column:"
            play_x = input(msg)
            valid_play = t.is_valid_play(play_x, board, size)

        board = t.update_board(play_x, board, size, "X")
        play_count += 1
        t.display_board(board, size)
        #check if game is over
        #if it is break from the loop
        result = t.is_game_over(play_x, play_count, board, size)
        if result[0] and (result[1] == "Win"):
            print("GAME OVER. PLAYER X WON!!!")
            break
        elif result[0] and (result[1] == "Tie"):
            print("GAME OVER. IT'S A DRAW.")
            break

        #if it's not over
        #try to get a valid input from player O
        valid_play = False
        while not valid_play:
            msg = "Player O, input the position of your play as a two digit number, row and column:"
            play_o = input(msg)
            valid_play = t.is_valid_play(play_o, board, size)

        board = t.update_board(play_o, board, size, "O")
        play_count += 1
        t.display_board(board, size)
        #check if game is over
        #if it is, break from the loop
        result = t.is_game_over(play_o, play_count, board, size)
        if result[0] and (result[1] == "Win"):
            print("GAME OVER. PLAYER O WON!!!")
            break
        elif result[0] and (result[1] == "Tie"):
            print("GAME OVER. IT'S A TIE.")
            break


if __name__ == "__main__":
    main()
