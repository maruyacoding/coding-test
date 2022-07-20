def solution(a, b):
    answer = 0
    if a == b :
        answer += a
    elif a < b :
        for i in range(a, b+1) :
            answer += i
    elif a > b :
        for i in range(b, a+1) :
            answer += i
    return answer


# 다른 사람 코드

def solution(a, b) :
    if a > b : 
        a, b = b, a
    
    return sum(range(a, b+1))