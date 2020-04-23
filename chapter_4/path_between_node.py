"""
방향 그래프에서 노드간 경로가 존재하는지 확인하는 알고리즘
-> 사이클에 대비
"""
from queue import Queue


def between_node(node, start, end):
    visited = [False for _ in range(len(node))]

    q = Queue()
    q.put(node[start])  # 1,2
    n_idx = start  # 0
    while q.qsize() != 0:
        adj = q.get()  # (1,2)
        visited[n_idx] = True
        if visited[n_idx] == visited[end]:
            return True
        # visite
        for i in adj:
            if visited[i] is False:
                q.put(node[i])
                n_idx = i
    return False


li = [
    (1, 2),  # 0, True
    (2,),  # 1, True
    (0, 3),  # 2, True
    (2,),  # 3, True
    (6,),  # 4, False
    (4,),  # 5, False
    (5,),  # 6, False
]

print(between_node(li, 0, 4))
