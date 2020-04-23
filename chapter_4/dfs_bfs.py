# class Node:
#
#     def __init__(self, *args, **kwargs):
#         self.node = node
from queue import Queue

dic = {
    0: (1,),
    1: (2,),
    2: (0, 3),
    3: (2, 4),
    4: (6,),
    5: (4,),
    6: (5,),
}


class Node:
    def __init__(self, node=None):
        self.node = node
        self.visited = False
        self.adj = list()


def dfs(root):
    print(root.node)  # visit
    root.visited = True
    for n in root.adj:
        if n.visited is False:
            dfs(n)


def bfs(root):
    q = Queue()
    root.visited = True
    q.put(root)
    while not q.empty():
        r = q.get()
        print(r.node)  # visit
        for i in r.adj:
            if i.visited is False:
                i.visited = True
                q.put(i)


node_li = list()
for k in dic.keys():
    node = Node(k)
    node_li.append(node)

for k, v in dic.items():
    for i in v:
        node_li[k].adj.append(node_li[i])

print('--------')
print("dfs")
# dfs(node_li[0])
print('--------')
print("bfs")
bfs(node_li[0])

li = [
    (1,),
    (2,),
    (0, 3),
    (2, 4),
    (6,),
    (4,),
    (5,),
]
visited = [False for _ in range(len(li))]


def dfs2(v):
    print(v)  # visit
    visited[v] = True
    for z in li[v]:
        if visited[z] is False:
            dfs2(z)


# dfs2(0)
def bfs2(graph, root):
    visited = list()  # 방문한 곳을 기록
    q = Queue()  # 큐에 시작점을 줄세움
    q.put(root)
    while not q.empty():  # queue 가 빌 때 까지 탐색을 계속
        vertex = q.get()  # 큐의 맨 앞의 원소를 방문할 꼭짓점으로 설정
        if vertex not in visited:  # 꼭짓점이 방문된 적이 없다면 방문 기록에 추가
            visited.append(vertex)  # visit
            for node in graph[vertex]:  # 꼭짓점에 연결된 노드들 중
                if node not in visited:  # 방문 안 된 곳 만을
                    q.put(node)  # 큐에 줄세움

    return visited


korea = {'세종': ['서울', '강릉', '대구', '광주'],
         '서울': ['평양', '인천', '세종'],
         '강릉': ['독도', '세종'],
         '광주': ['세종', '여수'],
         '대구': ['세종', '울산'],
         '평양': ['서울'],
         '인천': ['서울'],
         '독도': ['강릉'],
         '여수': ['광주', '부산'],
         '울산': ['대구', '부산'],
         '부산': ['여수', '울산'],
         }

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
print(bfs2(graph, 'A'))
