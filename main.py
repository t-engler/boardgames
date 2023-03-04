from chessboard import Chessboard
from chessgame import Chessgame
from simplegui import Simplegui


def main():
    gui = Simplegui()
    board = Chessboard()
    chessgame = Chessgame(gui=gui, board=board)

    chessgame.setup_game()


if __name__ == "__main__":
    main()
