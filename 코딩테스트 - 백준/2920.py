a = list(map(int, input().split(' ')))

if a == sorted(a, reverse = False) :
    print('ascending')
elif a == sorted(a, reverse = True) :
    print('descending')
else :
    print('mixed')
    
    
# 강의 코드
a = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1, 8) :
    if a[i] > a[i - 1] :
        descending = False
    elif a[i] < a[i - 1] :
        ascending = False

if ascending :
    print('ascending')
elif descending :
    print('descending')
else :
    print('mixed')
