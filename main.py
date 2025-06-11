

import tkinter as tk

from displays import GameDisplay, HomeDisplay
from gamemanager import GameManager


def main():
    root = tk.Tk()
    root.state("zoomed")
    root.update_idletasks()

    game = GameDisplay(root)
    game.place(x=0, y=0)
    
    manager = GameManager(game)

    home = HomeDisplay(root)
    home.place(x=0, y=0)
    home.tkraise()

    root.mainloop()

main()