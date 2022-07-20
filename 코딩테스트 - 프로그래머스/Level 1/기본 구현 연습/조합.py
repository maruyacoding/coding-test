# DFS(Depth-First Search) 구현
l = [1,2,3,4]
n = len(l)
r = 3
answer = []

def dfs(idx, list) :
    if len(list) == r :
        answer.append(list[:])
        return
    for i in range(idx, n) :
        dfs(i + 1, list + [l[i]])
    
dfs(0, [])
print(answer)


# 글로벌 변수 미사용 구현

def combination(arr, r) :
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen) :
        if len(chosen) == r:
            print(chosen)
            return
        '''
         chosen(뽑은 조합 원소)가 없으면 start = 0으로
         그 외에는 뽑은 조합의 가장 마지막 요소를 값의 인덱스 출력
         arr = [1,2,3,4]
         예를 들어 chosen = [1,2]를 뽑은 상태라면 start = arr.index(2)이므로 1이고
         거기에 1을 더해 최종 2
        '''

        start = arr.index(chosen[-1]) + 1 if chosen else 0

        for nxt in range(start, len(arr)) :
            # 만약 아직 뽑지 않았고 ~~ 조건이라면
            if used[nxt] == 0 and (nxt == 0 or arr[nxt - 1] != arr[nxt] or used[nxt - 1]) :
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                # 다 뽑고 마지막 요소부터 pop하고 방문 해제
                chosen.pop() 
                used[nxt] = 0
    generate([])

combination([1,2,3,4] , 3)
    
