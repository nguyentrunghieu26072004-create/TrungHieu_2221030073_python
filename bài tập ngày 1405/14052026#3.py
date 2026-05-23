a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

# Tìm chữ số nhỏ nhất của b
min_digit = 9
temp = b

while temp > 0:
    digit = temp % 10
    
    if digit < min_digit:
        min_digit = digit
        
    temp //= 10

print("Chữ số nhỏ nhất của b là:", min_digit)

# Kiểm tra chia hết
if min_digit != 0 and a % min_digit == 0:
    print(a, "chia hết cho", min_digit)
else:
    print(a, "không chia hết cho", min_digit)