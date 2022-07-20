def solution(n, m):
    answer = []
    n_div = [i for i in range(1, n + 1) if n % i == 0]
    m_div = [i for i in range(1, m + 1) if m % i == 0]
    answer.append(max(set(n_div) & set(m_div)))
    
    if answer[0] == 1 :
        answer.append(n * m)
    else :
        # e.g. 4, 6의 공배수는 4 * 6 안에는 반드시 존재할 것
        n_div2 = [n * i for i in range(1, m + 1)]
        m_div2 = [m * i for i in range(1, n + 1)]
        answer.append(min(set(n_div2) & set(m_div2)))
        
    return answer

# 다른 사람 코드
def solution(n, m) :
    a, b = max(n, m), min(n, m)
    t = 1
    while t > 0 :
        t = a % b
        a, b = b, t
    answer = [a, int(n * m / a)]
    return answer
# 최대공약수와 최소공배수 관계 : 유클리드 호제법
