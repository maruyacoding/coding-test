def solution(n, arr1, arr2):
    answer = []

    for i in range(n) :
        tmp = bin(arr1[i] | arr2[i])
        tmp = tmp[2:].zfill(n)
        tmp = tmp.replace('1', '#').replace('0', ' ')
        answer.append(tmp)
        
    return answer

def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2) :
        a12 = str(bin(i|j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)

    return answer

# zfill(width) : width 자리수를 만족하도록 앞에 0을 붙여줌
# rjust(width, [fillchar]) : widtj 자리수를 만족하도록 앞에 [fillchar]을 붙여줌
# e.g. bin( 0b1010 | 0b100101) == '0b101111'
