# pylint: disable=too-many-public-methods
"""
Test the Chessboard class.
"""
import unittest
from chessboard import Chessboard, PieceType, Color, Piece

class TestChessboard(unittest.TestCase):
    """Test the Chessboard class.
    """
    def setUp(self):
        """Set up a fresh chessboard for each test."""
        self.board = Chessboard()
    
    def test_initial_board_setup(self):
        """Test that the board is initialized correctly."""
        # Test white pieces
        self.assertEqual(self.board.get_piece(7, 0).piece_type, PieceType.ROOK)
        self.assertEqual(self.board.get_piece(7, 1).piece_type, PieceType.NIGHT)
        self.assertEqual(self.board.get_piece(7, 2).piece_type, PieceType.BISHOP)
        self.assertEqual(self.board.get_piece(7, 3).piece_type, PieceType.QUEEN)
        self.assertEqual(self.board.get_piece(7, 4).piece_type, PieceType.KING)
        
        # Test black pieces
        self.assertEqual(self.board.get_piece(0, 0).piece_type, PieceType.ROOK)
        self.assertEqual(self.board.get_piece(0, 4).piece_type, PieceType.KING)
        
        # Test pawns
        for i in range(8):
            self.assertEqual(self.board.get_piece(6, i).piece_type, PieceType.PAWN)
            self.assertEqual(self.board.get_piece(6, i).color, Color.WHITE)
            self.assertEqual(self.board.get_piece(1, i).piece_type, PieceType.PAWN)
            self.assertEqual(self.board.get_piece(1, i).color, Color.BLACK)
        
        # Test empty squares
        for i in range(8):
            for j in range(8):
                if i not in [0, 1, 6, 7]:
                    self.assertEqual(self.board.get_piece(i, j).piece_type, PieceType.EMPTY)
    
    def test_piece_values(self):
        """Test that piece values are correctly assigned."""
        self.assertEqual(self.board.piece_values[PieceType.EMPTY], 0)
        self.assertEqual(self.board.piece_values[PieceType.PAWN], 1)
        self.assertEqual(self.board.piece_values[PieceType.ROOK], 5)
        self.assertEqual(self.board.piece_values[PieceType.NIGHT], 3)
        self.assertEqual(self.board.piece_values[PieceType.BISHOP], 3)
        self.assertEqual(self.board.piece_values[PieceType.QUEEN], 9)
        self.assertEqual(self.board.piece_values[PieceType.KING], 100)
    
    def test_move_piece(self):
        """Test that pieces can be moved correctly."""
        # Move white pawn from e2 to e4
        self.assertTrue(self.board.move_piece(6, 4, 4, 4))
        self.assertEqual(self.board.get_piece(4, 4).piece_type, PieceType.PAWN)
        self.assertEqual(self.board.get_piece(4, 4).color, Color.WHITE)
        self.assertEqual(self.board.get_piece(6, 4).piece_type, PieceType.EMPTY)
        
        # Move black pawn from e7 to e5
        self.assertTrue(self.board.move_piece(1, 4, 3, 4))
        self.assertEqual(self.board.get_piece(3, 4).piece_type, PieceType.PAWN)
        self.assertEqual(self.board.get_piece(3, 4).color, Color.BLACK)
    
    def test_invalid_moves(self):
        """Test that invalid moves are rejected."""
        # Try to move white king directly
        self.assertFalse(self.board.move_piece(7, 4, 5, 4))
        
        # Try to move white pawn diagonally without capture
        self.assertFalse(self.board.move_piece(6, 4, 5, 5))
        
        # Try to move pawn 3 squares
        self.assertFalse(self.board.move_piece(6, 4, 3, 4))
    
    def test_pawn_capture(self):
        """Test that pawns can capture correctly."""
        # Set up a situation for capture
        self.board.move_piece(6, 4, 4, 4)  # White pawn to e4
        self.board.move_piece(1, 3, 3, 3)  # Black pawn to d5
        
        # Capture
        self.assertTrue(self.board.move_piece(4, 4, 3, 3))  # e4 captures d5
        self.assertEqual(self.board.get_piece(3, 3).piece_type, PieceType.PAWN)
        self.assertEqual(self.board.get_piece(3, 3).color, Color.WHITE)
    
    def test_knight_movement(self):
        """Test knight movement."""
        # Move knight from g1 to f3
        self.assertTrue(self.board.move_piece(7, 6, 5, 5))
        self.assertEqual(self.board.get_piece(5, 5).piece_type, PieceType.NIGHT)
        
        # Try invalid knight move
        self.assertFalse(self.board.move_piece(5, 5, 3, 3))
    
    def test_bishop_movement(self):
        """Test bishop movement."""
        # Move pawn to make space for bishop
        self.board.move_piece(6, 3, 4, 3)
        
        # Move bishop
        self.assertTrue(self.board.move_piece(7, 2, 5, 4))
        self.assertEqual(self.board.get_piece(5, 4).piece_type, PieceType.BISHOP)
        
        # Try invalid bishop move (non-diagonal)
        self.assertFalse(self.board.move_piece(5, 4, 5, 5))
    
    def test_queen_movement(self):
        """Test queen movement."""
        # Move pawn to make space for queen
        self.board.move_piece(6, 4, 4, 4)
        print("Hallo----\n",self.board)
        
        # Move queen diagonally
        self.assertTrue(self.board.move_piece(7, 3, 5, 5))
        self.assertEqual(self.board.get_piece(5, 5).piece_type, PieceType.QUEEN)
        
        # Move queen horizontally
        self.assertTrue(self.board.move_piece(5, 5, 5, 2))
        self.assertEqual(self.board.get_piece(5, 2).piece_type, PieceType.QUEEN)
    
    def test_rook_movement(self):
        """Test rook movement."""
        # Move pawn to make space for rook
        self.board.move_piece(6, 0, 4, 0)
        
        # Move rook vertically
        self.assertTrue(self.board.move_piece(7, 0, 5, 0))
        self.assertEqual(self.board.get_piece(5, 0).piece_type, PieceType.ROOK)
        
        # Move rook horizontally
        self.assertTrue(self.board.move_piece(5, 0, 5, 3))
        self.assertEqual(self.board.get_piece(5, 3).piece_type, PieceType.ROOK)
    
    def test_is_valid_blocked_path(self):
        """Test that pieces can't move through other pieces."""
        # Try to move rook through pawn
        self.assertFalse(self.board.is_valid(7, 0, 3, 0))
        
        # Try to move bishop through pawn
        self.assertFalse(self.board.is_valid(7, 2, 5, 0))
    
    def test_board_evaluation(self):
        """Test board evaluation function."""
        # Initial board should be balanced
        self.assertEqual(self.board.evaluate_board(), 0)
        
        # Capture a black pawn with white pawn
        self.board.move_piece(6, 0, 4, 0)  # White pawn to a4
        self.board.move_piece(1, 1, 3, 1)  # Black pawn to b5
        self.board.move_piece(4, 0, 3, 1)  # White pawn captures black pawn
        
        # White should be up by 1 point (1 pawn)
        self.assertEqual(self.board.evaluate_board(), 1)

    def test_get_possible_moves(self):
        """Test getting possible moves for various pieces."""
        # Get initial pawn moves for white
        moves = self.board.get_possible_moves(6, 0)  # a2 pawn
        self.assertEqual(len(moves), 2)  # Can move one or two squares forward
        
        # Get knight moves
        moves = self.board.get_possible_moves(7, 1)  # b1 knight
        self.assertEqual(len(moves), 2)  # Two possible knight moves
        
        # No moves for blocked bishop
        moves = self.board.get_possible_moves(7, 2)  # c1 bishop
        self.assertEqual(len(moves), 0)  # Can't move (blocked)

    def test_king_movement(self):
        """Test king movement."""
        # Move pawn to make space for king
        self.board.move_piece(6, 4, 4, 4)
        
        # Move king one square
        self.assertTrue(self.board.move_piece(7, 4, 6, 4))
        self.assertEqual(self.board.get_piece(6, 4).piece_type, PieceType.KING)
        
        # Move king diagonally
        self.assertTrue(self.board.move_piece(6, 4, 5, 5))
        self.assertEqual(self.board.get_piece(5, 5).piece_type, PieceType.KING)
        
        # Try invalid king move (more than one square)
        self.assertFalse(self.board.move_piece(5, 5, 3, 5))

    def test_pawn_double_move(self):
        """Test pawn's ability to move two squares from starting position."""
        # Double move from starting position
        self.assertTrue(self.board.move_piece(6, 0, 4, 0))
        self.assertEqual(self.board.get_piece(4, 0).piece_type, PieceType.PAWN)
        
        # Try double move from non-starting position (should fail)
        self.assertFalse(self.board.move_piece(4, 0, 2, 0))

    def test_pawn_promotion(self):
        """Test pawn promotion."""
        # Setup: Move a white pawn to the seventh rank
        board = Chessboard()
        # Replace a black piece with a white pawn
        board.board[1][0] = Piece(PieceType.PAWN, Color.WHITE, 1, 0)
        
        # Move to promotion square
        self.assertTrue(board.move_piece(1, 0, 0, 0))
        
        # Check if pawn was promoted to queen
        self.assertEqual(board.get_piece(0, 0).piece_type, PieceType.QUEEN)
        self.assertEqual(board.get_piece(0, 0).color, Color.WHITE)

    def test_capture_own_piece(self):
        """Test that a piece can't capture a piece of the same color."""
        # Try to move white knight to a square occupied by white pawn
        self.assertFalse(self.board.is_valid(7, 1, 6, 3))

    def test_empty_square_selection(self):
        """Test selecting an empty square."""
        # Try to get moves for an empty square
        moves = self.board.get_possible_moves(4, 4)
        self.assertEqual(len(moves), 0)

    def test_out_of_bounds_moves(self):
        """Test that moves outside the board are invalid."""
        # Setup a piece at the edge
        self.board.move_piece(6, 0, 0, 0)  # White pawn to a8
        
        # Try to move outside board boundaries
        self.assertFalse(self.board.is_valid(0, 0, -1, 0))
        self.assertFalse(self.board.is_valid(0, 0, 0, -1))
    
    def test_direction_generation(self):
        """Test that movement directions are generated correctly for pieces."""
        # Knight directions
        moves = self.board.get_possible_moves(7, 1)  # b1 knight
        self.assertEqual(len(moves), 2)  # Only specific moves are legal
        
        # Setup a queen in the center
        empty_board = Chessboard()
        empty_board.board = [[Piece(PieceType.EMPTY, Color.NONE, r, c) for c in range(8)] for r in range(8)]
        empty_board.board[3][3] = Piece(PieceType.QUEEN, Color.WHITE, 3, 3)
        
        # Queen should have moves in 8 directions
        moves = empty_board.get_possible_moves(3, 3)
        # Queen should be able to access majority of the board from center
        self.assertTrue(len(moves) > 20) 

    def test_fen_string_generation(self):
        """Test generating FEN string from board position."""
        # Starting position FEN
        expected_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        self.assertEqual(self.board.to_fen().split(" ")[0], expected_fen)
        
        # Move a piece and check FEN
        self.board.move_piece(6, 4, 4, 4)  # e2 to e4
        expected_fen_after_move = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR"
        self.assertEqual(self.board.to_fen().split(" ")[0], expected_fen_after_move)

    def test_load_from_fen(self):
        """Test loading board from FEN string."""
        # Custom position FEN
        fen = "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R"
        board = Chessboard.from_fen(fen)
        
        # Verify pieces are in the correct positions
        self.assertEqual(board.get_piece(4, 4).piece_type, PieceType.PAWN)
        self.assertEqual(board.get_piece(4, 4).color, Color.WHITE)
        self.assertEqual(board.get_piece(2, 2).piece_type, PieceType.PAWN)
        self.assertEqual(board.get_piece(2, 2).color, Color.BLACK)
        self.assertEqual(board.get_piece(5, 5).piece_type, PieceType.NIGHT)
        self.assertEqual(board.get_piece(5, 5).color, Color.WHITE)

    def test_copy_board(self):
        """Test board copying."""
        # Create a copy of the board
        board_copy = self.board.copy()
        
        # Modify original board
        self.board.move_piece(6, 0, 4, 0)
        
        # Copy shouldn't be affected
        self.assertEqual(board_copy.get_piece(6, 0).piece_type, PieceType.PAWN)
        self.assertEqual(board_copy.get_piece(4, 0).piece_type, PieceType.EMPTY)

if __name__ == '__main__':
    unittest.main()