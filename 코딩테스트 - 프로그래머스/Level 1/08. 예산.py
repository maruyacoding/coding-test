def solution(d, budget) :
    d.sort()
    total = 0
    for i in range(len(d)) :
        if d[i] <= budget :
            total += 1
            budget -= d[i]
        else :
            break
    return total