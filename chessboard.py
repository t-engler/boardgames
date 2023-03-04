from chesspieces import Chesspiece


class Chessboard:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        print(self.board)

    def place_piece(self, piece: Chesspiece, row: int, column: int) -> None:
        self.board[row][column] = piece

    def remove_piece(self, row: int, column: int) -> None:
        self.board[row][column] = None

    def retrieve_piece(self, row: int, column: int) -> Chesspiece | None:
        return self.board[row][column]

    def move_piece(
        self, row_origin: int, column_origin: int, row_target: int, column_target: int
    ) -> None:
        piece = self.retrieve_piece(row=row_origin, column=column_origin)
        self.remove_piece(row=row_origin, column=column_origin)
        self.place_piece(piece=piece, row=row_target, column=column_target)

    def possible_moves_for_piece(self, row: int, column: int):
        pass

    def possible_captures_for_piece(self, row: int, column: int):
        pass
