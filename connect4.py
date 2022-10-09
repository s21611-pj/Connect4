from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax
import numpy as np


# Authors: Wojciech Turek, Paweł Badysiak

class Connect4(TwoPlayerGame):

    def __init__(self, players):
        """Game Initialization"""
        self.players = players
        self.width = 7
        self.height = 6
        self.pile = 20
        self.current_player = 1
        self.board = [['x' for i in range(self.width)] for j in range(self.height)]
        self.counter = 0  # human even, ai odd

    def possible_moves(self):
        return ['0', '1', '2', '3', '4', '5', '6']

    def make_move(self, move):
        player_move = int(move)
        for i in range(self.height - 1, -1, -1):
            if 'x' in self.board[i][player_move]:
                self.board[i][int(move)] = '@'
                return self.board

    def win(self):
        return self.pile <= 0

    def is_over(self):
        return self.win()

    def show(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))

    def scoring(self):
        return 100 if self.win() else 0


ai = Negamax(13)
game = Connect4([Human_Player(), AI_Player(ai)])
history = game.play()
