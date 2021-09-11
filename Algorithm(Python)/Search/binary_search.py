#===================================
# 2.이진 탐색(Binary Search)
# 단, 데이터가 정렬된 후에 사용 가능!
# 배열의 시작, 중간, 끝 인덱스를 활용해 탐색
# 이상적으로는 연산 횟수를 매번 줄어들게 하므로 시간복잡도 O(logN)
# 입력 데이터가 10,000,000(천만) 이상 또는 탐색 범위가 1,000억 이상일 때 자주 사용
# while문, 재귀함수 구현 2가지 방법
#===================================

array = [x for x in range(20, 40, 2)]

# 2-1. 재귀함수 사용
def binary_search(array, target, start, end):
    if start > end:
        return None
    middle = (start + end) // 2
    if target == array[middle]:
        return middle
    elif target < array[middle]:
        return binary_search(array, target, start, middle-1)
    else:
        return binary_search(array, target, middle+1, end)


res = binary_search(array, 26, 0, len(array)-1)
print(res)


# 2-2. while 문 사용
def binary_search_while(array, target, start, end):
    if start > end:
        return None
    while start <= end:
        middle = (start + end) // 2
        if array[middle] == target:
            return middle
        elif target < array[middle]:
            end = middle - 1
        else:
            start = middle + 1


res2 = binary_search_while(array, 26, 0, len(array)-1)
print(res2)
