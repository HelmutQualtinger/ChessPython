# ChessPython

ChessPython is a simple chess game implemented in Python. It defines a chessboard, its pieces, and the rules governing their movements. The game can be played in a graphical interface using Tkinter.

## Features

- **Chessboard Representation**: A visual representation of the chessboard with pieces.
- **Piece Movement**: Implements movement rules for all chess pieces (Pawns, Rooks, Knights, Bishops, Queens, Kings).
- **Valid Move Checking**: Checks if a move is valid according to chess rules.
- **Board Evaluation**: Evaluates the board state and calculates a score based on piece values.
- **Graphical User Interface**: Displays the chessboard using Tkinter.

## Installation

To run this project, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This project requires the following Python packages:

- `Pillow` for image handling (if you plan to extend the project with images).
- `tkinter` for the graphical user interface (comes pre-installed with Python).

You can install the required packages using pip:

```bash
pip install Pillow
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ChessPython.git
   cd ChessPython
   ```

2. Run the chess game:

   ```bash
   python chessboard.py
   ```

3. A window will open displaying the chessboard. You can interact with the pieces according to the rules of chess.

## Code Structure

- `chessboard.py`: The main script that defines the chessboard, pieces, and their movements.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for their contributions and support.