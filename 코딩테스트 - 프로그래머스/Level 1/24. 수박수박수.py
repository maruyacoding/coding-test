def solution(n):
    answer = ''
    for index in range(n) :
        if index % 2 == 0 :
            answer = answer + '수'
        else :
            answer = answer + '박'
    return answer

# 다른 사람 코드
def solution(n) :
    s = '수박' * n
    return s[:n]