n=input()
l=1
dem=1
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        dem+=1
        l=max(l,dem)
    else:
        dem=1
print(l)
    