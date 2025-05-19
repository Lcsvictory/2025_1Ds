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

def bfs(g, i, visited, q):
    visited[i] = True
    print(chr(ord('A') + i), end=' ')
    is_input = False
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            q.append(j)
            is_input = True
    if not is_input : return
    bfs(g, q.popleft(), visited, q)


visited_dfs = [False for _ in range(len(graph))]
visited_bfs = [False for _ in range(len(graph))]
queue = deque()
dfs(graph, 3, visited_dfs)
print()
bfs(graph, 3, visited_bfs, queue)