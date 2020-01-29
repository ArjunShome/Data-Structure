from Code.Graph.Adjacency_Matrix.Graph import Graph

if __name__ == '__main__':
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.print_graph()