
from enum import Enum
from tkinter import Frame

from tkinterboardgame import Tile, BGEvent, Coordinate
from object import Symbol, SymbolFactory
from board import TicTacToeBoard
from displays import GameDisplay


class Direction(Enum):
    N = Coordinate(0, -1)
    S = Coordinate(0, 1)
    E = Coordinate(1, 0)
    W = Coordinate(-1, 0)
    NE = Coordinate(1, -1)
    SE = Coordinate(1, 1)
    SW = Coordinate(-1, 1)
    NW = Coordinate(-1, -1)


class GameManager:

    def __init__(self, game_display: GameDisplay):
        self.board: TicTacToeBoard = game_display.board
        self.game_display: GameDisplay = game_display
        self.game_display.sub_display.reset_display()

        self.turn_symbol: Symbol = Symbol.CIRCLE

        for x in range(self.board.board_size.x):
            for y in range(self.board.board_size.y):
                self.board.set_tile(self.create_tile(), (x, y))
    
    def draw_symbol(self, event: BGEvent):
        self.board.remove_tile(event.coordinate)
        self.board.put(
            SymbolFactory.create_symbol(self.turn_symbol), 
            event.coordinate
        )

        if self.__check_won_when_putting(self.turn_symbol, event.coordinate):
            self.end()
        
        self.change_turn()
    
    def __check_won_when_putting(self, symbol: Symbol, coordinate: Coordinate):
        for direction in Direction:
            cursor = coordinate
            same_symbol_count = 0
            for i in range(self.board.board_size.x):
                if not self.board.is_in_board(cursor):
                    break
                if self.board.get(cursor) is None:
                    break
                if self.board.get(cursor).symbol != symbol:
                    break
                same_symbol_count += 1
                cursor += direction.value
            if same_symbol_count == self.board.board_size.x:
                return True
        return False

    def create_tile(self):
        return Tile(left_clicked_func=self.draw_symbol)

    def change_turn(self):
        
        # 試合が終了していないか判定
        if len(self.board.get_all_pieces()) == (self.board.board_size.x * self.board.board_size.y):
            self.end()

        for symbol in Symbol:
            if self.turn_symbol != symbol:
                self.turn_symbol = symbol
                break
        
        self.game_display.sub_display.update_symbol(self.turn_symbol)

    def end(self):
        self.board.reset_tiles()
        self.game_display.sub_display.display_ending(self.turn_symbol)