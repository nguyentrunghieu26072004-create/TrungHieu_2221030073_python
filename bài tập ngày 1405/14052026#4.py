m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

tong = m + n

print("Tổng m + n =", tong)

# Tìm chữ số lớn nhất trong tổng
max_digit = 0
temp = tong

while temp > 0:
    digit = temp % 10
    
    if digit > max_digit:
        max_digit = digit
        
    temp //= 10

print("Chữ số lớn nhất trong tổng là:", max_digit)