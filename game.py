# input board dimensions
while True:
    try:
        c, r = input("Enter your board dimensions: ").strip().split()
        r = int(r)
        c = int(c)
        if r < 1 or c < 1:
            raise Exception
    except(ValueError, Exception):
        print('Invalid dimension!')
    else:
        break
# input knights starting position
while True:
    try:
        x, y = input("Enter the knight's starting position: ").strip().split()
        x = int(x)
        y = int(y)
        if x < 1 or x > c or y < 1 or y > r:
            raise Exception
    except(ValueError, Exception):
        print('Invalid position!')
    else:
        break

# declaring a matrix dictionary with coordinates as keys
matrix = dict()
for i in range(1, r + 1):
    for j in range(1, c + 1):
        matrix[(j, i)] = None

# cell size used for formatting the board upon output
cell_size = len(str(c * r))


# checks whether a position has been visited before by checking the value of matrix dict
def is_occupied(a, b):
    if matrix[(a, b)] is None:
        return False
    else:
        return True


# returns length of possible moves in the form of a list of coordinates
def count_possible_moves(a, b):
    return len(possible_moves(a, b))


# updates the board used for output
def update_board():
    global board
    for coord in possible_moves(x, y):
        i = coord[0]
        j = coord[1]
        board[j - 1][i - 1] = ' ' * (cell_size - 1) + str(count_possible_moves(i, j))


# returns list of possible moves as coordinates
def possible_moves(a, b):
    possible_moves_list = []
    if c + 1 > a + 2 > 0:
        if r + 1 > b + 1 > 0 and not is_occupied(a + 2, b + 1):
            possible_moves_list.append((a + 2, b + 1))
        if r + 1 > b - 1 > 0 and not is_occupied(a + 2, b - 1):
            possible_moves_list.append((a + 2, b - 1))
    if c + 1 > a - 2 > 0:
        if r + 1 > b + 1 > 0 and not is_occupied(a - 2, b + 1):
            possible_moves_list.append((a - 2, b + 1))
        if r + 1 > b - 1 > 0 and not is_occupied(a - 2, b - 1):
            possible_moves_list.append((a - 2, b - 1))
    if c + 1 > a + 1 > 0:
        if r + 1 > b + 2 > 0 and not is_occupied(a + 1, b + 2):
            possible_moves_list.append((a + 1, b + 2))
        if r + 1 > b - 2 > 0 and not is_occupied(a + 1, b - 2):
            possible_moves_list.append((a + 1, b - 2))
    if c + 1 > a - 1 > 0:
        if r + 1 > b + 2 > 0 and not is_occupied(a - 1, b + 2):
            possible_moves_list.append((a - 1, b + 2))
        if r + 1 > b - 2 > 0 and not is_occupied(a - 1, b - 2):
            possible_moves_list.append((a - 1, b - 2))
    return possible_moves_list


# sorts the list of possible moves according to the Wandorff's rule
def sort_possible_moves(list_):
    for i in range(len(list_) - 1):
        for j in range(len(list_) - i - 1):
            if count_possible_moves(list_[j][0], list_[j][1]) > count_possible_moves(list_[j + 1][0], list_[j + 1][1]):
                list_[j], list_[j + 1] = list_[j + 1], list_[j]


def borders():
    print(' ' * (len(str(r))) + '-' * (c * (cell_size + 1) + 3))


board = [['' for _ in range(c)] for _ in range(r)]
matrix[(x, y)] = 'X'


# resets the board to get rid of previous possible moves drawn on it, once the user makes a move
def reset_board():
    global board
    for i in range(r):
        for j in range(c):
            if matrix[(j + 1, i + 1)] is None:
                board[i][j] = "_" * cell_size
            else:
                board[i][j] = " " * (cell_size - 1) + str(matrix[(j + 1, i + 1)])


# outputs the board
def draw_board():
    borders()
    for i in range(r, 0, -1):
        print(' ' * (cell_size - len(str(i)) - 1) + str(i) + '| ', end='')
        for j in range(c):
            print(board[i - 1][j], end=' ')
        print('|')
    borders()
    print(' ' * (len(str(r)) + 1), end='')
    for j in range(1, c + 1):
        print(' ' * (1 + cell_size - len(str(j))) + str(j), end='')


# allows user to play the game
def play_game():
    global x
    global y
    moves_counter = 1
    while count_possible_moves(x, y) > 0:
        moves_counter += 1
        reset_board()
        board[y - 1][x - 1] = ' ' * (cell_size - 1) + 'X'
        matrix[(x, y)] = 'X'
        update_board()
        draw_board()
        print()
        while True:
            try:
                x_temp, y_temp = input("Enter your next move: ").strip().split()
                x_temp = int(x_temp)
                y_temp = int(y_temp)
                if x_temp < 1 or x_temp > c or y_temp < 1 or y_temp > r\
                        or (x_temp, y_temp) not in possible_moves(x, y):
                    raise Exception
            except(ValueError, Exception):
                print('Invalid move!', end='')
            else:
                break
        matrix[(x, y)] = '*'
        x = x_temp
        y = y_temp

    matrix[(x, y)] = '*'
    win = True
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if matrix[(j, i)] != '*':
                win = False
                break

    print()
    if win:
        print("What a great tour! Congratulations!")
    else:
        print("No more possible moves!")
        print("Your knight visited {} squares!".format(moves_counter))


# computer solves the game for you
def computer_play():
    global x
    global y
    print("Here's the solution!")
    solve_knights_tour(x, y)
    borders()
    for i in range(r, 0, -1):
        print(' ' * (cell_size - len(str(i)) - 1) + str(i) + '| ', end='')
        for j in range(1, c + 1):
            print(' ' * (cell_size - len(matrix[(j, i)])) + matrix[(j, i)], end=' ')
        print('|')
    borders()
    print(' ' * (len(str(r)) + 1), end='')
    for j in range(1, c + 1):
        print(' ' * (1 + cell_size - len(str(j))) + str(j), end='')


# recursion backtracking algorithm for finding the correct solution to the game
def solve_knights_tour(a, b):
    counter = 1

    def solution(a, b):
        nonlocal counter
        global matrix
        matrix[(a, b)] = str(counter)
        counter += 1

        if count_possible_moves(a, b) == 0:
            for pair in matrix:
                if matrix[pair] is None:
                    matrix[(a, b)] = None
                    counter -= 1
                    return False
            return True
        move_options = possible_moves(a, b)
        sort_possible_moves(move_options)
        for move in move_options:
            if solution(move[0], move[1]):
                return True
            else:
                continue
        return False

    return solution(a, b)


# ask user whether they want to play the game themselves
want_to_play = input('Do you want to try the puzzle? (y/n): ')
while want_to_play not in ('y', 'n'):
    print('Invalid input!')
    want_to_play = input('Do you want to try the puzzle? (y/n): ')

if want_to_play == 'y':
    if not solve_knights_tour(x, y):
        print("No solution exists!")
        quit()
    for pair in matrix:
        matrix[pair] = None
    play_game()
else:
    if not solve_knights_tour(x, y):
        print("No solution exists!")
        quit()
    computer_play()
