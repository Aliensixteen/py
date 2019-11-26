n = input()
res = ''
for i in range(6,14):
    res = res + n[i]
    if i == 9 or i == 11:
        res = res + '-'
print(res)