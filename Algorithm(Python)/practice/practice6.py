array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 선택 정렬
for i in range(len(array)):
    min_idx = i
    for j in range(i, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)

# 삽입 정렬
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
print(array)


# 퀵 정렬
def quick_sort(array, start, end):
    if start > end:
        return
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


# 퀵 정렬
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

# 계수 정렬
count = [0] * (max(array) + 1)

for a in array:
    count[a] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end=' ')


import heapq

array = [1, 3, 5, 7, 9, 0, 2, 4, 8, 6]

# 최소 힙 정렬
def min_heap(array):
    q = []
    for a in array:
        heapq.heappush(q, a)

    result = []
    for _ in range(len(array)):
        result.append(heapq.heappop(q))
    return result

res = min_heap(array)
print(res)


def max_heap(array):
    q = []
    for a in array:
        heapq.heappush(q, -a)
    result = []
    for _ in range(len(array)):
        result.append(-heapq.heappop(q))
    return result

res = max_heap(array)
print(res)



