def solution(arr, divisor):
    answer = []
    for num in arr :
        if num % divisor == 0 :
            answer.append(num)
    answer = sorted(answer)
    
    if len(answer) == 0 :
        return [-1]
    return answer


# 다른 사람 코드
def solution(arr, divisor) :
    return sorted([n for n in arr if n % divisor == 0]) or [-1]