def Bubble_sort(a):
    for i in range(len(a)):
        swapped = False #Biến swap: nếu có chuowmg trình sẽ "thông minh" hơn
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        print(a)
        if not swapped:
            break
    return a

def Selection_sort(a):
    for i in range(len(a)):
        minInd = i
        for j in range(i+1, len(a)):
            if a[minInd] > a[j]:
                minInd = j
        if minInd != i:
            a[i], a[minInd] = a[minInd], a[i]
            print(a)

def Insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >=0 and a[j] > key:
            a[j+1] = a[j] #dịch các phần tử bên trái lên 1
            j -= 1
        a[j+1] = key
    return a 
    





n = [30, 11, 70, 45, 41]

print('Từng bước')
print(n)

print(Insertion_sort(n))
