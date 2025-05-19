from collections import deque
graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def dfs(g, i, visited):
    visited[i] = True
    print(chr(ord('A') + i), end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

def bfs(g, start):
    visited = [False for _ in range(len(graph))]
    visited[start] = True
    q = deque()
    q.append(start)
    while q:
        current = q.popleft()
        print(chr(ord('A') + current), end=' ')
        for j in range(len(graph)):
            if g[current][j] == 1 and not visited[j]:
                visited[j] = True
                q.append(j)


visited_dfs = [False for _ in range(len(graph))]
queue = deque()
dfs(graph, 3, visited_dfs)
print()
bfs(graph, 4)