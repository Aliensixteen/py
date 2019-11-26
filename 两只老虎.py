T = int(input())
for i in range(T):
    a,b,c = [int(i1) for i1 in input().split()]
    c0 = int(c / 4)
    for i1 in range(0,c0+1):
        for i2 in range(0,c0-i1+1):
            i3 = c0 - i1 -i2
            if 2*i1 + 2*i3 == a and i1 + i2 == b: 
                print(i1)