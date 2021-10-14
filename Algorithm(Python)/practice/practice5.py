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
# 방문노드
visited = [False] * len(graph)

# DFS
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for next in graph[v]:
        if not visited[next]:
            dfs(graph, next, visited)

dfs(graph, 1, visited)

# BFS
from collections import deque

def bfs(graph, v, visited):
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

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 선택 정렬 ->  시간복잡도 O(N^2)
for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j
    # swap
    array[min_idx], array[i] = array[i], array[min_idx]

print(array)

# 삽입 정렬 -> 시간복잡도 O(N^2)
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j-1], array[j] = array[j], array[j-1]

print(array)

# 퀵 정렬 -> 시간 복잡도: N(NlogN)
def quick_sort(array, start ,end):
    if start > end:
        return None
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while start < right and array[pivot] < array[right]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

result = quick_sort(array)
print(result)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 3, 2, 5, 7, 4, 1]
# 계수 정렬 -> 시간 복잡도: O(N+K) K는 주어진 데이터의 최댓값
count = [0] * (max(array) + 1)
for a in array:
    count[a] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end=' ')

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 최소 힙 정렬 -> 시간 복잡도 (NlogN)
import heapq

def min_heap_sort(array):
    q = []
    result = []
    for a in array:
        heapq.heappush(q, a)
    for _ in range(len(array)):
        result.append(heapq.heappop(q))
    return result

def max_heap_sort(array):
    q = []
    result = []
    for a in array:
        heapq.heappush(q, -a)
    for _ in range(len(array)):
        result.append(-heapq.heappop(q))
    return result

min_sort = min_heap_sort(array)
max_sort = max_heap_sort(array)
print(min_sort)
print(max_sort)

# 선형 탐색 -> 시간 복잡도 O(N)
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i+1

# 이진 탐색 -> 시간 복잡도 O(logN) 단, 데이터가 미리 정렬되어 있어야 함!
array.sort()

def binary_search(array, target, start, end):
    if start > end:
        return '찾는 값 없음'
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)

def binary_search(array, target, start, end):
    if start > end:
        return None
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

res = binary_search(array, 0, 0, len(array)-1)
print(res)

# 이진 탐색을 활용한 특정 원소 개수 구하는 방법! -> 단, 주어진 데이터를 정렬시키고 사용해야 함!
from bisect import bisect_left, bisect_right

array.sort()

def count_by_range(array, left_val, right_val):
    left_idx = bisect_left(array, left_val)
    right_idx = bisect_right(array, right_val)
    return right_idx - left_idx

res = count_by_range(array, 4, 4)
print(res)

# DP -> 탑 다운 방식(재귀함수)

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


d = [0] * 11
d[1] = 1
d[2] = 1
for i in range(3, 11):
    d[i] = d[i-1] + d[i-2]

print(d)

# 다익스트라 알고리즘 -> 특정 노드에서 다른 노드들까지의 최단 거리 경로 -> 시간 복잡도 O(ElogV)
# (logV인 이유는 시작노드와 가장 가까운 노드를 찾는 것은 우선순위 큐를 이용하기 때문이고 E는 해당 노드와 연결된 간선들을 하나하나 탐색하므로 모든 간선의 개수 E
import heapq

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
INF = int(1e9)
distance = [INF] * (v+1)
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def dijkstra(start):
    distance[start] = 0
    q = []
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


# 플로이드 워셜 -> 모든 노드에서 모든 노드까지의 최단 경로 -> 시간 복잡도 O(V^3)
v, e = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

# 자기 자신으로 가는 비용은 0
for a in range(1, v + 1):
    for b in range(1, v + 1):
        if a == b:
            graph[a][b] = 0

# k = 거쳐가는 노드
for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, v + 1):
    for b in range(1, v + 1):
        print(graph[a][b], end=' ')
    print()

