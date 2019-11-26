T = int(input())
for i in range(T):
    a,b,c = [int(i1) for i1 in input().split()]
    if a / 30 >= 1:
        j = 0
        a1 = a
        while a >= 30:
            j += 1
            a -= 30
        sh = a1 * b + j * c
        print('%d'%sh)
    else:
        sh = a * b
        print('%d'%sh)