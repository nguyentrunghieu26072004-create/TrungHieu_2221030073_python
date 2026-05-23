# ==============================
# Vi du 1: Bien toan cuc

b = 20

def msg_global():
    a = 10  
    print("Gia tri cua a la:", a)
    print("Gia tri cua b la:", b)

msg_global()

print("Gia tri cua b ben ngoai ham la:", b)

print("-" * 30)

# Vi du 2: Bien cuc bo

def msg_local():
    a = 10   # khai bao bien cuc bo a
    print("Gia tri cua a la:", a)

msg_local()

# print(a)
# Dong nay se bao loi vi a la bien cuc bo,
# chi ton tai trong ham msg_local()

print("-" * 30)