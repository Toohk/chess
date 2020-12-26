from models.Square import Square
from models.Rules import Rules
from models.Pieces.King import King
from models.Pieces.Queen import Queen
from models.Pieces.Bishop import Bishop
from models.Pieces.Knight import Knight
from models.Pieces.Rook import Rook
from models.Pieces.Pawn import Pawn


class Board:
    def __init__(self):
        self.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.rows = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.squares = []
        self.squares_name = []
        self.rules = Rules()
        self.pieces = []
        self.pieces_out = []
        self.positions = []

    def set_squares(self):
        for c in self.columns:
            lines_square = []
            for r in range(len(self.columns)):
                case = Square(c, self.rows[r])
                lines_square.append(case)
                self.squares_name.append(c + self.rows[r])
            self.squares.extend(lines_square)


    def set_piece(self):
        for n_king in range(1):
            self.pieces.append(King(n_king, 'white', None))
            self.pieces.append(King(n_king, 'black', None))
        for n_queen in range(1):
            self.pieces.append(Queen(n_queen, 'white', None))
            self.pieces.append(Queen(n_queen, 'black', None))
        for n_bishop in range(2):
            self.pieces.append(Bishop(n_bishop, 'white', None))
            self.pieces.append(Bishop(n_bishop, 'black', None))
        for n_knight in range(2):
            self.pieces.append(Knight(n_knight, 'white', None))
            self.pieces.append(Knight(n_knight, 'black', None))
        for n_rook in range(2):
            self.pieces.append(Rook(n_rook, 'white', None))
            self.pieces.append(Rook(n_rook, 'black', None))
        for n_pawn in range(8):
            self.pieces.append(Pawn(n_pawn, 'white', None))
            self.pieces.append(Pawn(n_pawn, 'black', None))
        self.set_default_place_square()

    def search_square(self, name):
        for square in self.squares:
            if square.name == name:
                return square

    def set_default_place_square(self):
        for piece in self.pieces:
            if isinstance(piece, King):
                if piece.team == 'white':
                    piece.position = self.search_square('E1')
                if piece.team == 'black':
                    piece.position = self.search_square('E8')
            if isinstance(piece, Queen):
                if piece.team == 'white':
                    piece.position = self.search_square('D1')
                if piece.team == 'black':
                    piece.position = self.search_square('D8')
            if isinstance(piece, Bishop):
                if piece.team == 'white':
                    if piece.id == 0:
                        piece.position = self.search_square('C1')
                    if piece.id == 1:
                        piece.position = self.search_square('F1')
                if piece.team == 'black':
                    if piece.id == 0:
                        piece.position = self.search_square('C8')
                    if piece.id == 1:
                        piece.position = self.search_square('F8')
            if isinstance(piece, Knight):
                if piece.team == 'white':
                    if piece.id == 0:
                        piece.position = self.search_square('B1')
                    if piece.id == 1:
                        piece.position = self.search_square('G1')
                if piece.team == 'black':
                    if piece.id == 0:
                        piece.position = self.search_square('B8')
                    if piece.id == 1:
                        piece.position = self.search_square('G8')
            if isinstance(piece, Rook):
                if piece.team == 'white':
                    if piece.id == 0:
                        piece.position = self.search_square('A1')
                    if piece.id == 1:
                        piece.position = self.search_square('H1')
                if piece.team == 'black':
                    if piece.id == 0:
                        piece.position = self.search_square('A8')
                    if piece.id == 1:
                        piece.position = self.search_square('H8')
            if isinstance(piece, Pawn):
                if piece.team == 'white':
                    if piece.id == 0:
                        piece.position = self.search_square('A2')
                    if piece.id == 1:
                        piece.position = self.search_square('B2')
                    if piece.id == 2:
                        piece.position = self.search_square('C2')
                    if piece.id == 3:
                        piece.position = self.search_square('D2')
                    if piece.id == 4:
                        piece.position = self.search_square('E2')
                    if piece.id == 5:
                        piece.position = self.search_square('F2')
                    if piece.id == 6:
                        piece.position = self.search_square('G2')
                    if piece.id == 7:
                        piece.position = self.search_square('H2')
                if piece.team == 'black':
                    if piece.id == 0:
                        piece.position = self.search_square('A7')
                    if piece.id == 1:
                        piece.position = self.search_square('B7')
                    if piece.id == 2:
                        piece.position = self.search_square('C7')
                    if piece.id == 3:
                        piece.position = self.search_square('D7')
                    if piece.id == 4:
                        piece.position = self.search_square('E7')
                    if piece.id == 5:
                        piece.position = self.search_square('F7')
                    if piece.id == 6:
                        piece.position = self.search_square('G7')
                    if piece.id == 7:
                        piece.position = self.search_square('H7')
                piece.set_general_move_possibilities()
        self.update_all_positions()


    def search_piece_in_square(self, name):
        square = self.search_square(name)
        for piece in self.pieces:
            if piece.position == square:
                return piece

    def update_all_positions(self):
        for piece in self.pieces:
            piece.all_pieces = self.pieces
            piece.all_squares = self.squares_name