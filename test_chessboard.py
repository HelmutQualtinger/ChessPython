import unittest
from chessboard import Chessboard, PieceType, Color, Piece

class TestChessboard(unittest.TestCase):
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
        self.board.move_piece(6, 3, 4, 3)
        
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

if __name__ == '__main__':
    unittest.main()