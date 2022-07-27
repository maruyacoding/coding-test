import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
arr = list(map(int, input().split(' ')))
d = deque()

for i in range(n) :
    # (수, 번호) 형태로 원소를 삽입
    d.append((arr[i], i + 1))

result = []
result.append(1) # 맨 처음에는 1번 풍선 터뜨린다
current, index = d.popleft() # 원소 추출
for i in range(n - 1) : # 원소를 모두 꺼내기
    if current > 0 : 
        for j in range(current - 1) : # current - 1 번 왼쪽으로 돌리기 수행 
            d.append(d.popleft())
    else :
        for j in range(-current) :
            d.appendleft(d.pop())
    # 원소 추출
    current, index = d.popleft()
    result.append(index)
    
for x in result :
    print(x, end = ' ')
