import random

def next_empty(Board, i, j):
    idx = i*len(Board[0]) + j
    for idx in range(i*len(Board[0]) + j, len(Board[0])* len(Board)):
        x = idx//len(Board[0])
        y = idx%len(Board[0])
        if Board[x][y]=='*':
            return (x, y)
    return (-1, -1)

def make_board(x, y):
    return [['*' for x in range(y)] for x in range(x)]

def make_tiles(n):
    Tiles = []
    for x in range(0, n+1):
        for y in range(x, n+1):
            Tiles = Tiles + [[x, y]]
    return Tiles

def check(Board, i, j, ori):
    #Horizontal
    r = False
    if ori==0:
        if j<len(Board[i])-1:
            if Board[i][j]=='*' and  Board[i][j+1]=='*':
                r = True
    #Vertical
    elif ori==1:
         if i<len(Board)-1:
            if Board[i][j]=='*' and Board[i+1][j]=='*':
                r =  True
    return r

def place_tile(Board, i, j, ori, tile):
    Board[i][j] = tile[0]
    if ori == 0:
        Board[i][j+1] = tile[1]
    else:
        Board[i+1][j] = tile[1]

def create_puzzle(n):
    """
    es posible que el algoritmo generador falle y no encuentre un tablero válido
    Si sucede, retorna falso y no genera ningún archivo de salida
    """

    board = make_board(n+1, n+2)
    tiles = make_tiles(n)
    random.shuffle(tiles)
    solution = []

    current_pos = (0, 0)
    while tiles != []:
        next_tile = tiles.pop()
        random.shuffle(next_tile)
        current_pos = next_empty(board, current_pos[0], current_pos[1])
        ori = random.randint(0,1)
        if not(check(board, current_pos[0], current_pos[1], ori)):
            ori = (ori+1)%2
        if check(board, current_pos[0], current_pos[1], ori):
            place_tile(board, current_pos[0],current_pos[1], ori, next_tile)
            solution = solution + [ori]
        else:
            return False
    toFile("TableroDoble" + str(n), n, board, solution)
    return board

def toFile(filename, n, board, solution):    
    file = open(filename+ ".txt", "w")
    file.write(str(n) +  "\n")
    file.write("\n")

    #tablero
    for fila in board:
        for e in fila:
            file.write(str(e) + " ")
        file.write("\n")
    file.write("\n")
            
    for i in solution:
        file.write(str(i) + " ")
    file.write("\n")


create_puzzle(7)

