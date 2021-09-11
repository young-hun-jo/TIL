#===================================
# 1.순차=선형 탐색(Sequential=Linear Search)
# 보통 정렬되지 않고 무작위로 주어진 경우 사용
# 배열 내에 특정 원소 존재 여부를 체크한다거나 특정 원소개수를 셀 때 사용
# Python 문법의 count('value') 같은 메소드
# 시간복잡도는 최악의 경우 O(N)
#===================================

def linear_search(n, array, target):
    for i in range(n):
        if array[i] == target:
            return i+1

array = [i for i in range(10, 30, 2)]

res = linear_search(len(array), array, 14)
print(res)
