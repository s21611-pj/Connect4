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

    def possible_moves(self):
        return ['0', '1', '2', '3', '4', '5', '6']

    def make_move(self, move):
        player_move = int(move)
        board_height = len(self.board[int(move)])

        for i in range(board_height - 1, -1, -1):
            if '' not in self.board[int(move)][i]:
                print("todo")

    def win(self):
        return self.pile <= 0

    def is_over(self):
        return self.win()

    def show(self):
        print("%d bones left in the self pile" % self.pile)

    def scoring(self):
        return 100 if self.win() else 0


ai = Negamax(13)
game = Connect4([Human_Player(), AI_Player(ai)])
history = game.play()
