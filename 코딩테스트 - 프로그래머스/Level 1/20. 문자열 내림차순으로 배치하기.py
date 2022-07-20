def solution(s):
    answer = [ord(i) for i in s]
    answer.sort(reverse = True)
    answer = [chr(i) for i in answer]
    result = ''
    for i in answer :
        result += i
    return result


# 다른 사람 코드

def solution(s):
    return ''.join(sorted(s, reverse=True))
    
# 문자열도 정렬됨!
# join() : 리스트의 문자열을 합치는 역할을 한다.