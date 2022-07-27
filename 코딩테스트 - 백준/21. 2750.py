# 선택 정렬 (O(n^2))
n = int(input())
array = []

for _ in range(n) :
    array.append(int(input()))

for i in range(n) :
    min_index = i
    for j in range(i + 1, n) :
        if array[min_index] > array[j] :
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]

for i in array :
    print(i)

# 기본 정렬 라이브러리 (O(nlogn))
n = int(input())
array = []

for _ in range(n) :
    array.append(int(input()))

array.sort()

for i in array :
    print(i)
