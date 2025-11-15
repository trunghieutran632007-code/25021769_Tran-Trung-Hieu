n=input()
D=[0]*26
for i in n:
	D[ord(i)-65]+=1
dem=0
vt=0
for i in range(len(D)):
	if D[i]%2==1:
		dem+=1
		vt=i
a=''
if dem>=2:
	print('NO SOLUTION')
elif dem==1:
	for i in range(len(D)):
		a+=(D[i]//2)*chr(i+65)
	print(a+chr(vt+65)+a[::-1])
else:
	for i in range(len(D)):
		a+=(D[i]//2)*(chr(i+65))
	print(a+a[::-1])	