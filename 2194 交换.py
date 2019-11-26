import math
n = input()
res = ''
for i in range(1,len(n)):
    res = res + n[i] + n[i-1]
    x = [int(j) for j in res]
    x1 = x[0] * 10 + x[1]
    print('%.2f'%(math.sqrt(x1)))