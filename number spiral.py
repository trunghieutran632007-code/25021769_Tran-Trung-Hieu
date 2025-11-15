def xoanoc(x,y):
    if x>y:
        if x%2==0:
            return x*x-(y-1)
        else:
            return (x-1)**2+y
    else:
        if y%2==1:
            return y*y-(x-1)
        else:
            return (y-1)**2+x
n=int(input())
m=[]
for i in range(n):
    a=[]
    a=[int(i) for i in input().split()]
    m.append(a)
for i in m:
    print(xoanoc(i[0],i[1]))
    
