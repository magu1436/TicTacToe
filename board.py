

from tkinter import Misc

from tkinterboardgame import Board
from constants import BACKGROUND_PATH, GRID_PATH, GRID_WIDTH


class TicTacToeBoard(Board):

    def __init__(self, master: Misc, display_size: tuple[int, int]):
        super().__init__(
            master, 
            (3, 3),
            BACKGROUND_PATH,
            display_size,
            GRID_PATH,
            grid_display_width=GRID_WIDTH
        )