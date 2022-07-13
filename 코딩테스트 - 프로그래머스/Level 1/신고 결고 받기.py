from collections import defaultdict
# collections 모듈 : 데이터 처리를 위한 유용한 객체가 많이 있다.
# defaultdict : key값이 없을 경우 미리 지정해 놓은 초기(default)값을 반환하는 dictionary

def solution(id_list, report, k) :
    answer = []
    # 중복 신고 제거
    report = list(set(report))
    # user별 신고한 id 저장
    user = defaultdict(set)
    # user별 신고당한 횟수 저장
    cnt = defaultdict(int)

    for r in report :
        # report의 첫번째 값은 신고자 id, 두번째 값은 신고당한 id
        a, b = r.split()
        # 신고자가 신고한 id 추가
        user[a].add(b)
        # 신고당한 id의 신고 횟수 추가
        cnt[b] += 1
        
    for i in id_list :
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i] :
            if cnt[u] >= k :
                result += 1
        answer.append(result)
        
    return answer


# 다른 사람 코드

def solution(id_list, report, k) :
    answer = [0] * len(id_list)
    reports  = {x : 0 for x in id_list}

    for r in set(report) :
        reports[r.split()[1]] += 1

    for r in set(report) :
        if reports[r.split()[1]] >= k :
            answer[id_list.index(r.split()[0])] += 1
            
    return answer
