

from enum import Enum

from tkinterboardgame import Piece, Tile


CIRCLE_IMAGE_PATH = "images/maru.png"
CROSS_IMAGE_PATH = "images/batsu.png"


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