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
        """Game Initialization with fixed board size filled with zeroes"""
        self.players = players
        self.current_player = 1
        self.width = 7
        self.height = 6
        self.board = np.array([[0 for x in range(self.width)] for y in range(self.height)])
        self.roundCounter = 0

    def possible_moves(self):
        return [i for i in range(self.width) if (self.board[:, i].min() == 0)]

    def make_move(self, move):
        """ TBD """
        player_move = int(move)
        for i in range(self.height - 1, -1, -1):
            if self.board[i][player_move] == 0:
                self.board[i][int(move)] = self.current_player
                self.roundCounter += 1
                return self.board

    def rewrite_board(self, current_player_symbol):
        new_board = np.zeros((6, 7))
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == current_player_symbol:
                    new_board[i][j] = 1
        return new_board

    def winning_move(self):
        board_with_specific_symbol = self.rewrite_board(self.current_player)

        for kernel in get_detection_kernels():
            if (convolve2d(board_with_specific_symbol == 1, kernel, mode="valid") == 4).any():
                return True
        return False

    def win(self):
        return self.winning_move()

    def is_over(self):
        """ Game is over when someone wins the round """
        return self.win()

    def show(self):
        """ Prints whole board after each move """
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))

    def scoring(self):
        """ Assigns one point to winner """
        return 1 if self.win() else 0


ai = Negamax(1)
game = Connect4([Human_Player(), AI_Player(ai)])
history = game.play()
