from ..Piece import Piece


class Knight(Piece):
    def __init__(self, num, team, position):
        Piece.__init__(self, num, team, position)
        self.name = 'knight'

    def set_general_move_possibilities(self):
        self.general_move_possibilities = []
        mp = self.general_move_possibilities
        top = str(int(self.position.row) + 2)
        mp.append(chr(ord(self.position.column) - 1) + top)
        mp.append(chr(ord(self.position.column) + 1) + top)
        bottom = str(int(self.position.row) - 2)
        mp.append(chr(ord(self.position.column) - 1) + bottom)
        mp.append(chr(ord(self.position.column) + 1) + bottom)
        left = chr(ord(self.position.column) - 2)
        mp.append(left + str(int(self.position.row) - 1))
        mp.append(left + str(int(self.position.row) + 1))
        right = chr(ord(self.position.column) + 2)
        mp.append(right + str(int(self.position.row) - 1))
        mp.append(right + str(int(self.position.row) + 1))

