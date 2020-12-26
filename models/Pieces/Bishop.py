from ..Piece import Piece


class Bishop(Piece):
    def __init__(self, num, team, position):
        Piece.__init__(self, num, team, position)
        self.name = 'bishop'

    def set_general_move_possibilities(self):
        self.general_move_possibilities = []
        mp = self.general_move_possibilities
        nw = 0
        ne = 0
        sw = 0
        se = 0
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
