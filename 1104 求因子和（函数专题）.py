#http://acm.zzuli.edu.cn/problem.php?id=1104
def yz(x):
    x1 = 0
    for i in range(2,n):
        if x % i == 0:
            x1 += i
    return x1 + 1


n = int(input())
print(yz(n))