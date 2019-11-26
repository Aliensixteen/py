#http://acm.zzuli.edu.cn/problem.php?id=2372&csrf=D1KEJ2XFN2EYSEFTfWuWHm2jU8RuG3Fe
n = int(input())
for i in range(n):
    k,a,b = [int(i1) for i1 in input().split()]
    a1 = 0
    i = 0
    while True:
        a1 += a
        k += b
        i += 1
        if a1 > k:
            print(i)
            break
