import random
from util import Stack, Queue  

class User:
    def __init__(self, name):
        self.name = name

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
        # !!!! IMPLEMENT ME

        # Add users
        user_count = 0
        while user_count < num_users:
            self.add_user(f"User_{self.last_id + 1}")
            user_count += 1

        # Create friendships
        num_friends = num_users * avg_friendships
        friend_count = 0
        while friend_count < num_friends:
            friend_id, friend = random.choice(list(self.friendships.items()))
            user_id, user = random.choice(list(self.users.items()))
            while friend_id == user_id:
                user_id, user = random.choice(list(self.users.items()))
            while user in friend:
                user_id, user = random.choice(list(self.users.items()))
            self.friendships[friend_id].add(user_id)
            self.friendships[user_id].add(friend_id)
            friend_count += 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # return visited

        def bfs(starting_vertex, destination_vertex):
            """
            Return a list containing the shortest path from
            starting_vertex to destination_vertex in
            breath-first order.
            """
            q = Queue()
            q.enqueue(starting_vertex)
            visited = set()
            path = {}
            path[starting_vertex] = None

            while q.size() > 0:
                v = q.dequeue()
                if v not in visited:
                    if v == destination_vertex:
                        shortest_path = []
                        shortest_path.insert(0, destination_vertex)
                        curr = path[destination_vertex]
                        while curr != None:
                            shortest_path.insert(0, curr)
                            curr = path[curr]
                        return shortest_path
                    visited.add(v)
                    for next_vert in self.friendships[v]:
                        if next_vert not in visited:
                            path[next_vert] = v
                        q.enqueue(next_vert)

        connections = {}

        for user in self.users:
            connections[user] = []

        for path in connections:
            # print("\n")
            # print(bfs(user_id, path))
            short = bfs(user_id, path)
            if short != None:
                connections[path] = short

        return connections


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
