def giaithua(n):
 gt=1
 for i in range(1,n+1):
  gt=gt*i
 return gt
n=int(input("nhap so nguyen:"))
print("%d!=%d"%(n,giaithua(n)))