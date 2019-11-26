a = [0,1,2,3,4]
for i in range(5,56):
    a.append('0')
    a[i] = a[(i-1)] + a[(i-3)]
while True:
    n = int(input())
    if n == 0:
        break
    else:
        print('%d'%a[n])