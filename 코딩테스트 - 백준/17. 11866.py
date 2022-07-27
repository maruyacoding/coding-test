import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split(' '))
dq = deque([i for i in range(1, n + 1)])
ans = []


for i in range(n) :
    for i in range(k - 1) :
        x = dq.popleft()
        dq.append(x)
    x = dq.popleft()
    ans.append(x)

print('<', end='')
for i in range(len(ans)) :
    if i < len(ans) - 1 :
        print(ans[i], end= ', ')
    else :
        print(ans[i], end='')
print('>')
