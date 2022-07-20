def solution(s):
    s = str.lower(s)
    p_cnt, y_cnt = 0, 0
    for i in s :
        if i == 'p' :
            p_cnt += 1
        elif i == 'y' :
            y_cnt += 1
    if p_cnt == y_cnt :
        return True
    elif p_cnt == 0 and y_cnt == 0 :
        return True
    elif p_cnt != y_cnt :
        return False
    
# 다른 사람 코드
# count 활용!
def solution(s) :
    return s.lower().count('p') == s.lower().count('y')