def solution(n):
    answer = []
    n -= 1
    for i in range(2, n + 1) :
        if n % i == 0 :
            answer.append(i)
    return min(answer)