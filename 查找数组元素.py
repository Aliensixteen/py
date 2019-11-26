n = int(input())
n1 = [int(i) for i in input().split()]
x = int(input())
a = int(-1)
x1 = int(0)
for i1 in n1:
    a += 1
    if i1 == x:
        n1.pop(a)
        x1 += 1
        break
if x1 == 0:
    print('Not Found')
else:
    for j in n1:
        print('%4d'%j,end='')
