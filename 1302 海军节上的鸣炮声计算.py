n,a,b,c = [int(i) for i in input().split()]
x = {0}
for j in range (1,n):
    a2 = j * a
    x.add(a2)
    b2 = j * b
    x.add(b2)
    c2 = j * c
    x.add(c2)
print(len(x))



n,a,b,c = [int(i) for i in input().split()]
x = set()
for j in range (n):
    a2 = j * a
    x.add(a2)
    b2 = j * b
    x.add(b2)
    c2 = j * c
    x.add(c2)
print(len(x))