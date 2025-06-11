

from typing import Callable
from enum import Enum
from tkinter import Misc, Frame
from tkinter.ttk import Button

from tkinterboardgame import Piece, Tile
from constants import CIRCLE_IMAGE_PATH, CROSS_IMAGE_PATH


class Symbol(Enum):
    """記号を表す列挙型クラス"""
    CIRCLE = 0
    CROSS = 1


class SymbolPiece(Piece):
    """ボード上に置く記号オブジェクトのクラス"""

    def __init__(self, symbol: Symbol, image_path: str):
        """コンストラクタ
        
        Args:
            symbol(Symbol): 記号
            image_path(str): 画像のパス"""
        super().__init__(image_path)
        self.symbol: Symbol = symbol


class Circle(SymbolPiece):
    """丸を表すオブジェクトのクラス"""

    def __init__(self):
        super().__init__(Symbol.CIRCLE, CIRCLE_IMAGE_PATH)


class Cross(SymbolPiece):
    """バツを表すオブジェクトのクラス"""

    def __init__(self):
        super().__init__(Symbol.CROSS, CROSS_IMAGE_PATH)


class SymbolFactory:

    @staticmethod
    def create_symbol(symbol: Symbol):
        """記号オブジェクトを作成するメソッド
        
        Args:
            symbol(Symbol): 作成する記号
        
        Raises:
            ValueError: 引数に記号以外の値が与えられたときに生じる"""
        match symbol:
            case Symbol.CIRCLE: return Circle()
            case Symbol.CROSS: return Cross()
        raise ValueError("not given Symbol value.")


class PageTransitionButton(Button):

    def __init__(self, master: Misc, text: str, display: Frame):
        super().__init__(master, text=text, command=self.trans_page)

    def trans_page(self):
        pass