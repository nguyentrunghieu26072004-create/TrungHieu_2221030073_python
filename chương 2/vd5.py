tong = 0
i = 1
n = int(input("nhap so phan tu trong day:"))

while i <= n:
    x = int(input("nhap so:"))
    if x % 2 == 0:
        tong = tong + x
    else:
        pass  
    i = i + 1  
print("tong cac so chan la:", tong) 