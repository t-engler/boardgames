from chessboard import Chessboard
import pygame as pg
import os

from chesspieces import Chesspiece


class Simplegui:
    _ROWS, _COLUMNS = 8, 8
    _CELL_SIZE = 80
    _WIDTH, _HEIGHT = (
        _CELL_SIZE * _ROWS,
        _CELL_SIZE * _COLUMNS,
    )

    _BOARD_COLORS = [pg.Color("white"), pg.Color("grey20")]

    _PIECE_IMAGES = {}

    def __init__(self):
        pg.init()

        self.display_screen = pg.display.set_mode((self._WIDTH, self._HEIGHT))
        pg.display.set_caption("Python Chess")

        for row in range(self._ROWS):
            for column in range(self._COLUMNS):
                color = self._BOARD_COLORS[(row + column) % 2]
                pg.draw.rect(
                    surface=self.display_screen,
                    color=color,
                    rect=pg.Rect(
                        row * self._CELL_SIZE,
                        column * self._CELL_SIZE,
                        self._CELL_SIZE,
                        self._CELL_SIZE,
                    ),
                )

        pg.display.flip()

    @staticmethod
    def _generate_image_name_for_piece(piece: Chesspiece) -> str:
        return "_".join([type(piece).__name__.lower(), piece.color.lower()])

    def _load_image_from_disk(self, piece_image_name: str) -> pg.Surface:
        image = pg.image.load(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "icons",
                "chess",
                f"{piece_image_name}.png",
            )
        )
        image = pg.transform.scale(image, (self._CELL_SIZE, self._CELL_SIZE))
        return image

    def get_image_for_piece(self, piece: Chesspiece) -> pg.Surface:
        piece_image_name = Simplegui._generate_image_name_for_piece(piece)
        piece_image = self._PIECE_IMAGES.setdefault(
            piece_image_name,
            self._load_image_from_disk(piece_image_name),
        )
        return piece_image

    def display_board(self, board: Chessboard):
        for row in range(self._ROWS):
            for column in range(self._COLUMNS):
                piece = board.retrieve_piece(row=row, column=column)
                if not piece:
                    continue
                self.display_screen.blit(
                    self.get_image_for_piece(piece=piece),
                    pg.Rect(
                        row * self._CELL_SIZE,
                        column * self._CELL_SIZE,
                        self._CELL_SIZE,
                        self._CELL_SIZE,
                    ),
                )

        pg.display.flip()

        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
