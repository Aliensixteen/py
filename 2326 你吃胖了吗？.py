a,b = [float(i) for i in input().split()]
bmi = a / (b **2)
if bmi < 18.5 :
    print('偏瘦')
if 18.5 <= bmi < 24 :
    print('正常')
if 24 <= bmi < 28 :
    print('偏胖')
if 28 <= bmi < 30 :
    print('肥胖')
if 30 <= bmi :
    print('重度肥胖')