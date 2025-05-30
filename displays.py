
from typing import Sequence

from tkinter import Frame, Label, Misc, Canvas, PhotoImage
from tkinter.ttk import Button

from tkinterboardgame import BoardGamePhotoImage
from constants import CIRCLE_IMAGE_PATH, CROSS_IMAGE_PATH
from object import Symbol


TITLE_TEXT: str = "三目並べゲーム"
NEW_GAME_BUTTON_TEXT: str = "あたらしいゲーム！"
TO_HOME_BUTTON: str = "ホーム画面へ"


class HomeDisplay(Frame):
    
    def __init__(self, master: Misc):

        super().__init__(master)
        
        self.title: Label = Label(self, text=TITLE_TEXT)
        self.start_button: Button = Button(self, text=NEW_GAME_BUTTON_TEXT)

        self.title.pack(side="top")
        self.start_button.pack(side="top")


class GameDisplay(Frame):

    def __init__(self, master: Misc):
        master.update_idletasks()
        width = master.winfo_width()
        height = master.winfo_height()
        super().__init__(master, width=width, height=height)


class GameSubDisplay(Frame):

    IMAGE_TAG: str = "symbol"

    def __init__(self, master: Misc, size: Sequence[int]):
        self.size = size
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
    
    def display_ending(self, won_symbol: Symbol):
        pass


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