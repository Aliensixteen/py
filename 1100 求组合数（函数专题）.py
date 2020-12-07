#http://acm.zzuli.edu.cn/problem.php?id=1100
def cj(x):
    sum = 1
    i = x
    while i > 1:
        sum *= i
        i -= 1
    return sum


m , k = [int(i) for i in input().split()]
num = int()
num = cj(m) / (cj(k) * (cj(m-k)))
print('%d'%num)
# 测试
print('%d'%num)