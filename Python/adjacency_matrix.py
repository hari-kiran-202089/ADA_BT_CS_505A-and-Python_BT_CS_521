# Edge list to adjacency matrix of weighted undirected graph

class Graph:
    def __init__(self, total_vertices):
        self.matrix = [[0]*total_vertices for b in range(total_vertices)]
        self.size = total_vertices

    # Method to add edges to matrix
    def add_edge(self, v1, v2, w=1):
        self.matrix[v1][v2] = w
        self.matrix[v2][v1] = w

    # returns to total vertices
    def __len__(self):
        return self.size

    # prints matrix
    def display(self):
        for row in self.matrix:
            print(row)


if __name__ == '__main__':

    # Inputs
    v = int(input("Enter Number of vertices: "))
    num_edges = int(input("Enter number of edges: "))

    print("\nStart entering edges (s,d,w): ")
    edges = [list(map(int, input().split(" "))) for i in range(num_edges)]

    # Graph object
    g = Graph(v)

    # adding edges
    for edge in edges:
        v1, v2, w = edge
        g.add_edge(v1, v2, w)

    print("\nAdjacency Matrix is ")
    g.display()
