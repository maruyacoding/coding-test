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
    
            
