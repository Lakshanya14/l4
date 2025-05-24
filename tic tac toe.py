board = ["" for _ in range (9)]
def show_board():
    print()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("--+---+--")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("--+---+--")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
        else:
            return False

def check_draw():
    return " " not in board

def play_game():
    current_player = "X"
    while True:
        show_board()
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player
            else:
                print("Tha spot is taken ! Try again.")
                continue
        except [ValueError , IndexError] :
            print("Invalid input! Please enter a number between 1 and 9.")
            continue
        if check_win(current_player):
            show_board()
            print(f"🎉Player {current_player} wins!")
            break   
        elif check_draw():
            show_board()
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"


play_game()