# 서로소 집합 자료구조 알고리즘 -> 어떤 것을 집합으로 할 것인지를 알아내는 것이 포인트!
v, e = map(int, input().split())
parent = [0] * (v + 1)
# 부모 테이블 초기화
for i in range(1, v + 1):
    parent[i] = i


# find, union
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(e):
    # union 연산 정보
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소의 루트 노드 확인하기 위해 union 연산 처리한 후에서 find 연산 수행!
for i in range(1, v + 1):
    root = find_parent(parent, i)
    print(root, end=' ')


# 무방향에서 싸이클 판별 -> 부모노드가 같으면 사이클 발생!
cycle = False
for _ in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

# 크루스칼 알고리즘 -> 최소 신장 트리 만드는 데 드는 비용 계산하는 알고리즘!
v, e = map(int, input().split())
parent = [0] * (v + 1)
# 부모 테이블 초기화
for i in range(1, v + 1):
    parent[i] = i


# find, union
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선 비용 오름차순 정렬 후 하나씩 확인 -> 각 부모노드가 다르면 사이클 발생X->union연산처리 및 최소 신장 트리에 포함
edges.sort()
result = 0
for i in range(e):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(result)

# 특정 수 소수 판별하는 알고리즘
import math

def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

# m 이상 n 이하의 범위에서 소수인 값들 출력하는 알고리즘
def is_prime_number_range(n, m):
    array = [True] * (n+1)
    for i in range(2, int(math.sqrt(n))+1):
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
    for i in range(m, n+1):
        if i == 0 or i == 1:
            array[i] = False
        if array[i]:
            print(i, end=' ')

is_prime_number_range(10, 0)

# 특정한 합을 갖는 부분 연속 수열 찾는 알고리즘 -> 투 포인터 활용
N = 5  # 주어진 수열 길이
M = 5  # 찾고자하는 부분 합
data = [1, 2, 3, 2, 5]

# 시작을 기준으로 끝을 조건 만족할 때까지 계속 증가시키기
inter_sum = 0
end = 0
count = 0
for start in range(N):
    while end < N and inter_sum < M:
        inter_sum += data[end]
        end += 1
    if inter_sum == M:
        count += 1
    inter_sum -= data[start]

print(count)

# 투 포인터를 활용해 정렬된 두 리스트 합집합 후 정렬하는 알고리즘
# 단, 주어진 두 리스트는 정렬되어 있어야 함!
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 7]

# a, b의 각 인덱스
i, j = 0, 0
# 합한 후 정렬 결과 담을 리스트
result = [0] * (n+m)
k = 0  # result 인덱스

while i < n or j < m:
    # b 리스트 다 돌았거나 a < b일 경우 -> a의 원소들 모두 담기
    if j >= m or (i < n and a[i] < b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

print(result)

# 구간 합
a = [10, 20, 30, 40]

# 접두사 합
prefix = [0]
sum_val = 0
for i in a:
    sum_val += i
    prefix.append(sum_val)

# [left, right] 쿼리로 들어오면
left, right = 1, 3  # 1번째부터 3번째 구간 합
print(prefix[right] - prefix[left-1])

# 2차원 리스트 시계방향으로 90도 회전하는 함수

def rotate_matrix_90(a):
    n = len(a)  # 행
    m = len(a[0]) # 열
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

a = [[1,2,3],
     [4,5,6]]

res = rotate_matrix_90(a)
print(res)

# 오른쪽, 왼쪽으로 그때그때 방향 갱신하는 로직
# ex) 시작 방향이 동쪽!

# 동 -> 남 -> 서 -> 북 (오른쪽 방향으로 회전)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = 0 # 동쪽

def turn_direction(direction, c='L'):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())  # a -> b
    graph[a].append(b)

# 방문 체크 테이블
visited = [0] * (v + 1)


def cycle_dfs(node):
    if visited[node]:
        if visited[node] == -1:
            return True
        return False

    visited[node] = -1
    for next in graph[node]:
        if cycle_dfs(next):
            return True

    visited[node] = 1
    return False
