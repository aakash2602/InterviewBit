

def print_board(board):
    print('  |  |  ')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('  |  |  ')
    print('-----------')
    print('  |  |  ')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('  |  |  ')
    print('-----------')
    print('  |  |  ')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('  |  |  ')

def check_logic(board, marker):
    if board[7] == board[8] == board[9] == marker:
        return True
    elif board[4] == board[5] == board[6] == marker:
        return True
    elif board[1] == board[2] == board[3] == marker:
        return True
    elif board[7] == board[4] == board[1] == marker:
        return True
    elif board[8] == board[5] == board[2] == marker:
        return True
    elif board[9] == board[6] == board[3] == marker:
        return True
    elif board[1] == board[5] == board[9] == marker:
        return True
    elif board[7] == board[5] == board[3] == marker:
        return True
    else:
        return False

def main_logic():

    start = input("Do you wanna play tic tac toe: Yes or No:")
    if start.lower() != 'yes':
        print("Cool! have a nice day ahead")
        return

    while True:

        while True:
            player_1_symbol = input("Player 1, Choose X or O:")
            if player_1_symbol in ['X', 'O']:
                break
        player_2_symbol = 'O' if player_1_symbol == 'X' else 'X'
        mode = 1 # 1 means player 1 and 2 means player 2
        marker = player_1_symbol
        board = [' ']*10
        board[0] = '#'
        print_board(board)
        while True:
            number = int(input('Player '+str(mode) + " choose position to place your symbol: "))
            if number not in range(1, 10):
                print ("Please Select a valid position")
                continue
            elif board[number] != '':
                print ("Position already occupied")
                continue
            board[number] = marker
            print_board(board)
            if not check_logic(board, marker):
                if '' not in board:
                    print ('Well Played!!  Its a tie!!!')
                    break
                marker = player_2_symbol if mode == 1 else player_1_symbol
                mode = 2 if mode == 1 else 1
            else:
                print ("Congratulations!! Player "+ str(mode) + " You have won this time!")
                break

        start = input("Do you wanna play tic tac toe again?: Yes or No %s")
        if start.lower() != 'yes':
            print("Cool! have a nice day ahead")
            break


main_logic()