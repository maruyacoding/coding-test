def solution(s):
    if len(s) % 2 == 0 :
        return s[len(s)//2 - 1 : len(s)//2 + 1]
    else :
        return s[len(s)//2]
    return answer

# 다른 사람 코드

def solution(s) :
    return str[(len(s) - 1)//2 : len(s)//2 + 1]