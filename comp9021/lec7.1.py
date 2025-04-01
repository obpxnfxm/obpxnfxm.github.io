from random import *

density = 0.3
size = 10
grid = [[int(random() < density) for _ in range(size)] for _ in range(size)]

def display_grid():
    for row in grid:
        print(*row)

def display_population():
    square = {0: '\u2b1c', 1: '\u2b1b'}
    for row in grid:
        print(''.join(square[e] for e in row))

def next_generation():
    global grid
    new_grid = [[None] * size for _ in range(size)]
    nb_of_neighbors = 0
    for i in range(size):
        for j in range(size):
            # above left
            if i and j and grid[i-1][j-1]:
                nb_of_neighbors += 1
            # above
            if j and grid[i][j-1]:
                nb_of_neighbors += 1
            # above right
            if i and j < size - 1 and grid[i-1][j+1]:
                nb_of_neighbors += 1
            # left
            if i and grid[i-1][j]:
                nb_of_neighbors += 1
            # right
            if j < size - 1 and grid[i][j+1]:
                nb_of_neighbors += 1
            # below left
            if i and j < size - 1 and grid[i-1][j+1]:
                nb_of_neighbors += 1
            # below
            if i < size - 1 and grid[i+1][j]:
                nb_of_neighbors += 1
            # below right:
            if i < size - 1 and j < size - 1 and grid[i+1][j+1]:
                nb_of_neighbors += 1
            



display_grid()
display_population()