def solution(n):
    answer = ''
    num = sorted([i for i in str(n)], reverse = True)
    for i in num :
        answer += i
    return int(answer)

# 다른 사람 코드
def solution(n) :
    ls = list(str(n))
    ls.sort(reverse = True)
    return int(''.join(ls))

