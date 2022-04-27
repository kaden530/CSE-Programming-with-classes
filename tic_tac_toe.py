#Week 2 Prove solo assignment 
#Kaden Brown
space_1 = "1" 
space_2 = "2"
space_3 = "3"
space_4 = "4"
space_5 = "5"
space_6 = "6"
space_7 = "7"
space_8 = "8"
space_9 = "9"
board = [ "",
space_1, 
space_2,
space_3,
space_4,
space_5,
space_6,
space_7,
space_8, 
space_9]
def main(board):
    game = 1
    gameboard = gameboard_f(board, game)
    I = 1
    while game == 1:
        gameboard =  player_x(board)
        gameboard_f(board, game)
        I += 1
        game = win(gameboard)
        if I == 10:
            game =4
        else:
            gameboard = player_o(board, game)
            I += 1
            game = win(board)
            gameboard_f(board, game)
    if game == 2:
        print("O's win!")
    elif game ==3:
        print("X's win!")
    else:
        print("Draw, no one wins sorry.")

def gameboard_f(board, game):
    while game ==1:
        gameboard =  (f"{board[1]} | {board[2]} | {board[3]} \n{board[4]} | {board[5]} | {board[6]}\n{board[7]} | {board[8]} | {board[9]}")
        print (gameboard)
        return gameboard

def player_x(board):
    space = int(input ("What space would you like to place your X?\n: "))
    player = ("x") 
    while space not in range(1,10):
        print("please enter a valid number")
        space = int(input("What space would you like to place your x?\n: "))
    space = str(space)
    while space not in board: 
        print ("Sorry that space is already chosen")
        space = input ("What space would you like to place your X?\n: ")
    player_x = placement (space, player, board)
    return player_x
    
def player_o(board, game):
    while game ==1:
        space = int(input ("What space would you like to place your O?\n: "))
        player = ("o")
        while space not in range(1,10):
            print("please enter a valid number")
            space = int(input("What space would you like to place your O?\n: "))
        space = str(space)
        while space not in board:
            print ("Sorry that space is already chosen")
            space = input ("What space would you like to place your O?\n: ") 
        player_o = placement (space, player, board)
        return player_o

def placement(space, player, board):
    for i in board:
        if i == space:
            i = int(i)
            board[i] = player
    return board

def win(board):
    win = 1
    row_1 = (f"{board[1]}, {board[2]}, {board[3]}")
    row_2 = (f"{board[4]}, { board[5]}, { board[6]}")
    row_3 = (f"{board[7]}, { board[8]}, { board[9]}")
    column_1 = (f"{board[1]}, { board[4]}, { board[7]}")
    column_2 = (f"{board[2]}, { board[5]}, { board[8]}")
    column_3 = (f"{board[3]}, { board[6]}, { board[9]}")
    diagonal_1 = (f"{board[1]}, { board[5]}, { board[9]}")
    diagonal_2 = (f"{board[3]}, { board[5]}, { board[7]}")
    gameover = [row_1, row_2,row_3,column_1,column_2,column_3,diagonal_1,diagonal_2]
    for i in gameover:
        if i in ("o, o, o"):
            win = 2
        elif i in ("x, x, x"):
            win = 3
    return win
main(board)