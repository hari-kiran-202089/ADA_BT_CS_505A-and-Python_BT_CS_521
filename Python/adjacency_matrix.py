# Edge list to adjacency matrix of weighted undirected graph

def edges_to_adjacency_matrix(edges, total_vertices):

    # creating a matrix of size total vertices
    matrix = [[0]*total_vertices for b in range(total_vertices)]

    # filling the weights using edges
    for edge in edges:
        v1, v2, w = edge  # unpacking the values

        # Assuming That vertices values starts from 0
        matrix[v1][v2] = w
        matrix[v2][v1] = w

    return matrix


if __name__ == '__main__':

    # Inputs
    v = int(input("Enter Number of vertices: "))
    num_edges = int(input("Enter number of edges: "))

    print("\nStart entering edges (s,d,w): ")
    edges = [list(map(int, input().split(" "))) for i in range(num_edges)]

    matrix = edges_to_adjacency_matrix(edges, v)

    print("\nAdjacency Matrix is ")
    for row in matrix:
        print(row)
