def solution(price, money, count):
    result, cnt = 0, 0 
    for i in range(1, count + 1) :
        cnt += i
    total = price * cnt
    result = total - money
    if total <= money :
        return 0
    return result

# 다른 사람 코드
def solution(price, money, count) :
    # 등차수열의 특성 활용!
    return max(0, price * (count + 1) * count // 2 - money)

# 다른 사람 코드 2
def solution(price, money, count) :
    return abs(min(money - sum([price * i for i in range(1, count + 1)], 0)))