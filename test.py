#W6A9
def Nhap_dic(pairs):
    dic = {}
    for pair in pairs:
        key, value = pair.split(":")
        value = int(value)
        if key not in dic:
            dic[key] = 0
        dic[key] += value
    return dic
        



line1 = input()
pairs1 = line1.split( )
line2 = input()
pairs2 = line2.split( )
dic1 = {}
dic2 = {}
dic1 = Nhap_dic(pairs1)
dic2 = Nhap_dic(pairs2)

#Gop 2 dict
newdic = dic1
for key, value in dic2.items():
    if key in newdic:
        newdic[key] += value
    else:
        newdic[key] = value
for key in sorted(newdic.keys()):
    print(f'{key}:{newdic[key]}')


