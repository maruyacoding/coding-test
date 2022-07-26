import sys
input = sys.stdin.readline

n = int(input())
stack, answer, current = [], [], 1

for _ in range(n) :
    x = int(input())
    # top()보다 x가 더 크다면 스택에 삽입
    while len(stack) == 0 or stack[-1] < x :
        stack.append(current)
        current += 1
        answer.append('+')
    # top()과 x가 같다면 스택에서 제거
    if stack[-1] == x :
        stack.pop()
        answer.append('-')
    # top()보다 x가 더 작다면 불가능
    else :
        answer = ['NO']
        break
        
for x in answer :
    print(x)
