# 다익스트라 알고리즘 -> 특정 노드에서 다른 노드로 가는 최단경로
# O(NlogN), 방문하지 않은 노드이면서 시작노드와 가장 가까운 노드를 우선순위 큐가 자동 정렬해줌!
import heapq

v, e = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
distance = [INF] * (v+1)

def dijkstra(start):
    # 시작노드 처리
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

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print('X')
    else:
        print(distance[i])


# 플로이드 워셜 알고리즘 -> 모든 노드에서 다른 모든 노드까지의 최단거리
# 시간복잡도 O(V^3), 거리테이블을 2차원 리스트로 정의
v, e = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (v+1) for _ in range(v+1)]
# 자신의 경로는 0으로
for a in range(1, v+1):
    for b in range(1, v+1):
        if a == b:
            graph[a][b] = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

# 거쳐가는 노드 k
for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 서로소 집합 자료구조 -> 사이클 판별
# find연산 후 부모노드가 같으면 사이클 발생! 다르면 union연산
v, e = map(int, input().split())
# 부모테이블
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

cycle = False
for _ in range(e):
    a, b = map(int, input().split()) # union연산할 정보 주어짐
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클 발생')
else:
    print('X')

# 크루스칼 알고리즘 -> 최소신장트리 만드는 데 드는 비용 구하는 알고리즘
# 간선 정보를 받는데, 비용을 오름차순으로 정렬후 하나씩 확인하면서
# 부모노드가 다르면 사이클ㄹ 발생X->union연산후 최소신장에 포함 같으면 무시
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
result = 0
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

for i in range(e):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(result)

# 소수 판별 함수
import math

def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

# m이상 n이하의 값 중 소수인 값들 출력
def find_prime_numbers_range(n, m):
    if n == 0 or n == 1:
        return None
    array = [True] * (n+1)
    array[0], array[1] = False, False
    for i in range(2, int(math.sqrt(n))+1):
        if array[i]:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1
    for i in range(m, n+1):
        if array[i]:
            print(i, end=' ')

# 특정한 합을 갖는 부분 연속 수열 찾는 알고리즘 -> 투 포인터 활용
N = 5  # 주어진 수열 길이
M = 5  # 찾고자하는 부분 합
data = [1, 2, 3, 2, 5]

interval_sum = 0  # 실시간으로 계산할 구간 합
end = 0   # end index
count = 0

for start in range(N):
    # 조건 만족할 때까지 end 인덱스 늘리기
    while end < N and interval_sum < M:
        interval_sum += data[end]
        end += 1
    if interval_sum == M:
        count += 1
    # start 인덱스 옮기기
    interval_sum -= data[start]

print(count)

# 투 포인터를 활용해서 두 정렬된 리스트 합집합 정렬
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 7]

# a, b 인덱스
i, j = 0, 0
result = [0] * (n+m)
k = 0 # result 인덱스

while i < n or j < m:
    # b리스트를 다 돌았거나 a[i] < b[j] -> a[i]를 모두 담고 i+1
    if j >= m or (i < n and a[i] < b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

print(result)

# 구한 합
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합
prefix = [0]
sum_value = 0

for d in data:
    sum_value += d
    prefix.append(sum_value)

# [left, right] 쿼리 주어지면
left, right = 2, 4
res = prefix[right] - prefix[left-1]
print(res)

# 2차원 리스트 시계방향으로 90도 회전하는 함수 -> 직각,정강 행렬 모두 가능
def rotate_a_by_degree_90(a):
    n = len(a)  # 행
    m = len(a[0]) # 열
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

a = [[1,2,3],
     [7,8,9]]

res = rotate_a_by_degree_90(a)
print(res)
