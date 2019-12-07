def sort(x):
    t = len(x) # 6
    t1 = 0
    while t1 < t:
        t1 += 1
        t2 = -1
        for i in x[:-1]:
            t2 += 1
            if i > x[t2+1]:
                x1 = x[t2+1]
                x[t2+1] = x[t2]
                x[t2] = x1
    return x


n = int(input())
n1 = [int(i1) for i1 in input().split()]
n2 = sort(list(set(n1)))
print(len(n2))
print(*n2)