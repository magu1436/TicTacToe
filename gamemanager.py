

from tkinter import Frame

from tkinterboardgame import Tile
from object import Symbol
from board import TicTacToeBoard


class GameManager:

    def __init__(self, board: TicTacToeBoard):
        self.symbol = Symbol.CIRCLE
        self.board = board
    
    def draw_symbol(self, board, event):
        pass

    def create_tile(self):
        return Tile(left_clicked_func=self.draw_symbol)