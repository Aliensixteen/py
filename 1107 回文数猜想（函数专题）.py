#http://acm.zzuli.edu.cn/problem.php?id=1107&csrf=ZYHptANXa2Y2TilbEMaI0dVuPrmlbLU6
def daoxu(x):
    sum = 0
    while x != 0:
        sum = sum * 10 + x % 10
        x = x // 10
    return sum



n = int(input())
n1 = n
while True:
    print(n1,end=' ')
    if n1 != daoxu(n):
        n = n1 + daoxu(n)
        n1 = n
    else:
        break