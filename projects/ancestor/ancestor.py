from collections import deque


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.visited = set()

    def __repr__(self):
        for vertex in self.vertices:
            return f"{vertex}"

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        stack = deque()
        stack.append([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty:
        while len(stack) > 0:
            # Pop the first PATH
            current_path = stack.pop()
            # print("current path: ", current_path)
            # Grab the last vertex from the PATH
            last_vertex = current_path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # Check if it's the target
                if last_vertex == destination_vertex:
                    return current_path
                    # If so, return path
                # Mark it as visited
                visited.add(last_vertex)
                # Then add A PATH TO its neighbors to the top of the stack
                for neighbor in self.get_neighbors(last_vertex):
                    new_path = [*current_path, neighbor]
                    stack.append(new_path)
                    # Copy the path
                    # Append the neighbor to the back


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    paths = []
    for ancestor in ancestors:
        (person1, person2) = (ancestor[0], ancestor[1])
        g.add_vertex(person1)
        g.add_vertex(person2)

    for pair in ancestors:
        g.add_edge(pair[0], pair[1])

    for vertex in g.vertices:
        if g.dfs(vertex, starting_node) is not None:
            paths.append(g.dfs(vertex, starting_node))

    all_paths = sorted(paths, key=len, reverse=True)
    lowest = all_paths[0][0]
    for x in all_paths:
        if len(x) == len(all_paths[0]):
            if x[0] < lowest:
                lowest = x[0]

    if lowest == starting_node:
        return -1
    else:
        return lowest


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1), (14, 10), (15, 4), (16, 15), (12, 10), (17, 15)]


print(earliest_ancestor(test_ancestors, 3))
