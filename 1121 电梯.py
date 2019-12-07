n = int(input())
n1 = [int(i1) for i1 in input().split()]
t = 0
t = t + n * 5
a = 0
for i in n1:
    if i > a:
        t = t + (i - a) * 6
        a = i
    if i < a:
        t = t + (a - i) * 4
        a = i
    if i == a:
        t = t
print(t)