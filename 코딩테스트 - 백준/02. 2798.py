n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result, count = 0, 0
for i in range(0, len(data)) :
    for j in range(i + 1, len(data)) :
        for k in range(j + 1, len(data)) :
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m :
                result = max(result, sum_value)
print(result)

# 다른 사람 코드
from itertools import *

n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

print(max(x for x in map(sum, combinations(data, 3)) if x <= m))
