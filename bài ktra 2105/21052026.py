#CÂU 1
n = int(input("Nhập số phần tử n: "))

while n <= 0 or n >= 100:
    n = int(input("Nhập lại n (0 < n < 100): "))

tong = 0
dem = 0

for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    
    if 0 < x < 1000:
        tong += x
        dem += 1

if dem > 0:
    print("Trung bình cộng =", tong / dem)
else:
    print("Không có phần tử thỏa mãn")

#CÂU 2
n = int(input("Nhập số nguyên dương n: "))

tong = 0
temp = n

while temp > 0:
    tong += temp % 10
    temp //= 10

print("Tổng các chữ số =", tong)

if tong % 3 == 0:
    print("Tổng chia hết cho 3")
else:
    print("Tổng không chia hết cho 3")

#CÂU 3
n = int(input("Nhập số nguyên dương n: "))

tich = 1
temp = n

while temp > 0:
    tich *= temp % 10
    temp //= 10

print("Tích các chữ số =", tich)

if tich % 2 == 0 and tich > 20:
    print("Tích là số chẵn và lớn hơn 20")
else:
    print("Tích không thỏa mãn điều kiện")

#CÂU 4
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

tong = a + b

print("Tổng =", tong)

max_digit = 0
temp = tong

while temp > 0:
    digit = temp % 10
    
    if digit > max_digit:
        max_digit = digit
        
    temp //= 10

print("Chữ số lớn nhất là:", max_digit)

#CÂU 5
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

tong = 0
temp = n

while temp > 0:
    tong += temp % 10
    temp //= 10

print("Tổng các chữ số của n =", tong)

if tong != 0 and m % tong == 0:
    print(m, "chia hết cho", tong)
else:
    print(m, "không chia hết cho", tong)