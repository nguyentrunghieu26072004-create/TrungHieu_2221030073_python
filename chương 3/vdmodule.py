import math

# Hàm tính toán
def dien_tich_hcn(d, r):
    return d * r

def chu_vi_hcn(d, r):
    return 2 * (d + r)

def dien_tich_hv(a):
    return a * a

def dien_tich_tron(r):
    return math.pi * r * r

# Nhập dữ liệu và in kết quả
d = float(input("Nhập chiều dài HCN: "))
r = float(input("Nhập chiều rộng HCN: "))

print("Diện tích HCN:", dien_tich_hcn(d, r))
print("Chu vi HCN:", chu_vi_hcn(d, r))

a = float(input("Nhập cạnh hình vuông: "))
print("Diện tích HV:", dien_tich_hv(a))