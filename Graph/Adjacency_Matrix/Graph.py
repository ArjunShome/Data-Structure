# Adjacency Graph representation

class Graph:
    def __init__(self, size):
        self.graph_size = size
        self.matrix = []
        for i in range(size):
            self.matrix.append([0 for i in range(size)])

    def add_edge(self, v1, v2):
        if v1 and v2 == 1:
            print(f"Edge Already exists between {v1} and {v2}")
            return
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1

    def delete_edge(self, v1, v2):
        if v1 and v2 == 0:
            print(f'Edge Does not exists between {v1} and {v2}')
            return
        self.matrix[v1][v2] = 0
        self.matrix[v2][v1] = 0

    def get_size(self):
        return self.graph_size

    def print_graph(self):
        for rows in self.matrix:
            print(str(rows)[1:-1])