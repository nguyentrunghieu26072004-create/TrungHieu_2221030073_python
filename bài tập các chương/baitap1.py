class Circle:
    pi = 3.141592

    def __init__(self,radius=1):
        self.bk = radius
    
    def dientich(self):
        return self.bk * self.bk * self.pi

c = Circle(5)
print("Dien tich cua hinh tron la", c.dientich())