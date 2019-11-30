#http://acm.zzuli.edu.cn/problem.php?id=1102
def tp(x):
    x1 = x * 0.05
    if x1 % 1 < 0.25:
        x1 = x1 - (x1 % 1)
    if x1 % 1 >= 0.25 and x1 % 1 < 0.75:
        x1 = x1 - (x1 % 1) + 0.5
    if x1 % 1 >= 0.75:
        x1 = x1 - (x1 % 1) + 1
    return x1




n = float(input())
print(tp(n))