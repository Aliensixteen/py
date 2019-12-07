def zuxian(x,y):
    if x == y:
        return x
    elif x > y:
        return zuxian(x//2,y)
    else:
        return zuxian(x,y//2)


x,y = [int(i1) for i1 in input().split()]
print(zuxian(x,y))