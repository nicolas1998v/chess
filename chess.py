letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = range(1, 9)
placement = {'A1': '♜', 'A2': '♞', 'A3': '♝', 'A4': '♛', 'A5': '♚', 'A6': '♝', 'A7': '♞', 'A8': '♜',
             'B1': '♟️', 'B2': '♟️', 'B3': '♟️', 'B4': '♟️', 'B5': '♟️', 'B6': '♟️', 'B7': '♟️', 'B8': '♟️',
             'G1': '♙', 'G2': '♙', 'G3': '♙', 'G4': '♙', 'G5': '♙', 'G6': '♙', 'G7': '♙', 'G8': '♙',
             'H1': '♖', 'H2': '♘', 'H3': '♗', 'H4': '♔', 'H5': '♕', 'H6': '♗', 'H7': '♘', 'H8': '♖'}

for letter in letters:
    for number in numbers:
        tile = letter + str(number)
        piece = placement.get(tile, 'x')
        print(piece, end=' ')
    print('\n', end='')





