num = int(input())
a,b = int(),int()
a = num
b = 0
while b <= num:
    b = b + 1
    if b % 10 == 4 or (b // 10) % 10 == 4 or (b // 100) % 10 == 4:
        a = a - 1
print(a)