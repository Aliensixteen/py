#http://acm.zzuli.edu.cn/problem.php?id=1120&csrf=diY6KdH2vlgl0dsIzzMJOQ80TljSt2kO
n = int(input())
n1 = [int(i1) for i1 in input().split()]
a = 999999
b = -999999 
for i in n1:
    if i > b:
        b = i #最大判断
for j in n1:
    if a > j:
        a = j #最小判断
b1 = n1[-1] #最后一位
a1 = n1[0] #第一位
i2 = -1
for k in n1:
    i2 += 1
    if k == a:
        n1[0] = a
        n1[i2] = a1 #最小换位
        break
b1 = n1[-1] #最后一位
a1 = n1[0] #第一位
i3 = -1
for k1 in n1:
    i3 += 1
    if k1 == b:
        n1[-1] = b
        n1[i3] = b1 #最大换位
        break
print(*n1)
