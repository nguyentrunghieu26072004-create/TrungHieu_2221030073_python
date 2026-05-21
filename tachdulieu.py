def tach_du_lieu():
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            noi_dung = f.read()

        chuoi_so = ""
        chuoi_chu = ""

        for c in noi_dung:
            if c.isdigit() or c.isspace():
                chuoi_so += c
            if c.isalpha() or c.isspace():
                chuoi_chu += c

        open("outso.txt", "w", encoding="utf-8").write(chuoi_so.strip())
        open("outchu.txt", "w", encoding="utf-8").write(chuoi_chu.strip())

        print("Đã tách dữ liệu thành công!")

    except FileNotFoundError:
        print("Không tìm thấy file input.txt")