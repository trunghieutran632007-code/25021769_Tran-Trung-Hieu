def doi(a):
    if a=='1':
        return '0'
    else:
        return '1'
n=int(input())
a=['0']*(n)
print(''.join(a))
a[n-1]=doi(a[n-1])
print(''.join(a))
gh=0
vt=n-2
for i in range((2**n)//2):
    if vt<gh:
        vt=n-1
        gh+=1
        a[vt]=doi(a[vt])
        print(''.join(a))
        vt=n-2
    else:
        a[vt]=doi(a[vt])
        print(''.join(a))
        a[vt+1]=doi(a[vt+1])
        print(''.join(a))
        vt-=1


