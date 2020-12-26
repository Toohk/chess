class Piece:
    def __init__(self, num, team, position):
        self.id = num
        self.team = team
        self.position = position
        self.general_move_possibilities = []
        self.validate_move_possibilities = []
        self.all_pieces = []
        self.all_squares = []
        self.collision_pieces = []
        self.in_game = True

    def set_general_move_possibilities(self):
        pass

    def set_constraint(self):
        pass

    def search_piece_in_square(self, name):
        for piece in self.all_pieces:
            if piece.position.name == name:
                return piece

    def set_general_constraint(self):
        null_square = []
        for square in self.general_move_possibilities:
            if square not in self.all_squares:
                null_square.append(square)
        for ns in null_square:
            self.general_move_possibilities.remove(ns)
        self.validate_move_possibilities = self.general_move_possibilities
        for piece in self.collision_pieces:
            if self.team == piece.team:
                self.validate_move_possibilities.remove(piece.position.name)
        self.set_constraint()

    def move_to(self, square):
        if square.name in self.validate_move_possibilities:
            self.position = square
            self.set_general_move_possibilities()
            self.calculate_collision()
            print(self.position.name)
        else:
            print('error')

    def calculate_collision(self):
        for piece in self.all_pieces:
            if piece.position.name in self.general_move_possibilities:
                self.collision_pieces.append(piece)
        self.validate_move_possibilities = []
        self.set_general_constraint()

    def set_position(self, square):
        self.position = square
        self.set_general_move_possibilities()
        self.calculate_collision()