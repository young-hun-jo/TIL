#=============================
# 2. BFS -> 큐 자료구조 사용(deque)
# 단, BFS 시간 복잡도는 O(N) 이며 재귀함수를 사용하는 DFS 보다는 수행시간 보통 빠름
#=============================

from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * len(graph)

def bfs(graph, v, visited):
    # 첫 노드 큐에 삽입 및 방문 처리
    queue = deque([v])
    visited[v] = True
    # 큐를 pop 하면서 빈 큐가 될 때까지 반복
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        # 꺼낸 노드의 인접한 노드들 확인
        for i in graph[node]:
            # 인접 노드가 방문하지 않았다면 방문처리 및 인접 노드 큐에 넣기
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(graph, 1, visited)
