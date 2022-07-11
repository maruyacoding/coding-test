from itertools import combinations as cb

def solution(numbers):
    answer = []
    comb = list(cb(numbers, 2))
    for i in comb :
        i = sum(list(i))
        answer.append(i)
    answer = sorted(set(answer))
    
    return answer

# 다른 사람 코드
def solution(numbers) :
    answer = []
    for i in range(len(numbers)) :
        for j in range(i + 1, len(numbers)) :
            answer.append(numbers[i] + numbers[j])
    
    return sorted(list(set(answer)))