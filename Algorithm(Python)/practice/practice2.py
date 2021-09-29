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
    visited[v] = True
    print(v, end=' ')
    for next in graph[v]:
        if not visited[next]:
            visited[next] = True
            dfs(graph, next, visited)

dfs(graph, 1, visited)


# BFS(간선 비용 모두 동일, 최솟값) -> 큐 사용
from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])
    while queue:
        node = queue.popleft()
        visited[node] = True
        print(node, end=' ')
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

bfs(graph, 1, visited)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 선택 정렬 -> 시간 복잡도 O(N^2)
for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j
    # swap
    array[i], array[min_idx] = array[min_idx], array[i]
print(array)

# 삽입 정렬 -> 시간 복잡도 O(N^2)
for i in range(1, len(array)):
    for j in range(i, 0, -1): # 왼쪽으로
        if array[j] < array[j-1]:
            array[j-1], array[j] = array[j], array[j-1]
print(array)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 퀵 정렬 -> 시간 복잡도 O(NlogN)
# 1. while, 재귀함수 활용
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
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

# 2. Pythonic
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

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 계수 정렬 -> 시간 복잡도 O(N + K) , K는 주어진 데이터의 최댓값
count = [0] * (max(array) + 1)
for a in array:
    count[a] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

# 순차 탐색 -> 시간 복잡도 O(N)
array = [9, 5, 3, 2, 10, 18, 23, 44]

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i+1
    return '찾으려는 값 없음'

res = linear_search(array, 12)
print(res)

# 이진 탐색 -> array가 정렬되어있을 경우에만 사용 가능!
# 1. 재귀함수 사용
def binary_search(array, target, start, end):
    if start > end:
        return '찾으려는 값 없음'
    mid = (start + end) // 2
    if array[mid] == target:
        return mid+1
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

array.sort()
res = binary_search(array, 2, 0, len(array)-1)
print(res)

# 2. while문 사용
def binary_search(array, target, start, end):
    if start > end:
        return '찾으려는 값 없음'
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid+1
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid-1
array.sort()
res = binary_search(array, 2, 0, len(array)-1)
print(res)

# 이진 탐색 특정 원소 개수 구하는 함수
from bisect import bisect_left, bisect_right

def change_by_range(array, left_val, right_val):
    left_idx = bisect_left(array, left_val)
    right_idx = bisect_right(array, right_val)
    return right_idx - left_idx

# DP
# 1. 재귀함수
d = [0] * 11
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

fibo(10)
print(d)

# 2. for loop
d = [0] * 11
d[1] = 1
d[2] = 1
for i in range(3, 11):
    d[i] = d[i-1] + d[i-2]

print(d)

# 최소 힙 정렬 -> 시간 복잡도 O(NlogN)
import heapq

def min_heap_sort(array):
    q = []
    result = []
    for a in array:
        heapq.heappush(q, a)
    for _ in range(len(array)):
        result.append(heapq.heappop(q))
    return result

array = [9, 5, 3, 2, 10, 18, 23, 44]

res = min_heap_sort(array)
print(res)

def max_heap_sort(array):
    q = []
    result = []
    for a in array:
        heapq.heappush(q, -a)
    for _ in range(len(array)):
        result.append(-heapq.heappop(q))
    return result

array = [9, 5, 3, 2, 10, 18, 23, 44]
res = max_heap_sort(array)
print(res)

# 개선된 다익스트라 알고리즘 -> 시간 복잡도 O(ElogV)
import heapq

n, m = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
distance = [INF] * (n+1)  # 거리 테이블 1차원으로 정의

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
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
for i in range(n+1):
    if distance[i] == INF:
        print('도달 X')
    else:
        print(distance[i])


# 플로이드 워셜 알고리즘 -> O(N^3)
# 거리 테이블을 노드 개수+1 사이즈의 2차원 리스트로 만듦
n, m = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
# 자기 자신으로 가는 길은 0으로 초기화
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# k = 거쳐가는 경로의 노드
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
