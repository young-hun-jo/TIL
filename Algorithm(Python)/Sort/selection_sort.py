#=============================
# 1. Selection Sort(선택정렬)
# - 단순 무식하게 가장 작은 요소를 찾고 위치로, 그다음 작은 요소를 찾고 위치로, ...(반복)
#=============================
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    # 갱신할 최소값 인덱스 변수
    min_idx = i
    for j in range(i+1, len(array)):
        # 최소값 인덱스 갱신
        if array[j] < array[min_idx]:
            min_idx = j
    # 최소값 인덱스 자리 스와핑
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)
