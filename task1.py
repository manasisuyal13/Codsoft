import tkinter as tk
from tkinter import messagebox
import random

# Create a window and set up the game board
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("400x450")
window.configure(bg="lightblue")

board = [' ' for _ in range(9)]
current_player = 'X'  # 'X' is always the player
buttons = []

# Check if a player has won


def check_winner():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            highlight_winning_combination(a, b, c)
            return True
    return False

# Highlight the winning combination


def highlight_winning_combination(a, b, c):
    buttons[a].config(bg="lightgreen")
    buttons[b].config(bg="lightgreen")
    buttons[c].config(bg="lightgreen")

# Check if the board is full


def is_board_full():
    return ' ' not in board

# AI move: Simple decision-making


def ai_move():
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner():
                buttons[i].config(text='O', state="disabled",
                                  disabledforeground="red")
                return
            board[i] = ' '

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner():
                board[i] = 'O'
                buttons[i].config(text='O', state="disabled",
                                  disabledforeground="red")
                return
            board[i] = ' '

    available_moves = [i for i in range(9) if board[i] == ' ']
    if available_moves:
        move = random.choice(available_moves)
        board[move] = 'O'
        buttons[move].config(text='O', state="disabled",
                             disabledforeground="red")

# Handle button click events


def on_click(index):
    global current_player
    if board[index] == ' ':
        board[index] = current_player
        buttons[index].config(text=current_player,
                              state="disabled", disabledforeground="blue")
        if check_winner():
            messagebox.showinfo("Game Over", f"{current_player} wins!")
            reset_game()
        elif is_board_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = 'O'
            ai_move()
            if check_winner():
                messagebox.showinfo("Game Over", "AI (O) wins!")
                reset_game()
            elif is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                reset_game()
            else:
                current_player = 'X'

# Reset the game


def reset_game():
    global board, current_player
    board = [' ' for _ in range(9)]
    current_player = 'X'
    for button in buttons:
        button.config(text='', state="normal", bg="white")


# Create the game grid with colors and styles
for i in range(9):
    button = tk.Button(window, text='', width=10, height=3, font=('Arial', 20),
                       bg="white", activebackground="lightgrey", command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i % 3, padx=5, pady=5)
    buttons.append(button)

# Create a title label
label = tk.Label(window, text="Tic-Tac-Toe", font=("Arial",
                 24, "bold"), bg="lightblue", fg="darkblue")
label.grid(row=3, column=0, columnspan=3, pady=10)

# Run the Tkinter window
window.mainloop()
