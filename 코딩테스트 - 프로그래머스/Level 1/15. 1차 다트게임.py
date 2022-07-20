def solution(dartResult):
    num = ''
    result = []
    for i in dartResult :
        if i.isnumeric() :
            num += i
        elif i == 'S' :
            result.append(int(num) ** 1)
            num = ''
        elif i == 'D' :
            result.append(int(num) ** 2)
            num = ''
        elif i == 'T' :
            result.append(int(num) ** 3)
            num = ''
        elif i == '*' :
            if len(result) == 1 :
                result[0] = result[0] * 2
            else :
                result[-1] = result[-1] * 2
                result[-2] = result[-2] * 2
        elif i == '#' :
            result[-1] = result[-1] * (-1)

    return sum(result)

# isdigit() : 해당 문자열이 '숫자'로 이루어져 있는지 검사한다.
# isdecimal() : 해당 문자열이 0~9까지의 수로 이루어진 것인지 검사한다. 즉 바로 int로 변환할 수 있는 수인지 검사
# isnumeric() : '수로 볼 수 있는 것' 인경우 True를 반환


# 다른 사람 코드

import re

def solution(dartResult) :
    bonus = {'S' : 1, 'D': 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)) :
        if dart[i][2] == '*' and i > 0 :
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    
    answer = sum(dart)
    return answer

# 다른 사람 코드2

def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10', 'k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point :
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*' :
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#' :
            answer[i] = answer[i] * (-1)
        else :
            answer.append(int(j))
            i += 1
    return sum(answer)