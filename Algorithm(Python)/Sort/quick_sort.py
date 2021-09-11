#=============================
# 3. Quick Sort(퀵 정렬)
# pivot 을 활용하기
# 2가지 방법으로 구현
# 시간복잡도는 O(NlogN)
#=============================
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 3-1. while문
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # array의 왼쪽에서 pivot보다 큰 최초의 값 찾기
        while left <= end and array[left] < array[pivot]:
            left += 1
        # array의 오른쪽에서 pivot보다 작은 최초의 값 찾기
        while start < right and array[right] > array[pivot]:
            right -= 1
        # 서로 이동하다가 왼쪽, 오른쪽 인덱스가 엇갈릴 경우 pivot과 right(pivot보다 작은값) 교체
        if right < left:
            array[pivot], array[right] = array[right], array[pivot]
        # 왼쪽, 오른쪽 인덱스 엇갈리지 않을 경우 left, right 교체
        else:
            array[left], array[right] = array[right], array[left]
    # 위 로직을 구현하는데, 왼쪽, 오른쪽 인덱스가 엇갈린 경우에 해당하는 위치에서 분할 후 각 퀵 정렬 적용
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)
#==================================================================
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 3-2. Pythonic 방법
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


res = quick_sort(array)
print(res)
