a=int(input())
m=[i for i in range(1,a+1)]
tong=a*(a+1)//2
if tong%2==1:
    print('NO')
else:
    print('YES')
    n=[]
    v=[]
    if a%2==0:
        n=m[:a//4]+m[3*(a//4):]
        v=m[a//4:3*(a//4)]
    else:
        v.append(m[a-1])
        m.pop(a-1)
        a=len(m)
        n=m[:a//4+1]+m[3*(a//4)+1:]
        v=v+m[a//4+1:3*(a//4)+1]
    print(len(n))
    for i in n:
        print(i,end=' ')
    print()
    print(len(v))
    for i in v:
        print(i,end=" ")


    
