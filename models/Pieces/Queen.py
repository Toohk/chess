from ..Piece import Piece


class Queen(Piece):
    def __init__(self, num, team, position):
        Piece.__init__(self, num, team, position)
        self.name = 'queen'

    def set_general_move_possibilities(self):
        self.general_move_possibilities = []
        mp = self.general_move_possibilities
        nw = 0
        ne = 0
        sw = 0
        se = 0
        top = 0
        bottom = 0
        left = 0
        right = 0
        while nw < 7:
            nw += 1
            name = chr(ord(self.position.column) - nw) + str(int(self.position.row) + nw)
            mp.append(name)
            if self.search_piece_in_square(name):
                break

        while ne < 7:
            ne += 1
            name = chr(ord(self.position.column) + ne) + str(int(self.position.row) + ne)
            mp.append(name)
            if self.search_piece_in_square(name):
                break

        while sw < 7:
            sw += 1
            name = chr(ord(self.position.column) - sw) + str(int(self.position.row) - sw)
            mp.append(name)
            if self.search_piece_in_square(name):
                break

        while se < 7:
            se += 1
            name = chr(ord(self.position.column) + se) + str(int(self.position.row) - se)
            mp.append(name)
            if self.search_piece_in_square(name):
                break

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
