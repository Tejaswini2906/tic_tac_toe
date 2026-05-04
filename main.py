import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Tic Tac Toe")

# Variables
current_player = "X"
board = [""] * 9

# Check winner
def check_winner():
    win_patterns = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win_patterns:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    return None

# Button click
def click(i):
    global current_player

    if board[i] == "":
        board[i] = current_player

        if current_player == "X":
            buttons[i].config(text="X", fg="red")
        else:
            buttons[i].config(text="O", fg="blue")

        winner = check_winner()

        if winner:
            messagebox.showinfo("Winner", f"Player {winner} wins!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Draw", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.config(text=f"Player {current_player} Turn")

# Reset game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="", fg="black")
    status_label.config(text="Player X Turn")

# Buttons
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20),
                    width=5, height=2,
                    bg="lightyellow",
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Status label
status_label = tk.Label(root, text="Player X Turn", font=("Arial", 14))
status_label.grid(row=3, column=0, columnspan=3)

# Restart button
reset_btn = tk.Button(root, text="Restart", command=reset_game, bg="lightgreen")
reset_btn.grid(row=4, column=0, columnspan=3, sticky="we")

# Run
root.mainloop()