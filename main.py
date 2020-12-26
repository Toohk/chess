from models.Board import Board

b1 = Board()
b1.set_squares()
b1.set_piece()

p5 = b1.search_piece_in_square('H1')
c5 = b1.search_square('F4')
p5.set_position(c5)


p6 = b1.search_piece_in_square('E1')
c6 = b1.search_square('E3')
p6.set_position(c6)
b1.update_all_positions()

print(p6.name + '(' + p6.team + p6.position.name + ')')
print(p6.validate_move_possibilities)
p6.move_to(b1.search_square('D4'))

print(p6.position.name)
print(p6.validate_move_possibilities)




