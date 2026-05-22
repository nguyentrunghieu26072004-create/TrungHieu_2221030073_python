m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

tong = m + n

max_digit = 0
temp = tong

while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
    temp //= 10

print("Tổng =", tong)
print("Chữ số lớn nhất trong tổng là:", max_digit)