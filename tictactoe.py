'''
A simple tic tac toe game developed by Yan Waipann
'''
import random
import os


def print_board(sign_lst):
    '''
    Prints the tic tac toe board with the signs in the array
    '''
    print("\n")  # for input prompt to be separated one line from the board printed
    # clear console on linux 'cls' for windows systems
    (lambda: os.system('clear'))()
    for i in range(1, 10, 3):
        if i < 6:
            divider = '-' * 11  # prints 11 '-'
        else:
            divider = ''
        print(
            f'{sign_lst[-i-2]:>2} | {sign_lst[-i-1]:^1} | {sign_lst[-i]:2} \n{divider}')


def player_input():
    '''
    Asks the first player of the preferred mark and returns the marks array
    '''
    try:
        player_1 = input("Enter your mark 'O' or 'X': ")
        while not player_1 in ("O", "X"):
            player_1 = input("Enter your mark 'O' or 'X': ")
        if player_1 == "X":
            player_2 = "O"
        else:
            player_2 = "X"
        print(f'Player 1 is: {player_1} and Player 2 is: {player_2}')
        return [player_1, player_2]
    except KeyboardInterrupt:
        print("\n You exited the game! Bye!")


def place_marker(board, marker, position):
    '''
    Puts the sign into the selected position of the array and return the updated board
    '''
    board[position] = marker
    return board


def win_check(board, mark, player):
    '''
    Checks if the mark matches a certain win pattern and returns the result
    '''
    won = (board[1:4:] == [mark] *
           3) or (board[4:7:] == [mark] *
                  3) or (board[7::] == [mark] *
                         3) or (board[1::3] == [mark] *
                                3) or (board[2::3] == [mark] *
                                       3) or (board[3::3] == [mark] *
                                              3) or (board[1::4] == [mark] *
                                                     3) or (board[3:8:2] == [mark] *
                                                            3)
    if won:
        print(f"Player {player} WINS! CONGRATULATIONS!\n")
        return True
    return False


def choose_first():
    '''
    Determines which player plays first randomly and return the player
    '''
    first_player = random.randint(1, 2)
    print(f"Player {first_player} goes first!")
    return first_player


def space_check(board, position):
    '''
    Check if the selected position is available
    '''
    return board[position] == ''


def full_board_check(board):
    '''
Checks if the board is full.
    '''
    if len("".join(board)) == 10:
        print("DRAW!")
        return True
    return False


def player_choice(board):
    '''
    Asks the position the player wishes to put the mark.
    '''
    while True:
        try:
            position = int(input("Enter your position of choice 1~9: "))
            while ((position < 1 or position > 9)
                   or not space_check(board, position)):
                print("The position is not available!")
                position = int(input("Enter your position of choice 1~9: "))
            return position
        except ValueError:
            print("Invalid Input!")
            continue
        except KeyboardInterrupt:
            print("\nYou exited the game!")
            break


def replay():
    '''
    Asks if the players want to play again.
    '''
    try:
        answer = input(
            "Wanna play again? \nEnter 'Y' to play and enter any other key to exit: ")
        if answer in ("Y", "y"):
            return True
        return False
    except KeyboardInterrupt:
        print("\nYou Exited the Game! Bye!")


def game_start():
    '''
    Initializes the game.
    '''
    marks = player_input()  # get player signs (O or X)
    first_player = choose_first()  # gets which player makes the first move
    second_player = 2
    if first_player == 2:
        second_player = 1
    board = ["#", "", "", "", "", "", "", "",
             "", ""]  # initialize an empty board
    while not full_board_check(board):
        try:
            print(f"Player {first_player}'s turn")
            position = player_choice(board)  # asks for the position
            # checks if the position is available, sets position
            place_marker(board, marks[first_player - 1], position)
            print_board(board)
            if win_check(board, marks[first_player - 1],
                         first_player) or full_board_check(board):
                # if player 1 wins or the board is full stop the loop
                break

            print(f"Player {second_player}'s turn")
            position = player_choice(board)
            place_marker(board, marks[second_player - 1], position)
            print_board(board)
            if win_check(board, marks[second_player - 1], second_player):
                break
        except TypeError:
            print("Something went wrong!")
            break
        except KeyboardInterrupt:
            print("You exited the game!")
            break

    else:
        replay()


print('Welcome to Tic Tac Toe!')
print('The positons on the tic tack toe board are as follow.')
print('1~3 bottom row, 4~6 middle, 7~9 top.')
game_start()

while replay():
    game_start()
    print('Hope you had fun! See ya!')
