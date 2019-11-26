T = int(input())
a = int(0)
for i in range(T):
    n = input()
    if n >= '0' and n <= '9':
        n = int(n)
        a += n
    if n == 'D':
        a *= 2
    if n == 'C':
        a = 0
print(a)