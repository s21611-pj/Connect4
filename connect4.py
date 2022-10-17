from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax
import numpy as np

# Authors: Wojciech Turek, Paweł Badysiak

class Connect4(TwoPlayerGame):

    def __init__(self, players):
        """Game Initialization with fixed board size"""
        self.players = players
        self.current_player = 1
        self.width = 7
        self.height = 6
        self.board = [['x' for i in range(self.width)] for j in range(self.height)]
        self.roundCounter = 0  # human even, ai odd
        self.HumanPlayerSymbol = 'PL'
        self.AIPlayerSymbol = 'AI'

    def possible_moves(self):
        return ['0', '1', '2', '3', '4', '5', '6']

    def make_move(self, move):
        """ TBD """
        player_move = int(move)
        for i in range(self.height - 1, -1, -1):
            if 'x' in self.board[i][player_move]:
                if self.roundCounter % 2 == 0:
                    self.board[i][int(move)] = self.HumanPlayerSymbol
                else:
                    self.board[i][int(move)] = self.AIPlayerSymbol
                self.roundCounter += 1
                return self.board

    def win(self):
        """ TBD """
        symbol = ''
        if (self.roundCounter -1) % 2 == 0:
            symbol = self.HumanPlayerSymbol
        else:
            symbol = self.AIPlayerSymbol

        # Check for win horizontaly
        for x in range(self.height):
            counter = 0
            for y in range(self.width):
                if self.board[x][y] == symbol:
                    counter += 1
                else:
                    counter = 0
                if counter >= 4:
                    return True

        # Check for win verticaly
        for y in range(self.width):
            counter = 0
            for x in range(self.height):
                if self.board[x][y] == symbol:
                    counter += 1
                else:
                    counter = 0
                if counter >= 4:
                    return True
        # Check for win diagonally

        return False

    def is_over(self):
        """ Game is over when someone wins """
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
