# Edge list to adjacency list of weighted undirected graph

def edges_to_adjacency_list(edges):
    adjacency_list = {}

    for edge in edges:
        v1, v2, w = edge
        if v1 in adjacency_list:
            adjacency_list[v1].append((v2, w))
        else:
            adjacency_list[v1] = [(v2, w)]

        if v2 in adjacency_list:
            adjacency_list[v2].append((v1, w))
        else:
            adjacency_list[v2] = [(v1, w)]

    return adjacency_list


if __name__ == "__main__":

    v = int(input("Enter Number of vertices: "))
    num_edges = int(input("Enter number of edges: "))

    print("\nStart entering edges (s,d,w): ")
    edges = [list(map(int, input().split(" "))) for i in range(num_edges)]

    adjacency_list = edges_to_adjacency_list(edges)

    print("\nAdjacency List is: ")
    for vertex in adjacency_list.keys():
        print(f"{vertex} -> {adjacency_list[vertex]}")
