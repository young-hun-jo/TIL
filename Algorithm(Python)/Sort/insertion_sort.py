#=============================
# 2. Insertion Sort(삽입정렬)
# - 첫 데이터는 정렬되었다고 가정 하고
# - 두번째 데이터부터 하나씩 확인해보면서 왼쪽 데이터보다 작다면 왼쪽으로 계속 이동
#=============================
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    # step=-1로 해서 왼쪽 데이터랑 계속 비교
    for j in range(i, 0, -1):
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
print(array)
