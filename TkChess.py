import tkinter as tk

def create_chess_board():
    root = tk.Tk()
    root.title("Chess Board")
    board = tk.Frame(root)
    board.pack()

    rows, cols = 8, 8
    square_size = 60

    for row in range(rows):
        for col in range(cols):
            color = "white" if (row + col) % 2 == 0 else "black"
            square = tk.Frame(
                board,
                width=square_size,
                height=square_size,
                bg=color
            )
            square.grid(row=row, column=col)

    root.mainloop()

if __name__ == "__main__":
    create_chess_board()