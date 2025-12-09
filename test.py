def So_doi_xung(n):
    temp = n
    new_Num = 0
    while n > 0:
        new_Num *= 10
        new_Num += n % 10
        n //= 10
    return temp == new_Num
lst = list(map(int, input().split()))
print(lst)
