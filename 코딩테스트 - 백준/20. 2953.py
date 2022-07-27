import sys
input = sys.stdin.readline

scores = []
for _ in range(5) :
    scores.append(list(map(int, input().split(' '))))

for i in range(len(scores)) :
    scores[i] = sum(scores[i])

print(scores.index(max(scores)) + 1, max(scores))

# 강의 코드
result = 0
max_value = 0
for i in range(5) :
    row = list(map(int,input().split(' ')))
    summary = sum(row)
    if max_value < summary :
        max_value = summary
        result = i + 1

print(result, max_value)
