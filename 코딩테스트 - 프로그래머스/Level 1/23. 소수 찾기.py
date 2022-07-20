# 시간 초과
def solution(n):
    count = 0
    for n in range(2, n+1) :
        for i in range(2, n) :
            if n % i == 0:
                break
        else :
            count += 1
    return count

# 다른 사람 코드
# 에라토스테네스의 체, 차집합 활용!
def solution(n) :
    num = set(range(2, n+1))

    for i in range(2, n+1) :
        if i in num : # 만약 i가 num 집합에 있다면
            num -= set(range(2*i, n+1, i)) # i의 배수는 num 집합에서 제외
    return len(num)
