
from typing import Sequence

from tkinter import Frame, Label, Misc, Canvas, PhotoImage
from tkinter.ttk import Button

from tkinterboardgame import BoardGamePhotoImage
from constants import CIRCLE_IMAGE_PATH, CROSS_IMAGE_PATH
from object import Symbol, PageTransitionButton


TITLE_TEXT: str = "三目並べゲーム"
NEW_GAME_BUTTON_TEXT: str = "あたらしいゲーム！"
TO_HOME_BUTTON: str = "ホーム画面へ"
WINNER_DISPLAY_HEIGHT = 80


class HomeDisplay(Frame):
    
    def __init__(self, master: Misc):

        super().__init__(master)
        
        self.title: Label = Label(self, text=TITLE_TEXT)
        self.start_button: Button = Button(self, text=NEW_GAME_BUTTON_TEXT)


class GameDisplay(Frame):

    def __init__(self, master: Misc):
        master.update_idletasks()
        width = master.winfo_width()
        height = master.winfo_height()
        super().__init__(master, width=width, height=height)


class GameSubDisplay(Frame):

    IMAGE_TAG: str = "symbol"

    def __init__(self, master: Misc, size: Sequence[int]):
        super().__init__(master, width=size[0], height=size[1])

        self.current_symbol: Canvas = Canvas(self, width=size[0], height=size[1])
        self.current_symbol.pack(side="top")

        self.winner_label: Label = Label(self)
        self.home_button: Button = Button(self, text=TO_HOME_BUTTON)
    
    def update_symbol(self, symbol: Symbol):
        self.current_symbol.delete(self.IMAGE_TAG)
        match symbol:
            case Symbol.CIRCLE: image = PhotoImage(file=CIRCLE_IMAGE_PATH)
            case Symbol.CROSS: image = PhotoImage(file=CROSS_IMAGE_PATH)
        self.current_symbol.create_image(image=image, tags=self.IMAGE_TAG)
    
    def display_ending(self, won_symbol: Symbol, home_display: HomeDisplay):
        winner_display = WinnerDisplay(
            self, 
            (self.winfo_width(), WINNER_DISPLAY_HEIGHT),
            won_symbol,
        )
        winner_display.pack(side="top")

        button = PageTransitionButton(
            self,
            TO_HOME_BUTTON,
            home_display
        )
        button.pack(side="top")


class WinnerDisplay(Frame):

    def __init__(self, master: Misc, size: Sequence[int], symbol: Symbol):
        super().__init__(master)

        match symbol:
            case Symbol.CIRCLE: image = BoardGamePhotoImage(CIRCLE_IMAGE_PATH)
            case Symbol.CROSS: image = BoardGamePhotoImage(CROSS_IMAGE_PATH)
        canvas_size = (size[1], size[1])
        image.resize(canvas_size)

        self.symbol_canvas: Canvas = Canvas(self, width=canvas_size[0], height=canvas_size[1])
        self.symbol_canvas.create_image(0, 0, image=image, anchor="NW")

        self.label = Label(self, text="の勝ち！")

        self.symbol_canvas.pack(side="left")
        self.label.pack(side="left")