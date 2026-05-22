class Circle:
    def dientich(self):
        return self.bk * self.bk * 3.141592

    def nhap(self):
        self.bk = float(input("Nhap ban kinh: "))

c = Circle()
c.nhap()
print("Dien tich cua hinh tron la: ", c.dientich())