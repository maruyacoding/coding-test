def solution(participant, completion):
    dic = {}
    
    for i in participant :
        if i in dic.keys() :
            dic[i] += 1
        else :
            dic[i] = 1
            
    for j in completion :
        if j in dic.keys() :
            dic[j] -= 1
    
    for k in dic :
        if dic[k] != 0 :
            return k