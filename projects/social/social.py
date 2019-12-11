import random
from collections import deque


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        #  call add_user() until our number of users == num_users
        for i in range(num_users):
            self.add_user(f"User {i + 1}")

        # Create friendships
        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users

        # Create a list with all possible friendship combinations
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        # print(possible_friendships)

        # Grab the first N elements from the list
        # Number of times to call add_friendship = avg_friendships * num_users / 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_neighbors(self, user_id):
        return self.friendships[user_id]

    def bfs(self, user_id, friend_id):
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = deque()
        q.appendleft([user_id])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty:
        while len(q) > 0:
            # Dequeue the first PATH
            path = q.pop()
            # print("path: ", path)
            # Grab the last vertex from the PATH
            last_friend = path[-1]
            # If that vertex has not been visited...
            if not last_friend in visited:
                # Check if it's the target
                if last_friend == friend_id:
                    # If so, return path
                    return path
                # Mark it as visited
                visited.add(last_friend)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_friend):
                    # Copy the path
                    path_copy = path.copy()
                    # Append the neighbor to the back
                    path_copy.append(neighbor)
                    q.appendleft(path_copy)

    def get_all_social_paths(self, user_id):
        """1
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        HINT: shortest path => BFS!!!

        The key is the friend's ID and the value is the path.
        """
        q2 = deque()
        q2.appendleft(user_id)
        visited = {}  # Note that this is a dictionary, not a set
        while len(q2) > 0:
            f = q2.pop()
            if f not in visited:
                # print("f: ", f)
                if user_id is not f:
                    visited[f] = self.bfs(user_id, f)
                for neighbor in self.get_neighbors(f):
                    q2.appendleft(neighbor)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("Friendships graph: ", sg.friendships)
    # print(sg.users)
    connections = sg.get_all_social_paths(1)
    print("Connections to each friend from 1: ", connections)
