n=int(input())
dem=0
while n!=0:
    dem+=n//5
    n//=5
print(dem)