def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

x = int(input("nhap so thu nhat: "))
y = int(input("nhap so thu hai: "))
print("tong cua hai so la:", cong(x, y))
print("hieu cua hai so la:", tru(x, y))