# 최단 경로 -> 개선된 다익스트라 알고리즘 -> 특정 노드에서 다른 노드들까지 최단 거리 -> O(ElogV)
import heapq

v, e = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a, b, cost = map(int, input().split()) # a->b, cost
    graph[a].append((b, cost))

def dijkstra(start):
    # 시작 노드 처리
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
for i in range(1, v+1):
    if distance[i] == INF:
        print('X')
    else:
        print(distance[i])

# 플로이드 워셜 알고리즘 -> 모든 노드에서 모든까지의 거리 -> 시간 복잡도 V^3
v, e = map(int, input().split())
INF = int(1e9)
distance = [[INF] * (v+1) for _ in range(v+1)]

for a in range(1, v+1):
    for b in range(1, v+1):
        if a == b:
            distance[a][b] = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    distance[a][b] = cost

# k = 거쳐가는 노드
for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            distance[a][b] = min(distance[a][b], distance[a][k]+distance[k][b])

for a in range(1, v+1):
    for b in range(1, v+1):
        print(distance[a][b], end=' ')
    print()

# 서로소 집합 자료구조 알고리즘
v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i


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


# 들어오는 간선 정보에 대해 union 연산 수행
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소에 대해 find 연산해서 루트노드 찾기
for i in range(1, v + 1):
    root = find_parent(parent, i)
    print(root, end=' ')

for i in range(1, v + 1):
    print(parent[i], end=' ')

# 서로소 집합 자료구조 알고리즘
v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i


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

cycle = False
# 부모노드 같으면 사이클 발생!
for _ in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클 발생')
else:
    print('사이클 발생 X')

# 최소신장 트리 찾는 크루스칼 알고리즘 -> 간선 정보를 오름차순 정렬
# -> 하나씩 확인 -> find연산 수행 -> 부모노드 같지 X -> union연산 -> 최소신장 트리 비용에 포함
# -> 부모노드 같으면 무시

v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

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
total_cost = 0
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

for i in range(e):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)

from collections import deque

# 위상 정렬(선후관계 고려)-> 진입차수 활용 -> 진칩차수 0인 노드 큐에 넣고 뺀다음 그 노드와 연결된 간선 제거(진입차수 -1)
v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split()) # a->b
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    q = deque()
    result = []
    # 초기 진입차수가 0인 노드 넣기 위해 선형탐색
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        result.append(node)
        for next in graph[node]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    for r in result:
        print(r, end=' ')

topology_sort()

# 특정 수가 소수인지 판별하는 알고리즘
import math

def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

res = is_prime_number(1)
print(res)

# 에라토스테네스의 체 -> 주어진 범위에서 다수의 소수 판별
# m이상 n이하의 소수들 출력
import math

def find_prime_number_range(n, m):
    if (n < m) or (n == 0 or n == 1) or (m == 0 or m ==1):
        return False
    array = [True] * (n+1)
    for i in range(2, int(math.sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1

    for i in range(m, n+1):
        if array[i]:
            print(i, end=' ')

find_prime_number_range(10, 5)

# 투 포인터를 활용한 특정한 합을 갖는 부분 연속 수열 찾기
n, m = 5, 5
data = [1, 2, 3, 2, 5]

interval_sum = 0
end = 0
count = 0

for start in range(n):
    # 조건 만족할 때까지 end 조정
    while end < n and interval_sum < m:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    # start 조정
    interval_sum -= data[start]

print(count)

# 정렬된 두 리스트 합집합 후 정렬하는 알고리즘 -> 결과리스트에 a, b 원소중 a < b -> a를 넣고 a의 i+1
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 7]

i, j = 0, 0
result = [0] * (n+m)
k = 0

while i < n or j < m:
    # b 리스트 모두 탐색했거나 a원소가 작을때는 a원소를 모두 결과리스트에 집어넣기
    if j >= m or (i < n and a[i] < b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

print(result)

# 구간 합. 특정 구간의 모든 수를 합해서 출력 -> 접두사 합 이용
data = [10, 20, 30, 40, 50]

prefix = [0]
sum_value = 0
for d in data:
    sum_value += d
    prefix.append(sum_value)
# 쿼리 주어짐
left, right = 2, 4

res = prefix[right] - prefix[left-1]
print(res)
