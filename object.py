

from typing import Callable
from enum import Enum
from tkinter import Misc, Frame
from tkinter.ttk import Button

from tkinterboardgame import Piece, Tile
from constants import CIRCLE_IMAGE_PATH, CROSS_IMAGE_PATH


class Symbol(Enum):
    CIRCLE = 0
    CROSS = 1


class SymbolPiece(Piece):

    def __init__(self, symbol: Symbol, image_path: str):
        super().__init__(image_path)
        self.symbol: Symbol = symbol


class Circle(SymbolPiece):

    def __init__(self):
        super().__init__(Symbol.CIRCLE, CIRCLE_IMAGE_PATH)


class Cross(SymbolPiece):

    def __init__(self):
        super().__init__(Symbol.CROSS, CROSS_IMAGE_PATH)


class PageTransitionButton(Button):

    def __init__(self, master: Misc, text: str, display: Frame):
        super().__init__(master, text=text, command=self.trans_page)

    def trans_page(self):
        pass