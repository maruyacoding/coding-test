def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isnumeric() :
        return True
    else :
         return False

# 다른 사람 코드
def solution(s):
    return s.isdigit() and len(s) in (4, 6)

# 다른 사람 코드 2
# try, except 활용!
# try : 실행 코드, except : 예외 처리 코드
# else : 예외 처리할 오류가 없을 때 실행되는 코드
# finally : 오류 발생 여부 상관 없이 무조건 실행되는 코드
# raise : 오류를 일부로 발생시키기

def solution(s) :
    try :
        int(s)
    except :
        return False
    return len(s) == 4 or len(s) == 6