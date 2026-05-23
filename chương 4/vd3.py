f = open("input.txt", "r")

s = f.readlines()

for i in s:
    num = int(i)

    print("Các số nguyên tố của", num, "là:")

    for j in range(2, num + 1):

        if num % j == 0:

            kt = True

            for k in range(2, int(j**0.5) + 1):

                if j % k == 0:
                    kt = False
                    break

            if kt:
                print(j)

f.close()