def solution(s):
    if s[0] == '-' :
        return int(s[1:]) * (-1)
    else :
        return int(s)

# 다른 사람 코드
# 정수형으로 변경 시 문자 +, -는 알아서 부호로 인식!
def solution(s):
    a = int(s)
    return a