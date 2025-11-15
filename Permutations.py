n=int(input())
if 1<n<=3:
    print('NO SOLUTION')
else:
    c=[]
    l=[]
    for i in range(1,n+1):
        if i%2==0:
            c.append(i)
        else:
            l.append(i)
    a=c+l
    for i in a:
        print(i,end=" ")