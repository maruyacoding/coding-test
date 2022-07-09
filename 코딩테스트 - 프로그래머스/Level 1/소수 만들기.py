from itertools import combinations

def is_prime_number(num) : # 소수 판별 함수
    if num == 0 or num == 1 :
        return False
    else :
        for i in range(2, num) :
            if num % i == 0 :
                return False
    return True

def solution(nums) :
    answer = 0
    cmb = list(combinations(nums, 3))
    for arr in cmb :
        if is_prime_number(sum(arr)) :
            answer += 1
    return answer


# 다른 사람 코드

def solution(nums) :
    from itertools import combinations as cb
    answer=0

    for a in cb(nums, 3) :
        cand = sum(a)
        for j in range(2, cand) :
            if cand % j == 0 :
                break
        else :
            answer += 1

    return answer