
from typing import Sequence, Callable
from enum import StrEnum

from tkinter import Frame, Label, Misc, Canvas, Event
from tkinter.ttk import Button

from tkinterboardgame import BoardGamePhotoImage, Coordinate
from constants import CIRCLE_IMAGE_PATH, CROSS_IMAGE_PATH, BACKGROUND_PATH, TITLE_LOGO_PATH
from object import Symbol
from board import TicTacToeBoard
from text_object import AutoFontLabel


TITLE_TEXT: str = "三目並べゲーム"
NEW_GAME_BUTTON_TEXT: str = "あたらしいゲーム！"
HOME_BUTTON_TEXT: str = "ホーム画面へ"
WINNER_DISPLAY_HEIGHT = 150

TITLE_LOGO_RATIO = .8
CONTENT_PADDING = 30


class View(StrEnum):
    HOME = "home"
    GAME = "game"


class ViewTransitionButton(Button):

    def __init__(self, master: Misc, text: str, view_to: View, another_command: Callable[[], None] | None = None):
        super().__init__(master, text=text, command=self.on_click)
        self.view_to = view_to
        self.another_command = another_command
    
    def on_click(self):
        for child in self.master.winfo_toplevel().winfo_children():
            if child.winfo_name() == self.view_to:
                child.tkraise()
        if self.another_command is not None:
            self.another_command()


class HomeDisplay(Frame):
    
    def __init__(self, master: Misc):

        self.display_size: tuple[int, int] = (
            master.winfo_width(), master.winfo_height()
        )

        super().__init__(
            master, 
            name=View.HOME,
            width=self.display_size[0],
            height=self.display_size[1]
        )
        
        self.home_canvas: Canvas = Canvas(
            self,
            width=self.display_size[0],
            height=self.display_size[1]
        )
        self.home_canvas.pack(fill="both", expand=True)

        self.__bg_image_ref: BoardGamePhotoImage = BoardGamePhotoImage(
            BACKGROUND_PATH,
            self.display_size,
        )
        self.home_canvas.create_image(
            0,
            0,
            image=self.__bg_image_ref,
            anchor="nw"
        )
        
        title_logo_width = self.display_size[0] * TITLE_LOGO_RATIO
        self.__title_image_ref: BoardGamePhotoImage = BoardGamePhotoImage(
            TITLE_LOGO_PATH
        )
        img_origin_size = Coordinate(self.__title_image_ref.width(), self.__title_image_ref.height())
        logo_ratio_to_window = title_logo_width // img_origin_size.x
        self.__title_image_ref.resize(img_origin_size * logo_ratio_to_window)
        self.home_canvas.create_image(
            self.display_size[0] // 2,
            CONTENT_PADDING + self.__title_image_ref.height(),
            image=self.__title_image_ref,
            anchor="s"
        )

        self.start_button: ViewTransitionButton = ViewTransitionButton(
            self, NEW_GAME_BUTTON_TEXT, View.GAME
        )
        self.start_button.place(
            x=self.display_size[0] // 2,
            y=2 * CONTENT_PADDING + self.__title_image_ref.height(),
            anchor="c"
        )


class GameDisplay(Frame):

    def __init__(self, master: Misc):
        self.display_size: tuple[int, int] = (
            master.winfo_width(), master.winfo_height()
        )
        super().__init__(
            master, 
            name=View.GAME,
            width=self.display_size[0],
            height=self.display_size[1]
            )
        
        self.display_size = self.display_size
        self.board: TicTacToeBoard = TicTacToeBoard(
            self,
            (self.display_size[1], self.display_size[1])
        )
        self.board.pack(side="left")

        self.sub_display: GameSubDisplay = GameSubDisplay(
            self,
            (self.display_size[0] - self.board.board_display_size[0], self.display_size[1])
        )
        self.sub_display.pack(side="left", fill="both", expand=True)


class GameSubDisplay(Frame):

    IMAGE_TAG: str = "symbol"

    def __init__(self, master: GameDisplay, size: tuple[int, int]):
        super().__init__(master, width=size[0], height=size[1])
        self.pack_propagate(False)
        self.display_size: tuple[int, int] = size
        self.winner_display = None

        self.home_button: ViewTransitionButton = ViewTransitionButton(
            self, 
            HOME_BUTTON_TEXT, 
            View.HOME,
            lambda: (master.board.take_all_pieces(), self.reset_display())
            )
        self.home_button.pack(side="top", fill="both", expand=True)

        self.canvas_size: tuple[int. int] = (size[0], size[0])
        self.current_symbol: Canvas = Canvas(self, width=self.canvas_size[0], height=self.canvas_size[1])
        self.reset_display()
    
    def update_symbol(self, symbol: Symbol):
        self.current_symbol.delete(self.IMAGE_TAG)
        self.__draw_symbol(symbol)
    
    def __draw_symbol(self, symbol: Symbol):
        match symbol:
            case Symbol.CIRCLE: self.__symbol_image_ref = BoardGamePhotoImage(CIRCLE_IMAGE_PATH)
            case Symbol.CROSS: self.__symbol_image_ref = BoardGamePhotoImage(CROSS_IMAGE_PATH)
        self.__symbol_image_ref.resize(self.canvas_size)
        self.current_symbol.create_image(
            0,
            0,
            image=self.__symbol_image_ref,
            tags=self.IMAGE_TAG,
            anchor="nw"
        )

    def display_ending(self, won_symbol: Symbol):
        self.current_symbol.pack_forget()
        self.winner_display = WinnerDisplay(
            self, 
            (self.winfo_width(), WINNER_DISPLAY_HEIGHT),
            won_symbol,
        )
        self.winner_display.pack(side="top", fill="both", expand=True)
    
    def reset_display(self):
        if self.winner_display is not None:
            self.winner_display.destroy()
            self.winner_display = None
        self.current_symbol.pack(side="top")
        self.update_symbol(Symbol.CIRCLE)


class WinnerDisplay(Frame):

    def __init__(self, master: Misc, size: Sequence[int], symbol: Symbol):
        super().__init__(
            master,
            width=size[0],
            height=size[1],
        )
        self.pack_propagate(False)

        match symbol:
            case Symbol.CIRCLE: self.__symbol_image_ref = BoardGamePhotoImage(CIRCLE_IMAGE_PATH)
            case Symbol.CROSS: self.__symbol_image_ref = BoardGamePhotoImage(CROSS_IMAGE_PATH)
        canvas_size = (size[1], size[1])
        self.__symbol_image_ref.resize(canvas_size)

        self.symbol_canvas: Canvas = Canvas(self, width=canvas_size[0], height=canvas_size[1])
        self.symbol_canvas.create_image(0, 0, image=self.__symbol_image_ref, anchor="nw")

        self.label = AutoFontLabel(
            self,
            "の勝ち！",
            size[0] - canvas_size[0]
        )

        self.symbol_canvas.pack(side="left")
        self.label.pack(side="left")