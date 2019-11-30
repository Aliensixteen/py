#http://acm.zzuli.edu.cn/problem.php?id=1106
def hw(x):
    x1 = 0
    while x != 0:
        x1 = x1 * 10 + x % 10
        x = x // 10
    return x1

m ,n = [int(i) for i in input().split()]
for i1 in range(m,n):
    if i1 == hw(i1):
        print(i1,end=' ')