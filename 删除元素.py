n = int(input())
n1 = [int(i) for i in input().split()]
i = int(input())
n1.pop(i)
for j in n1:
    print(j,end=' ')
