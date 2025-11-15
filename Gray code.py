def doi(a):
    if a=='1':
        return '0'
    else:
        return '1'
n=int(input())
a=['0']*(n)
c=[i for i in range(n-1,-1,-1)]+[i for i in range(1,n-1)]
c=c*((2**n)//(len(c)))+c[:((2**n)//(len(c)))]
print(''.join(a))
for i in range((2**n)-1):
    a[c[i]]=doi(a[c[i]])
    print(''.join(a))
