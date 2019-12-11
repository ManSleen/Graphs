"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.visited = set()

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            current_node = queue.dequeue()
            if current_node not in visited:
                visited.add(current_node)
                print("Node: ", current_node)
                for neighbor in self.get_neighbors(current_node):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                print("Node: ", current_node)
                for neighbor in self.get_neighbors(current_node):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Mark the node as visited
        # Call `dft_recursive` on each neighbor that has not been visited
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        queue = Queue()
        queue.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty:
        while queue.size() > 0:
            # Dequeue the first PATH
            current_path = queue.dequeue()
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
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_vertex):
                    new_path = [*current_path, neighbor]
                    queue.enqueue(new_path)
                    # Copy the path
                    # Append the neighbor to the back

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        self.stack = Stack()
        self.stack.push([starting_vertex])
        # Create a Set to store visited vertices
        self.visited = set()
        # While the stack is not empty:
        while self.stack.size() > 0:
            # Pop the first PATH
            current_path = self.stack.pop()
            # print("current path: ", current_path)
            # Grab the last vertex from the PATH
            last_vertex = current_path[-1]
            # If that vertex has not been visited...
            if last_vertex not in self.visited:
                # Check if it's the target
                if last_vertex == destination_vertex:
                    return current_path
                    # If so, return path
                # Mark it as visited
                self.visited.add(last_vertex)
                # Then add A PATH TO its neighbors to the top of the stack
                for neighbor in self.get_neighbors(last_vertex):
                    new_path = [*current_path, neighbor]
                    self.stack.push(new_path)
                    # Copy the path
                    # Append the neighbor to the back

    def dfs_recursive(self, starting_vertex, destination_vertex, visited, path_list):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        current_node = starting_vertex
        if current_node not in visited:
            path_list.append(current_node)
            visited.add(current_node)

            if starting_vertex == destination_vertex:
                print(path_list)

            for neighbor in self.get_neighbors(starting_vertex):
                self.dfs_recursive(
                    neighbor, destination_vertex, visited, path_list)

    # THIs ONE WORKS!!! vvvvv

    def dfs_recursive2(self, starting_vertex, destination_vertex, visited=None, path=None):
        # Init visited
        if visited is None:
            visited = set()
        # Init path
        if path is None:
            path = []
        visited.add(starting_vertex)
        # Add vertex to the path
        path = path + [starting_vertex]
        # If we are at the target value, return the path
        if starting_vertex == destination_vertex:
            return path
        # Otherwise call the dfs_recursive function on each unvisited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive2(
                    neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 5)
    graph.add_edge(5, 3)
    graph.add_edge(2, 4)
    graph.add_edge(4, 7)
    graph.add_edge(4, 6)
    graph.add_edge(7, 6)
    graph.add_edge(7, 1)
    graph.add_edge(6, 3)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    # print(graph.get_neighbors(2))
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(6)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)

    # visited = set()
    # graph.dft_recursive(1, visited)
    # graph.dft_recursive(1, visited)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # visited = set()
    # path_list = []
    print(graph.dfs_recursive2(1, 6))
