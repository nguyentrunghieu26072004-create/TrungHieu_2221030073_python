def giai_thua(n):
    gt = 1
    for i in range(1, n + 1):
        gt *= i
    return gt

n = int(input("Nhap so nguyen duong: "))
print(f"{n}! = {giai_thua(n)}")


# Ham co tham so mac dinh
def tong(a, b=10):
    return a + b

print(tong(1, 2))
print(tong(5))


# Ham co nhieu tham so
def tong_nhieu(*so):
    return sum(so)

print(tong_nhieu(1, 2))
print(tong_nhieu(1, 2, 3))
print(tong_nhieu(1, 2, 4, 5, 6))