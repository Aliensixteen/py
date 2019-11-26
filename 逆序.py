n = int(input())
n1 = [int(i) for i in input().split()]
stack = []
for j in n1:
    stack.append(j)
while (len(stack) > 0):
    x = stack.pop()
    print('%4d'%x,end='')