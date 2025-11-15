import math
def haiconma(a):
    if a==1:
        return 0
    elif a==2:
        return 6
    elif a==3:
        return 28
    elif a==4:
        return 96
    else:
        k=((a**2)*(a**2-1))//2

        return k-((8+24+4*(4*(a-4)+4)+24*(a-4)+8*(a-4)*(a-4))//2)

    
n=int(input())
for i in range(1,n+1):
    print(haiconma(i))