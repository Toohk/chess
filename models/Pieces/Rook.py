from ..Piece import Piece


class Rook(Piece):
    def __init__(self, num, team, position):
        Piece.__init__(self, num, team, position)
        self.name = 'rook'

    def set_general_move_possibilities(self):
        self.general_move_possibilities = []
        mp = self.general_move_possibilities
        top = 0
        bottom = 0
        left = 0
        right = 0
        while top < 7:
            top += 1
            name = self.position.column + str(int(self.position.row) + top)
            mp.append(name)
            if self.search_piece_in_square(name):
                break

        while bottom < 7:
            bottom += 1
            name = self.position.column + str(int(self.position.row) - bottom)
            mp.append(name)
            if self.search_piece_in_square(name):
                break

        while left < 7:
            left += 1
            name = chr(ord(self.position.column) - left) + self.position.row
            mp.append(name)
            if self.search_piece_in_square(name):
                break

        while right < 7:
            right += 1
            name = chr(ord(self.position.column) + right) + self.position.row
            mp.append(name)
            if self.search_piece_in_square(name):
                break