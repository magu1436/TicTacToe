

import tkinter as tk

from displays import GameDisplay


def main():
    root = tk.Tk()
    root.state("zoomed")
    root.update_idletasks()
    game_display = GameDisplay(root)
    game_display.place(x=0, y=0, anchor="nw")
    root.mainloop()

main()