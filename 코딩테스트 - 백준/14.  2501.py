n, k = map(int, input().split(' '))

div = [i for i in range(1, n + 1) if n % i == 0]
print(0 if len(div) < k else div[k - 1])
