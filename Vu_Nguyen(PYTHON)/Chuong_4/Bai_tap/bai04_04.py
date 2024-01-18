gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))

if 0 <= gio < 24:
    print(gio," giờ", end="/")
    if 0 <= phut < 60:
        print(phut, "phút", end="/")
        if 0 <= giay <  60:
            print(giay, "giây")
    print("Hợp lệ")
else: 
    if (gio > 23):
        print("Gio khong hop le")
        if phut > 60: 
            print("Phut khong hop le")
            if giay > 60:
                print("Giay khong hop le")