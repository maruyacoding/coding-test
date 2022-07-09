def solution(array, commands) :
    answer = []
    for i in range(len(commands)) :
        arr = array[commands[i][0]-1 : commands[i][1]]
        arr.sort()
        answer.append(arr[commands[i][2] - 1])
        
    return answer

# 다른 사람 코드

def solution(array, commands) :
    answer = []
    for command in commands :
        i, j, k = command
        answer.append(list(sorted(array[i-1 : j]))[k-1])

    return answer

