n = int(input())
n1 = [int(i) for i in input().split()]
a = int(99999999)
b = int(0)
for i in range(0,n):
    if n1[i] < a:
        a = n1[i]
        b = i
print(a,b,end=' ')
