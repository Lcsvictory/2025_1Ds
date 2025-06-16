from collections import deque
graph = [
   # 0  1  2  3  4  5  6  7
    [0, 1, 1, 0, 0, 0, 0, 0],  # A(0)
    [1, 0, 0, 1, 0, 0, 0, 0],  # B(1)
    [1, 0, 0, 1, 0, 0, 0, 0],  # C(2)
    [0, 1, 1, 0, 1, 1, 1, 0],  # D(3)
    [0, 0, 0, 1, 0, 1, 0, 0],  # E(4)
    [0, 0, 0, 1, 1, 0, 0, 0],  # F(5)
    [0, 0, 0, 1, 0, 0, 0, 1],  # G(6)
    [0, 0, 0, 0, 0, 0, 1, 0]   # H(7)
]

def dfs(g, i, visited):
    visited[i] = True
    print(chr(ord('A') + i), end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)


def bfs(graph, i, visited:list):
    visited.append(i)
    
    q = deque()
    q.append(i)
    while q:
        current = q.popleft()
        print(chr(65 + current), end=" ")
        for j in range(len(graph[current])):
            if graph[current][j] == 1 and j not in visited:
                q.append(j)
                visited.append(j)


visited_dfs = [False for _ in range(len(graph))]
visited_b = list()
dfs(graph, 4, visited_dfs)
print()
bfs(graph, 4, visited_b)