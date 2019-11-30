def d(x1):
    if x1 >= 60:
        x1 =(x1 - 50) // 10
        return x1
    if x1 < 60:
        return 0




n = int(input())
x1 = float() #学点 * 学分
x2 = float() #总学分
for i in range(0,n):
    x,y = [int(j) for j in input().split()]
    x1 = x1 + x * d(y)
    x2 = x2 + x
    x3 = x1 / x2
if x3 < 1:
    x3 = 1
print('%.1f'%x3)