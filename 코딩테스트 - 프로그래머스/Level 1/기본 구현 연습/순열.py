def permutation(arr, r) : # 사용할 list, 선택할 갯수 r
    arr = sorted(arr)
    # 사용된 원소를 저장할 배열을 만든다.
    used = [0 for _ in range(len(arr))] 

    def generate(chosen, used) :
        # 선택리스트에 순열의 원소를 저장하다가 갯수가 r개가 되면 출력 후 함수를 종료한다.
        if len(chosen) == r:
            print(chosen)
            return

        for i in range(len(arr)) :
            # 아직 사용하지 않았다면
            if not used[i] : 
                # 선택리스트에 저장하고 방문체크
                chosen.append(arr[i])
                used[i] = 1 
                # 다시 generate 함수를 반복한다.
                generate(chosen, used)
                # 하나의 순열이 만들어지면 다시 uncheck한다.
                used[i] = 0
                chosen.pop()

    generate([], used)

permutation([1,2,3,4], 3)


# practice
def permutation(arr, r) :
    arr = sorted(arr)
    used = [ 0 for _ in range(len(arr))]

    def generate(chosen, used) :
        if len(chosen) == r :
            print(chosen)
            return
        
        for i in range(len(arr)) :
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)

permutation([1,2,3], 3)