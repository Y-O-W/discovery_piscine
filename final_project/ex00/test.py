theBoard = {            
            '1': ' ' , '2': ' ' , '3': ' ', '4': ' ' , '5': ' ' , '6': ' ' ,'7': ' ' , '8': ' ' , '9': ' ' ,
            }

board_keys = []

for key in theBoard:
    board_keys.append(key)
    # print(board_keys)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def check_victory(b):
    victory_combinations = [
        ['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], 
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
        ['7', '5', '3'], ['1', '5', '9']
    ]
    for combination in victory_combinations:
        if all(b[position] == 'X' for position in combination):
            return True
        if all(b[position] == 'O' for position in combination):
            return True
    return False

def game():
    player_1 = input("Player 1, What is your name? ")
    player_2 = input("Player 2, What is your name? ")

    score = {player_1: 0, player_2: 0, 'Ties': 0}
    count =0

    for i in range(1, 10):
        # print(i)
        printBoard(theBoard)
        print(f"Turn for {player_1 if i % 2 != 0 else player_2}. Choose a space (1-9) or type 'STOP'")
        move = input()
        # print(f"Player {player_1 if i % 2 != 0 else player_2} chose: {move}")
        if theBoard[move] == ' ':
            theBoard[move] = 'X' if i % 2 != 0 else 'O'
        else:
            print("That place is already filled. Move to another space!")
            i -= 1
            continue
        if check_victory(theBoard):
            printBoard(theBoard)
            winner = player_1 if i % 2 != 0 else player_2
            print(f"Game Over. {winner} won!")
            score[winner] += 1
            print(f"Scores: {player_1}: {score[player_1]}, {player_2}: {score[player_2]}, Ties: {score['Ties']}")
            break
game()