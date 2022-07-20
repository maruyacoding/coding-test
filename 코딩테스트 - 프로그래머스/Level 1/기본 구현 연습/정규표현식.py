# 정규표현식은 복잡한 문자열을 처리할 때 사용하는 기법

import re
p = re.compile('[a-z]+')
m = p.match('python')
print(m)

a = p.match('3 python')
print(a)

if m :
    print('Match found: ', m.group())
else :
    print('No match')

