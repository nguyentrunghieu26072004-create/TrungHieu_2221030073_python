# vi du1 
def giaithuat(m):
    gt = 1
    for i in range(1, m + 1):
        gt = gt * i
    return gt

n = int(input("nhap vao mot so nguyen duong: "))
print("%d! = %d" % (n, giaithuat(n)))