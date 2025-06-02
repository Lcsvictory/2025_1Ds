class Graph:
    def __init__ (self, size):
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)] # 각 노드의 부모는 자기자신으로 초기화한다.

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    '''
    오름차순 정렬된 edges
    [[10, 0, 1], [10, 1, 0], [11, 1, 3], [11, 3, 1], [12, 2, 3], [12, 3, 2], [15, 0, 2], [15, 2, 0], [20, 3, 4], [20, 4, 3], [28, 4, 5], [28, 5, 4], [30, 3, 5], [30, 5, 3], [40, 1, 2], [40, 2, 1], [55, 1, 4], [55, 4, 1]]
    비용이 가장 적은 순으로 정렬해뒀으니 우선 연결하고, 이미 연결되어있으면 연결할 필요가 없다. 간선의 수는 vertex - 1이라는 공식이 있는데 자연스럽게 공식을 따르게 된다.
    0,1 합치면 1의 부모는 0이됨.
    3,1 합치면 1부모 0, 3부모 3 서로 다르니 3의 부모는 0이됨 현재 : 0의 자식 1, 3
    3,2 합치면 3부모 0, 2부모 2 서로 다르니 3의 부모는 0이됨 현재 : 0의 자식 1, 3, 2
    2,0 합치면 2부모 0, 0부모 0 서로 같으니 이미 최소 비용의 간선이 존재하게됨. 따라서 최소비용트리에 추가하지 않음.
    3,4 합치면 3부모 0, 4부모 4 서로 다르니 4의 부모는 0이됨 현재 : 0의 자식 1, 3, 2, 4
    4,5 합치면 4부모 0, 5부모 5 서로 다르니 5의 부모는 0이됨 현재 : 0의 자식 1, 3, 2, 4, 5
    3,5 합치면 3부모 0, 5부모 0 서로 같으니 추가하지 않음
    1,2 합치면 1부모 0, 2부모 0 서로 같으니...
    1,4 합치면 1부모 0, 4부모 0 서로 같...
    '''

    def merge(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[y_root] = x_root
            return True
        return False

def print_graph(g) :
    print('   ', end = ' ')
    for v in range(len(g.graph)) :
        print(cities[v], end =' ')
    print()
    for row in range(len(g.graph)) :
        print(cities[row], end =' ')
        for col in range(len(g.graph)) :
            print(f"{g.graph[row][col]:3d}", end=' ')
        print()
    print()



g1 = None
cities = ['인천', '서울', '강릉', '대전', '광주', '부산']
incheon, seoul, gangneung, daejeon, gwangju, busan = 0, 1, 2, 3, 4, 5


graph_size = 6
g1 = Graph(graph_size)
g1.graph[incheon][seoul] = 10; g1.graph[incheon][gangneung] = 15
g1.graph[seoul][incheon] = 10; g1.graph[seoul][gangneung] = 40; g1.graph[seoul][daejeon] = 11; g1.graph[seoul][gwangju] = 55
g1.graph[gangneung][incheon] = 15; g1.graph[gangneung][seoul] = 40; g1.graph[gangneung][daejeon] = 12
g1.graph[daejeon][seoul] = 11; g1.graph[daejeon][gangneung] = 12; g1.graph[daejeon][gwangju] = 20; g1.graph[daejeon][busan] = 30
g1.graph[gwangju][seoul] = 55; g1.graph[gwangju][daejeon] = 20; g1.graph[gwangju][busan] = 28
g1.graph[busan][daejeon] = 30; g1.graph[busan][gwangju] = 28

print('도시 간 도로 건설을 위한 전체 연결도')
print_graph(g1)

# 간선을 만들자
edges = list()
for i in range(graph_size) :
    for j in range(graph_size) :
        if g1.graph[i][j] != 0 :
            edges.append([g1.graph[i][j], i, j])
print(edges)

# 간선을 오름차순 정렬하자
edges.sort(key=lambda x: x[0]) # 오름차순 정렬
print(edges)

# 서로소 집합을 만들자
dj = DisjointSet(graph_size)
mst_edges = list() # 최소신장트리
mst_cost = 0 # 최소비용

# 최소신장트리를 구현하자
for cost, s, e in edges:
    if dj.merge(s, e):
        mst_edges.append((cost, s, e))
        mst_cost += cost
print(mst_edges)

mst_graph = Graph(graph_size)
for c, s, e in mst_edges:
    mst_graph.graph[s][e] = c
    mst_graph.graph[e][s] = c


print_graph(mst_graph)
print(f"최소 비용 : {mst_cost}")

print("\nedges list")
for c, s, e in mst_edges:
    print(f"{cities[s]} --- {cities[e]} : {c}")
