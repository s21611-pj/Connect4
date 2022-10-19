"""
Authors: Paweł Badysiak (s21166), Wojciech Turek (s21611)
Connect4 Rules video -> https://www.youtube.com/watch?v=ejHQw0g2iKM&ab_channel=Hasbro
Connect4 Rules text PL -> https://pl.wikipedia.org/wiki/Czw%C3%B3rki
Connect4 Rules text ENG -> https://en.wikipedia.org/wiki/Connect_Four
How to run:
Install:
1. Numpy -> in terminal 'pip install numpy'
2. esayAI -> in terminal 'pip install easyAI'
After instalation:
-> in console open folder with connect4.py and run command "python connect4.py" to play the game
"""

from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax
import numpy as np
from scipy.signal import convolve2d


class Connect4(TwoPlayerGame):

    @staticmethod
    def get_detection_kernels():
        """
            Create kernels for horizontal, vertical and diagonal win detection.
            Create a 2D array from game board
            Returns:
                detection_kernels (list): List of 4 possible kernels to detect
        """
        horizontal_kernel = np.array([[1, 1, 1, 1]])
        vertical_kernel = np.transpose(horizontal_kernel)
        diagonal1_kernel = np.eye(4, dtype=np.uint8)
        diagonal2_kernel = np.fliplr(diagonal1_kernel)
        detection_kernels = [horizontal_kernel, vertical_kernel, diagonal1_kernel, diagonal2_kernel]
        return detection_kernels

    def __init__(self, players):
        """Game Initialization with fixed board size filled with zeroes
            Current Player fixed to 1 (Human), if you want AI to start, just change this value to "2"

        Parameters:
            players (list): List containing 2 players
        """
        self.players = players
        self.current_player = 1
        self.width = 7
        self.height = 6
        self.board = np.array([[0 for x in range(self.width)] for y in range(self.height)])

    def possible_moves(self):
        """ Returns:
                list: List of possible moves.
        """
        return [i for i in range(self.width) if (self.board[:, i].min() == 0)]

    def make_move(self, move):
        """ Places a piece on the bottom of the board.
            Parameters:
                move (int): Position on the board.
        """
        line = np.argmin(self.board[:, move] != 0)
        self.board[line, move] = self.current_player

    def lose(self):
        """
            Run the board through the convolution operations
            using Scipy's highly optimized convolve2d function.
            In the array formed by the convolution output, any "4"
            indicates that there were 4 connected tiles in the board.
            Returns:
                 bool: True if found 4 connected tiles, default False
        """
        for kernel in self.get_detection_kernels():
            if (convolve2d(self.board == self.opponent_index, kernel, mode="valid") == 4).any():
                return True
        return False

    def is_over(self):
        """ Returns:
                bool: True if the game is over.
        """
        return self.lose()

    def show(self):
        """ Prints whole board after each move """
        reverse_board = self.board[::-1]
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in reverse_board]))

    def scoring(self):
        """
            Decreases one point from the loser
            Returns:
                -1 point if current_player loses game, default 0
        """
        return -1 if self.lose() else 0


if __name__ == "__main__":
    """
        Game runner
        Setting up Negamax to 7 moves ahead intelligent
        Game contains two players - Human and Artificial Intelligence
    """
    ai = Negamax(7)
    game = Connect4([Human_Player(), AI_Player(ai)])
    history = game.play()
    if game.lose():
        if game.opponent_index == 1:
            print("Human has won")
        elif game.opponent_index == 2:
            print("AI has won")
        else:
            print("Draw")
