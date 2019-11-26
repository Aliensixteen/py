N = int(input())
for i in range(N):
    n,m = [int(i1) for i1 in input().split()]
    for k in range(1,n):
        m += 2
    print(m)