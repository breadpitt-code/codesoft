import math
import random

def board_printer(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_the_winner(board, player):
    #checking rows and colns
    for i in range(3):
        check_rows= True
        check_colns=True
        for j in range(3):
            if board[i][j] != player:
                check_rows = False
            if board[j][i] != player:
                check_colns = False
        if check_rows or check_colns:
            return True
    #check diagonals
    check_diag1 = True
    check_diag2 = True
    for i in range(3):
        if board[i][i] != player:
            check_diag1 = False
        if board[i][2 - i] != player:
            check_diag2 = False
    if check_diag1 or check_diag2:
        return True
    return False

def is_it_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def ai_minimax(board, depth, is_maximizing, alpha, beta):
    if check_the_winner(board, "X"):
        return -1
    if check_the_winner(board, "O"):
        return 1
    if is_it_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = ai_minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = ai_minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def ai_best_move(board):
    best_score = -math.inf
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = ai_minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    moves = [(i, j)]
                elif score == best_score:
                    moves.append((i, j))
    return random.choice(moves)

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        board_printer(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        
        if player == "X":
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if board[row][col] != " ":
                    print("Cell already occupied. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers between 0 and 2.")
                continue
        else:
            print("AI (O) is thinking...")
            row, col = ai_best_move(board)
        
        board[row][col] = player
        
        if check_the_winner(board, player):
            board_printer(board)
            print(f"Player {player} wins!")
            break
        
        if is_it_full(board):
            board_printer(board)
            print("It's a draw!")
            break
        
        turn += 1

tic_tac_toe()