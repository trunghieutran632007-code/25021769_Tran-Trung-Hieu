class Sv:
    def __init__(self, id, name, pt1, pt2, pt3):
        self.id = id
        self.name = name
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3
    def avrPt(self):
        return self.pt1 * 0.1 + self.pt2 * 0.3 + self.pt3 * 0.6
    def __repr__(self):
        return f'Ho ten: {self.name} \nMa sinh vien: {self.id} \n Diem trung binh: {self.avrPt()}'
    
sv1 = Sv(25021769, 'Tran Trung Hieu' , 10.0, 5.0, 4.0)
print(sv1)

numofSv = int(input("Nhap so luong sinh vien them vao: "))
lstOfStudens = []
for i in range(numofSv):
    
