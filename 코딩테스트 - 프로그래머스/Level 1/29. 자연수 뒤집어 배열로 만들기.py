def solution(n):
    answer = []
    for i in range(len(str(n)) - 1, -1, -1) :
        answer.append(int(str(n)[i]))
    return answer

# 다른 사람 코드
def solution(n) :
    return list(map(int, reversed(str(n)))) 

# 다른 사람 코드2
def solution(n):
    return [int(i) for i in str(n)][::-1]                 