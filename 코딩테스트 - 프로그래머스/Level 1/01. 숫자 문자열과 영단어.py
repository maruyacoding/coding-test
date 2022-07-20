def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    # enumerate : 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
    for idx,num in enumerate(eng) :
        if num in s :
            s = s.replace(num, str(idx))
    return int(s)