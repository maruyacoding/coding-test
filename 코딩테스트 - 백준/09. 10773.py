import sys
input = sys.stdin.readline 

n = int(input())
stack = []

for _ in range(n) :
    data = int(input())
    if data != 0 :
        stack.append(data)
    elif data == 0 :
        stack.pop()
print(sum(stack))
