# This script defines a chessboard and its pieces, along with their movements and rules.

import enum
from dataclasses import dataclass
import tkinter as tk
from PIL import Image, ImageTk

# Enum for the color of the chess pieces
class Color(enum.Enum):
    NONE = 0  # No color (empty square)
    WHITE = 1  # White pieces
    BLACK = 2  # Black pieces

# Enum for the type of chess pieces
class PieceType(enum.Enum):
    EMPTY = 0  # Empty square
    PAWN = 1  # Pawn
    ROOK = 2  # Rook
    NIGHT = 3  # Knight
    BISHOP = 4  # Bishop
    QUEEN = 5  # Queen
    KING = 6  # King

# Class representing a chess piece
@dataclass
class Piece:
    """
    Represents a chess piece on the board.
    Attributes:
        piece_type (PieceType): The type of the piece (e.g., PAWN, ROOK)
        color (Color): The color of the piece (e.g., WHITE, BLACK)
        row (int): The row position on the board
        col (int): The column position on the board
    """
    piece_type: PieceType  # Type of the piece (e.g., PAWN, ROOK)
    color: Color  # Color of the piece (e.g., WHITE, BLACK)
    row: int = -1  # Row position on the board
    col: int = -1  # Column position on the board

# Class representing the chessboard
class Chessboard:
    """_summary_
    This class represents a chessboard and its pieces, along with their movements and rules.
    It provides methods to initialize the board, check for valid moves, and evaluate the board state.
    Attributes:
        board (list): A 2D list representing the chessboard, where each element is a Piece object.
    Methods:
        initialize_board(): Initializes the chessboard with the standard chess setup.
        get_piece(row, col): Returns the piece at the specified row and column.
        __str__(): Returns a string representation of the chessboard for printing.
        is_valid(start_row, start_col, end_row, end_col): Checks if a move is valid.
        get_possible_moves(start_row, start_col): Returns a list of possible moves for a piece.
        evaluate_board(): Evaluates the board and calculates the total score based on piece values.
    Args:
        None
    Returns:
        None
    Raises:
        None
    Example:
        chessboard = Chessboard()
        print(chessboard)  # Print the initial board configuration
        moves = chessboard.get_possible_moves(6, 0)  # Get possible moves for the white rook at (6, 0)
        print(moves)
        chessboard.evaluate_board()  # Evaluate the board score
    Example:
    """
    def __init__(self):
        # Initialize an 8x8 board with empty pieces
        self.board = [[Piece(PieceType.EMPTY, Color.NONE) for _ in range(8)] for _ in range(8)]
        # Dictionary to track the count of each piece type for both colors
        self.initialize_board()  # Set up the initial board configuration

    # Method to initialize the board with the standard chess setup
    def initialize_board(self):
        # Reset the board to empty
        self.board = [[Piece(PieceType.EMPTY, None) for _ in range(8)] for _ in range(8)]
       
        # Place white pieces
        for color in {Color.WHITE, Color.BLACK}:
            fl = 7 if color == Color.WHITE else 0 
            pl = 6 if color == Color.WHITE else 1
            self.board[fl][0] = Piece(PieceType.ROOK, color)
            self.board[fl][1] = Piece(PieceType.NIGHT, color)
            self.board[fl][2] = Piece(PieceType.BISHOP, color)
            self.board[fl][3] = Piece(PieceType.QUEEN, color)
            self.board[fl][4] = Piece(PieceType.KING, color)
            self.board[fl][5] = Piece(PieceType.BISHOP, color)
            self.board[fl][6] = Piece(PieceType.NIGHT, color)
            self.board[fl][7] = Piece(PieceType.ROOK, color)
            for i in range(8):
                self.board[pl][i] = Piece(PieceType.PAWN, color)

    # Method to get the piece at a specific position on the board
    def get_piece(self, row, col):
        return self.board[row][col]

    # Method to represent the board as a string for printing
    def __str__(self):
        board_str = ""
        for row in self.board:
            for piece in row:
                # Use the first letter of the piece type and color, or '.' for empty squares
                board_str += f"{piece.piece_type.name[0] if piece.piece_type != PieceType.EMPTY else '.'}{piece.color.name[0] if piece.piece_type != PieceType.EMPTY else '.'} "
            board_str += "\n"
        return board_str

    # Method to check if a move is valid
    def is_valid(self, start_row, start_col, end_row, end_col):
        """
        Check if a move is valid.

        Args:
            start_row (int): The starting row index.
            start_col (int): The starting column index.
            end_row (int): The ending row index.
            end_col (int): The ending column index.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        # Check if the start and end positions are within the board boundaries
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        piece = self.get_piece(start_row, start_col)  # Get the piece at the starting position
        end_piece = self.get_piece(end_row, end_col)  # Get the piece at the ending position

        # Check if there is a piece at the starting position
        if piece.piece_type == PieceType.EMPTY:
            return False

        # Check if the start and end positions are the same
        if start_row == end_row and start_col == end_col:
            return False

        # Validate moves for each piece type
        # Pawn
        if piece.piece_type == PieceType.PAWN:
            # White pawn movement
            if piece.color == Color.WHITE:
                if (start_col == end_col and start_row - end_row == 1 and end_piece.piece_type == PieceType.EMPTY) or \
                   (start_col == end_col and start_row == 6 and end_row == 4 and end_piece.piece_type == PieceType.EMPTY and \
                    self.get_piece(5, start_col).piece_type == PieceType.EMPTY) or \
                   (abs(start_col - end_col) == 1 and start_row - end_row == 1 and end_piece.color == Color.BLACK):
                    return True
            # Black pawn movement
            elif piece.color == Color.BLACK:
                if (start_col == end_col and end_row - start_row == 1 and end_piece.piece_type == PieceType.EMPTY) or \
                   (start_col == end_col and start_row == 1 and end_row == 3 and end_piece.piece_type == PieceType.EMPTY \
                    and self.get_piece(2, start_col).piece_type == PieceType.EMPTY) or \
                   (abs(start_col - end_col) == 1 and end_row - start_row == 1 and end_piece.color == Color.WHITE):
                    return True
            return False

        # Knight
        if piece.piece_type == PieceType.NIGHT:
            if (abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1) or \
               (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2):
                if end_piece.color != piece.color:
                    return True
            return False

        # Bishop
        if piece.piece_type == PieceType.BISHOP:
            if abs(start_row - end_row) == abs(start_col - end_col):  # Diagonal movement
                step_row = 1 if end_row > start_row else -1
                step_col = 1 if end_col > start_col else -1
                # Check if the path is clear
                for i in range(1, abs(start_row - end_row)):
                    if self.get_piece(start_row + i * step_row, start_col + i * step_col).piece_type != PieceType.EMPTY:
                        return False
                if end_piece.color != piece.color:
                    return True
            return False

        # Rook
        if piece.piece_type == PieceType.ROOK:
            if start_row == end_row or start_col == end_col:  # Horizontal or vertical movement
                if start_row == end_row:  # Horizontal movement
                    step = 1 if end_col > start_col else -1
                    for col in range(start_col + step, end_col, step):
                        if self.get_piece(start_row, col).piece_type != PieceType.EMPTY:
                            return False
                else:  # Vertical movement
                    step = 1 if end_row > start_row else -1
                    for row in range(start_row + step, end_row, step):
                        if self.get_piece(row, start_col).piece_type != PieceType.EMPTY:
                            return False
                if end_piece.color != piece.color:
                    return True
            return False

        # Queen
        if piece.piece_type == PieceType.QUEEN:
            if start_row == end_row or start_col == end_col or abs(start_row - end_row) == abs(start_col - end_col):
                if start_row == end_row:  # Horizontal movement
                    step = 1 if end_col > start_col else -1
                    for col in range(start_col + step, end_col, step):
                        if self.get_piece(start_row, col).piece_type != PieceType.EMPTY:
                            return False
                elif start_col == end_col:  # Vertical movement
                    step = 1 if end_row > start_row else -1
                    for row in range(start_row + step, end_row, step):
                        if self.get_piece(row, start_col).piece_type != PieceType.EMPTY:
                            return False
                else:  # Diagonal movement
                    step_row = 1 if end_row > start_row else -1
                    step_col = 1 if end_col > start_col else -1
                    for i in range(1, abs(start_row - end_row)):
                        if self.get_piece(start_row + i * step_row, start_col + i * step_col).piece_type != PieceType.EMPTY:
                            return False
                if end_piece.color != piece.color:
                    return True
            return False

        # King
        if piece.piece_type == PieceType.KING:
            if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:  # One square in any direction
                if end_piece.color != piece.color:
                    return True
            return False

        return False  # If no valid move is found, return False

    
    def get_possible_moves(self, start_row, start_col):
        """
        Get all possible moves for a piece at a given position.

        Args:
            start_row (int): The starting row index.
            start_col (int): The starting column index.

        Returns:
            list: A list of tuples representing valid moves 
               (piece_type.name, start_row, start_col, end_row, end_col)
        """
        possible_moves = []
        piece = self.get_piece(start_row, start_col)

        # If the square is empty, return an empty list
        if piece.piece_type == PieceType.EMPTY:
            return possible_moves


        # Define possible directions based on piece type
        directions = []
        
        if piece.piece_type == PieceType.PAWN:
            directions = [(-2,0),(-1, 0), (-1, -1), (-1, 1)] if piece.color == Color.WHITE else [(2,0),(1, 0), (1, -1), (1, 1)]
        elif piece.piece_type == PieceType.NIGHT:
            directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        elif piece.piece_type == PieceType.BISHOP:
            directions = [(i, i) for i in range(-7, 8)] + [(i, -i) for i in range(-7, 8)]
        elif piece.piece_type == PieceType.ROOK:
            directions = [(i, 0) for i in range(-7, 8)] + [(0, i) for i in range(-7, 8)]
        elif piece.piece_type == PieceType.QUEEN:
            directions = [(i, i) for i in range(-7, 8)] + [(i, -i) for i in range(-7, 8)] + \
                 [(i, 0) for i in range(-7, 8)] + [(0, i) for i in range(-7, 8)]
        elif piece.piece_type == PieceType.KING:
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # Iterate over possible directions
        for direction in directions:
            end_row, end_col = start_row + direction[0], start_col + direction[1]
            while 0 <= end_row < 8 and 0 <= end_col < 8:
                if self.is_valid(start_row, start_col, end_row, end_col):
                    possible_moves.append((piece.piece_type.name, start_row, start_col, end_row, end_col))
                # Stop further movement for non-sliding pieces
                if piece.piece_type in {PieceType.PAWN, PieceType.NIGHT, PieceType.KING}:
                    break
                # Stop if the path is blocked
                if self.get_piece(end_row, end_col).piece_type != PieceType.EMPTY:
                    break
                # Continue sliding for sliding pieces
                end_row += direction[0]
                end_col += direction[1]

        return possible_moves
    
    def evaluate_board(self):
        """
        Evaluate the board and calculate the total score based on piece values.

        Returns:
            int: The total score of the board.
        """

        piece_values = {piece_type: score 
                        for piece_type, score in zip(PieceType, [0, 1, 5, 3, 3, 9, 100])}   
        # Sum up piece values over both dimensions of the board
        total_score = sum(
            piece_values[piece.piece_type] if piece.color == Color.WHITE else -piece_values[piece.piece_type]
            for row in self.board for piece in row 
        )
        return total_score

    def display_board_tk(self):
        """
        Display the chess board using Tkinter.
        Creates a window with a graphical representation of the current board state.
        """
        # Create the main window
        root = tk.Tk()
        root.title("Chess Board")
        
        # Create a frame for the board
        board_frame = tk.Frame(root)
        board_frame.pack(padx=10, pady=10)
        
        # Define colors for the squares
        colors = ["darkgrey", "gray"]
        
        # Dictionary to map pieces to unicode chess symbols
        piece_symbols = {
            (PieceType.KING, Color.WHITE): "♔",
            (PieceType.QUEEN, Color.WHITE): "♕",
            (PieceType.ROOK, Color.WHITE): "♖",
            (PieceType.BISHOP, Color.WHITE): "♗",
            (PieceType.NIGHT, Color.WHITE): "♘",
            (PieceType.PAWN, Color.WHITE): "♙",
            (PieceType.KING, Color.BLACK): "♚",
            (PieceType.QUEEN, Color.BLACK): "♛",
            (PieceType.ROOK, Color.BLACK): "♜",
            (PieceType.BISHOP, Color.BLACK): "♝",
            (PieceType.NIGHT, Color.BLACK): "♞",
            (PieceType.PAWN, Color.BLACK): "♟"
        }
        
        # Update the font to use Pecita
        font_style = ("Pecita", 70)  # Change font to Pecita with size 40
        
        # Create the squares and place pieces
        for row in range(8):
            for col in range(8):
                # Calculate square color
                color = colors[(row + col) % 2]
                
                # Create square
                square = tk.Frame(
                    board_frame,
                    width=60,
                    height=60,
                    bg=color
                )
                square.grid(row=row, column=col)
                square.pack_propagate(False)
                
                # Get piece at current position
                piece = self.get_piece(row, col)
                
                # If square is not empty, place piece symbol
                if piece.piece_type != PieceType.EMPTY:
                    piece_symbol = piece_symbols.get((piece.piece_type, piece.color), "")
                    label = tk.Label(
                        square,
                        text=piece_symbol,
                        font=font_style,  # Use the updated font style
                        bg=color,
                        fg="black" if piece.color == Color.BLACK else "white"
                    )
                    label.pack(expand=True)
        
        # Add column labels (a-h)
        for col in range(8):
            tk.Label(
                board_frame,
                text=chr(97 + col)
            ).grid(row=8, column=col)
        
        # Add row labels (1-8)
        for row in range(8):
            tk.Label(
                board_frame,
                text=str(8 - row)
            ).grid(row=row, column=8)
        
        root.mainloop()
  
if __name__ == "__main__":
    board = Chessboard()
    board.display_board_tk()


