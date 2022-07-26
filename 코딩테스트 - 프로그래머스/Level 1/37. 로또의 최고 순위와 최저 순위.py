def solution(lottos, win_nums):
    best_rank, worst_rank = 7, 7
    
    for i in lottos :
        if i in win_nums :
            worst_rank -= 1
            best_rank -= 1
        elif i not in win_nums and i == 0 :
            best_rank -= 1
    
    if best_rank > 6 :
        best_rank = 6
    if worst_rank > 6 :
        worst_rank = 6
    
    return [best_rank, worst_rank]
    
# 다른 사람 코드
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
