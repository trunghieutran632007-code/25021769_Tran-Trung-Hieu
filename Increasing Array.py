n=int(input())
a=[int(i) for i in input().split()]
dem=0
for i in range(n-1):
    if a[i]>a[i+1]:
        dem+=(a[i]-a[i+1])
        a[i+1]=a[i]
print(dem)

