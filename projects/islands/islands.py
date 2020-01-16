from collections import deque

'''
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
'''
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

# island_counter(islands) # returns 4


def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # Check north
    if y > 0 and graph_matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    # Check south
    if y < len(graph_matrix) - 1 and graph_matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1))
    # Check east
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    # Check west
    if x > 0 and graph_matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    print("point: ", vertex, " neighbors: ", neighbors)
    return neighbors


def bft(x, y, matrix, visited):
    q = deque()
    q.appendleft((x, y))

    while len(q) > 0:
        v = q.pop()
        x = v[0]
        y = v[1]
        if not visited[y][x]:
            visited[y][x] = True
            for neighbor in get_neighbors((x, y), matrix):
                q.appendleft(neighbor)

    return visited


def island_counter(matrix):
    # Create a visited matrix
    visited = []

    # Create counter, init counter to 0
    counter = 0

    # Get height and length of matrix to make the 'walking' part easier to understand
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])

    # Make visited matrix same size as original matrix, with every spot filled with 'False'
    for _ in range(matrix_height):
        visited.append([False] * matrix_width)

    print("visited: ", visited)
    # Walk through each cell in the original matrix
    for y in range(matrix_height):
        for x in range(matrix_width):
            print("matrix[y][x]: ", matrix[y][x])
            # print("visited[y][x]: ", visited[y][x])
            # If cell has not been visited:
            if not visited[y][x]:
                # If you reach a '1':
                if matrix[y][x] == 1:
                    # Do a BFT and mark each neighbor as visited
                    visited = bft(x, y, matrix, visited)
                    counter += 1
                    # Increment counter by 1

    return counter


print(island_counter(islands))
