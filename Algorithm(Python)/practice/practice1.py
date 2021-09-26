# DFS -> 스택, 재귀함수 사용
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

def dfs(graph, v, visited):
    # 노드 방문처리
    visited[v] = True
    print(v, end=' ')
    # 노드의 인접노드를 재귀함수로 깊이 우선 탐색
    for next in graph[v]:
        # 방문하지 않았을 때 탐색
        if not visited[next]:
            dfs(graph, next, visited)

dfs(graph, 1, visited)

# BFS -> 큐 사용
def bfs(graph, v, visited):
    # 시작 노드 처리
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

bfs(graph, 1, visited)

# 선택 정렬
# 시간복잡도 O(N^2)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j
    # swap
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)

# 삽입 정렬
# 시간복잡도 O(N^2)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j-1], array[j] = array[j], array[j-1]

print(array)

# 1. while, 재귀함수 사용
def quick_sort(array, start, end):
    if start > end:
        return None
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] < array[pivot]:
            left += 1
        while start < right and array[pivot] < array[right]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    # 피벗 기준으로 분할해 각 퀵 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

# 2.Pythonic 방법
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

res = quick_sort(array)
print(res)

# 계수 정렬
# 시간복잡도: 데이터 최대값이 K이라 할 때, O(N+K)
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array) + 1)

for a in array:
    count[a] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

# 순차 탐색
# 시간복잡도 O(N)
array = [i for i in range(10, 30, 2)]

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i+1


# 이진 탐색 -> 데이터가 정렬되어 있는 경우
# 시간 복잡도 O(logN)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array.sort()


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid+1
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

res = binary_search(array, 0, 0, len(array)-1)
print(res)

def binary_search(array, target, start, end):
    if start > end:
        return None
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid+1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

res = binary_search(array, 0, 0, len(array)-1)
print(res)

from bisect import bisect_left, bisect_right

def change_by_range(array, left_val, right_val):
    left_idx = bisect_left(array, left_val)
    right_idx = bisect_right(array, right_val)
    return right_idx - left_idx


# DP
# 1. Top-Down 방식
d = [0] * 1001

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

fibo(10)
print(d[:11])

# 2. Botton-Up 방식
d = [0] * 101
d[1] = 1
d[2] = 1

for i in range(3, 101):
    d[i] = d[i-1] + d[i-2]

print(d[:11])

# 개선된 다익스트라 알고리즘
# 시간복잡도 O(ElogV)
import heapq

n, m = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('X')
    else:
        print(distance[i])
