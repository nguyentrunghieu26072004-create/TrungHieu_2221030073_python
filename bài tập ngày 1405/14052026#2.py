n = int(input("Nhập số phần tử n: "))

while n <= 0 or n >= 200:
    n = int(input("Nhập lại n (0 < n < 200): "))

tong_chan = 0

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    
    if x % 2 == 0:
        tong_chan += x

print("Tổng các phần tử chẵn là:", tong_chan)

if tong_chan % 7 == 0 and tong_chan < 200:
    print("Tổng chia hết cho 7 và nhỏ hơn 200")
else:
    print("Tổng không thỏa mãn điều kiện")