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


# Authors: Wojciech Turek, Paweł Badysiak

def get_detection_kernels():
    horizontal_kernel = np.array([[1, 1, 1, 1]])
    vertical_kernel = np.transpose(horizontal_kernel)
    diag1_kernel = np.eye(4, dtype=np.uint8)
    diag2_kernel = np.fliplr(diag1_kernel)
    detection_kernels = [horizontal_kernel, vertical_kernel, diag1_kernel, diag2_kernel]
    return detection_kernels

class Connect4(TwoPlayerGame):

    def __init__(self, players):
        """Game Initialization with fixed board size filled with zeroes

        Parameters:
            players (list): List containing 2 players
        """
        self.players = players
        self.current_player = 1
        self.width = 7
        self.height = 6
        self.board = np.array([[0 for x in range(self.width)] for y in range(self.height)])
        self.roundCounter = 0

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

    def win(self):
        for kernel in get_detection_kernels():
            if (convolve2d(self.board == self.current_player, kernel, mode="valid") == 4).any():
                return True
        return False

    def is_over(self):
        """ Returns:
            bool: True if the game is over.
        """
        return self.win()

    def show(self):
        """ Prints whole board after each move """
        reverse_board = self.board[::-1]
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in reverse_board]))

    def scoring(self):
        """ Assigns one point to winner """
        return 1 if self.win() else 0


ai = Negamax(5)
game = Connect4([Human_Player(), AI_Player(ai)])
history = game.play()
