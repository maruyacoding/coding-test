import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split(' '))
d = deque([i for i in range(1, n + 1)]) # 1부터 N까지의 원소 삽입
targets = list(map(int, input().split(' '))) # 뽑아낼 원소 목록
cnt = 0

for target in targets :
    index = d.index(target) # deque에서 해당 원소의 위치 찾기
    if index <= len(d) // 2 : # 왼쪽으로 돌리는 것이 더 빠른 경우
        for i in range(index) : # 회전 연산 반복 수행
            x = d.popleft()
            d.append(x)
            cnt += 1
    else : # 오른쪽으로 돌리는 것이 더 빠른 경우
        for i in range(len(d) - index) : # 회전 연산 반복 수행
            x = d.pop()
            d.appendleft(x)
            cnt += 1
    d.popleft() # 원소 꺼내기
    
print(cnt)


# 다른 사람 코드
n, m = map(int, input().split(' '))
dq = [i for i in range(1, n + 1)]

ans = 0

for find in map(int, input().split(' ')) :
    ix = dq.index(find)
    ans += min(len(dq[ix : ]), len(dq[: ix]))
    dq = dq[ix + 1 :] + dq[: ix]

print(ans)
