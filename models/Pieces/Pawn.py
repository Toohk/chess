from ..Piece import Piece


class Pawn(Piece):
    def __init__(self, num, team, position):
        Piece.__init__(self, num, team, position)
        self.name = 'pawn'

    def set_general_move_possibilities(self):
        self.general_move_possibilities = []
        mp = self.general_move_possibilities
        if self.team == 'white':
            if self.position.row != '8':
                mp.append(self.position.column + str(int(self.position.row) + 1))
                if self.position.row == '2':
                    mp.append(self.position.column + str(int(self.position.row) + 2))
                if self.position.column != 'A':
                    mp.append(chr(ord(self.position.column) - 1) + str(int(self.position.row) + 1))
                if self.position.column != 'H':
                    mp.append(chr(ord(self.position.column) + 1) + str(int(self.position.row) + 1))
        if self.team == 'black':
            if self.position.row != '1':
                mp.append(self.position.column + str(int(self.position.row) - 1))
                if self.position.row == '7':
                    mp.append(self.position.column + str(int(self.position.row) - 2))
                if self.position.column != 'A':
                    mp.append(chr(ord(self.position.column) - 1) + str(int(self.position.row) - 1))
                if self.position.column != 'H':
                    mp.append(chr(ord(self.position.column) + 1) + str(int(self.position.row) - 1))

    def set_constraint(self):
        for piece in self.collision_pieces:
            if self.team == 'white':
                if piece.position.name == self.position.column + str(int(self.position.row) + 1):
                    self.validate_move_possibilities.remove(piece.position.name)
                if piece.position.name == self.position.column + str(int(self.position.row) + 2):
                    self.validate_move_possibilities.remove(piece.position.name)
            if self.team == 'black':
                if piece.position.name == self.position.column + str(int(self.position.row) - 1):
                    self.validate_move_possibilities.remove(piece.position.name)
                if piece.position.name == self.position.column + str(int(self.position.row) - 2):
                    self.validate_move_possibilities.remove(piece.position.name)