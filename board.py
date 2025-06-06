

from tkinter import Misc

from tkinterboardgame import Board
from constants import BACKGROUND_PATH, GRID_PATH, GRID_WIDTH


class TicTacToeBoard(Board):

    def __init__(self, master: Misc):
        master.update_idletasks()
        width = master.winfo_width()
        height = master.winfo_height()
        super().__init__(
            master, 
            (3, 3),
            BACKGROUND_PATH,
            (width, height),
            GRID_PATH,
            grid_display_width=GRID_WIDTH
        )