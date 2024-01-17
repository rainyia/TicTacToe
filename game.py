import tkinter as tk

# Logic to check if the current player has won
def check_winner():
    global game_over

    # check rows for winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            game_over = True
            return True

    # check column for winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            game_over = True
            return True

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        game_over = True
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        game_over = True
        return True

    return False

def on_click(row, col):
    global current_player, game_over
    if board[row][col] == " " and not game_over:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner():
            label.config(text=f"Player {current_player} wins!")
            game_over = True
            return
        elif is_board_full():
            label.config(text="It's a tie!")
            return
        toggle_player()

def is_board_full():
    # logic to check if board is full
    pass
def toggle_player():
    global current_player
    current_player = "0" if current_player == "X" else "X"
    label.config(text=f"It's {current_player}'s turn")

# initialize game window
root = tk.Tk()
root.title("LoLo's Tic Tac Toe: The Game")

# initialize game variables
current_player = "X"
game_over = False
board = [[" " for i in range(3)] for _ in range(3)]

# Creates a 3x3 grid of buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=('normal', 30),
                                  width=5, height=2, command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Status Label
label = tk.Label(root, text="Player X's turn", font=('normal', 15))
label.grid(row=3, column=0, columnspan=3)

# restart game
def restart_game():
    global current_player, game_over, board
    current_player = "X" # resets players to "X"
    game_over = False # reset game over flag
    board = [[" " for i in range(3)] for _ in range(3)] # reset board

    # reset and re-enable buttons on board
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state=tk.NORMAL)

    # Update Status
    label.config(text="Player X's turn")


restart_button = tk.Button(root, text="Restart Game", font=('normal', 15), command=restart_game)
restart_button.grid(row=4, column=0, columnspan=3)

# closes main loop
root.mainloop()

