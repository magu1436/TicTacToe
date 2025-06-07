

import tkinter as tk

from displays import GameDisplay, HomeDisplay


def main():
    root = tk.Tk()
    root.state("zoomed")
    root.update_idletasks()

    game = GameDisplay(root)
    game.place(x=0, y=0)
    game.lower()

    home = HomeDisplay(root)
    home.place(x=0, y=0)
    home.tkraise()

    root.mainloop()

main()