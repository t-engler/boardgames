from typing import Protocol
from chessboard import Chessboard
from chesspieces import Chesscolor, Rook, Knight, Bishop, Queen, King, Pawn


class GUI(Protocol):
    def display_board(self, board: Chessboard) -> None:
        pass


class Chessgame:
    def __init__(self, gui: GUI, board: Chessboard):
        self.gui = gui
        self.board = board
        self.current_player = None

    def setup_game(self) -> None:
        self.current_player = Chesscolor.WHITE

        self.board.place_piece(piece=Rook(Chesscolor.WHITE), column=7, row=0)
        self.board.place_piece(piece=Knight(Chesscolor.WHITE), column=7, row=1)
        self.board.place_piece(piece=Bishop(Chesscolor.WHITE), column=7, row=2)
        self.board.place_piece(piece=Queen(Chesscolor.WHITE), column=7, row=3)
        self.board.place_piece(piece=King(Chesscolor.WHITE), column=7, row=4)
        self.board.place_piece(piece=Bishop(Chesscolor.WHITE), column=7, row=5)
        self.board.place_piece(piece=Knight(Chesscolor.WHITE), column=7, row=6)
        self.board.place_piece(piece=Rook(Chesscolor.WHITE), column=7, row=7)
        for i in range(8):
            self.board.place_piece(piece=Pawn(Chesscolor.WHITE), column=6, row=i)

        self.board.place_piece(piece=Rook(Chesscolor.BLACK), column=0, row=0)
        self.board.place_piece(piece=Knight(Chesscolor.BLACK), column=0, row=1)
        self.board.place_piece(piece=Bishop(Chesscolor.BLACK), column=0, row=2)
        self.board.place_piece(piece=Queen(Chesscolor.BLACK), column=0, row=3)
        self.board.place_piece(piece=King(Chesscolor.BLACK), column=0, row=4)
        self.board.place_piece(piece=Bishop(Chesscolor.BLACK), column=0, row=5)
        self.board.place_piece(piece=Knight(Chesscolor.BLACK), column=0, row=6)
        self.board.place_piece(piece=Rook(Chesscolor.BLACK), column=0, row=7)
        for i in range(8):
            self.board.place_piece(piece=Pawn(Chesscolor.BLACK), column=1, row=i)

        self.gui.display_board(self.board)
