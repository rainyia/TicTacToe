import tkinter as tk


class Board:
    def __init__(self, game):
        self.game = game
        self.root = self.game.root
        self.root.title("Tic Tac Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.initialize_buttons()

    def initialize_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=('normal', 15),
                                               width=5, height=2, command=lambda i=i, j=j: self.game.on_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)


class GameLogic:
    def check_winner(self, board):
        # rows
        for row in board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        # columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2] != " ":
                return board[0][col]
        # diagonals
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]
        # return True if winner found, else False
        return None

    def is_board_full(self, board):
        for row in board:
            if " " in row:
                return False
            return True


class Game:
    def __init__(self):
        self.root = tk.Tk()  # Initialize the main window
        self.game_logic = GameLogic()
        self.board = Board(self)
        self.current_player = "X"
        self.game_over = False
        self.game_board = [[" " for _ in range(3)] for _ in range(3)]
        self.label = tk.Label(self.root, text="Player X's turn", font=('normal', 15))
        self.label.grid(row=3, column=0, columnspan=3)
        self.restart_button = tk.Button(self.root, text="Restart Game", font=('normal', 10), command=self.restart_game)
        self.restart_button.grid(row=4, column=0, columnspan=3)


    def on_click(self, i, j):
        if self.game_board[i][j] == " " and not self.game_over:
            self.game_board[i][j] = self.current_player
            self.board.buttons[i][j].config(text=self.current_player)

            winner = self.game_logic.check_winner(self.game_board)
            if winner:
                self.label.config(text=f"Player {winner} wins!")
                self.game_over = True
                return
            elif self.game_logic.is_board_full(self.game_board):
                self.label.config(text="It's a tie!")
                self.game_over = True
                return

            self.toggle_player()

    def toggle_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"
        self.label.config(text=f"Player {self.current_player}'s turn")

    def restart_game(self):
        self.current_player = "X"
        self.game_over = False
        self.game_board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.board.buttons[i][j].config(text=" ", state=tk.NORMAL)
        self.label.config(text="Player X's turn")


game = Game()
game.root.mainloop()
