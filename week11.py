class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def print_graph(self):
        for r in range(self.size):
            for c in range(self.size):
                print(self.graph[r][c], end=' ')
            print()


G1 = Graph(4)
G2 = Graph(4)
G_self = Graph(4)


# 0 == A, 1 == B, 2 == C, 3 == D
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("G1 무방향 그래프")
G1.print_graph()


# 0 == A, 1 == B, 2 == C, 3 == D
G2.graph[0][1] = 1; G2.graph[0][2] = 1
G2.graph[3][0] = 1; G2.graph[3][2] = 1

print("G2 방향 그래프")
G2.print_graph()

# 0 == A, 1 == B, 2 == C, 3 == D
G_self.graph[0][3] = 1
G_self.graph[1][2] = 1; G_self.graph[1][3] = 1
G_self.graph[2][1] = 1
G_self.graph[3][0] = 1; G_self.graph[3][1] = 1

print("G_self 무방향 그래프")
G_self.print_graph()
