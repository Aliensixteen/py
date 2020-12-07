for i in range(1,10):
    for j in range(1,i+1):
        if j >= 1:
            print(j,'*',i,'=',j*i,end=' ')
    print()