C = int(input())
for i in range(C):
    n = input()
    res = ''
    for j in range(1,len(n),2):
        res = res + n[j] + n[j-1]
    if len(n) % 2 == 1:
        res = res + n[-1]
    print(res)