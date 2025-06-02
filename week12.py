class Graph:
    def __init__ (self, size):
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def print_graph(g) :
    print(' ', end = '     ')
    for v in range(len(g.graph)) :
        print(name_ary[v], end =' ')
    print()
    for row in range(len(g.graph)) :
        print(name_ary[row], end =' ')
        for col in range(len(g.graph)) :
            print(f"{g.graph[row][col]:4d}", end=' ')
        print()
    print()

def dfs(g1, start, visited):
    visited.append(start)
    for j in range(len(g1.graph[start])):
        if g1.graph[start][j] != 0 and (j not in visited):
            dfs(g1, j, visited)

def find_vertex(g, target) :
    visited = list()
    dfs(g, 0, visited)
    return True if target in visited else False


if __name__ == "__main__":
    g1 = None
    name_ary = ['한국', '일본', '중국', '태국', '미국', '대만']
    korea, japan, china, thailand, usa, taiwan = 0, 1, 2, 3, 4, 5

    graph_size = 6
    g1 = Graph(graph_size)
    g1.graph[korea][japan] = 45; g1.graph[korea][china] = 32
    g1.graph[japan][korea] = 45; g1.graph[japan][china] = 78; g1.graph[japan][thailand] = 28; g1.graph[japan][usa] = 95
    g1.graph[china][korea] = 32; g1.graph[china][japan] = 78; g1.graph[china][thailand] = 55
    g1.graph[thailand][japan] = 28; g1.graph[thailand][china] = 55; g1.graph[thailand][usa] = 67; g1.graph[thailand][taiwan] = 42
    g1.graph[usa][japan] = 95; g1.graph[usa][thailand] = 67; g1.graph[usa][taiwan] = 83
    g1.graph[taiwan][thailand] = 42; g1.graph[taiwan][usa] = 83

    print('국가 간 여행 비용 연결도')
    print_graph(g1)

    edge_ary = []  # 결과적으로 2d list
    for i in range(graph_size) :
        for k in range(graph_size) :
            if g1.graph[i][k] != 0 :
                edge_ary.append([g1.graph[i][k], i, k])
    print(edge_ary)

    edge_ary.sort(reverse=True, key=lambda x: x[0])
    print(edge_ary)

    new_ary = list()
    for i in range(1, len(edge_ary), 2):
        new_ary.append(edge_ary[i])
    print(new_ary)

    index = 0
    while len(new_ary) > graph_size - 1:	# 간선의 개수가 '정점 개수-1'일 때까지 반복
        start = new_ary[index][1]
        end = new_ary[index][2]
        save_cost = new_ary[index][0]

        g1.graph[start][end] = 0
        g1.graph[end][start] = 0

        start_reachable = find_vertex(g1, start)
        end_reachable = find_vertex(g1, end)

        if start_reachable and end_reachable :
            del new_ary[index]
        else:
            g1.graph[start][end] = save_cost
            g1.graph[end][start] = save_cost
            index = index + 1

    print('최소 비용의 여행 경로 연결도')
    print_graph(g1)

    total_cost = 0
    for i in range(graph_size):
        for k in range(graph_size):
            if g1.graph[i][k] != 0:
                total_cost = total_cost + g1.graph[i][k]

    total_cost = total_cost // 2 # 무방향그래프에선 양쪽의 비용이 2개씩 존재하니까 하나의 비용만을 기준으로 더해야한다.
    print(f"최소 비용으로 모든 국가를 여행하는 비용: {total_cost}")