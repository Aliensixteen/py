#http://acm.zzuli.edu.cn/problem.php?id=1101
def daoxu(x):
    sum = 0
    while x != 0:
        sum = sum * 10 + x % 10
        x = x // 10
    return sum

n = int(input())
n1 = daoxu(n)
print('%d'%(n+n1))