H1 = int(input("Nhap SL mat hang H1: "))
H2 = int(input("Nhap SL mat hang H2: "))
H3 = int(input("Nhap SL mat hang H3: "))
H4 = int(input("Nhap SL mat hang H4: "))
H5 = int(input("Nhap SL mat hang H5: "))
H6 = int(input("Nhap SL mat hang H6: "))
h1, h2, h3, h4, h5, h6 = 100, 150, 120, 90, 130, 140
tonghoadon = H1 + H2 + H3 + H4 + H5 + H6
tonghoadon1 = (h1 * H1) + (h2 * H2) + (h3 * H3) + (h4 * H4) + (h5 * H5) + (h6 * H6)
# if tonghoadon >= 4:
#     print("Ban du dieu kien giam 20k")
#     print("tien goc: ", tonghoadon1,".000VND")
#     print("Tien uu dai: ", tonghoadon1 - 20,".000VND")
# if H6 >= 2:
#     print("Ban du dieu kien giam 20k")
#     print("tien goc: ", tonghoadon1,".000VND")
#     print("Tien uu dai: ", tonghoadon1 - 30,".000VND")
# if tonghoadon1 > 500: 
#     print("Ban du dieu kien giam 10%")
#     print("tien goc: ", tonghoadon1,".000VND")
#     print("Tien uu dai: ", tonghoadon1 * 0.1,".000VND")
if tonghoadon >= 4 and H6 >= 2: 
    print("Ban du dieu kien giam 40k")
    print("tien goc: ", tonghoadon1,".000VND")
    print("Tien uu dai: ", tonghoadon1 - 90,".000VND")
elif (tonghoadon >= 4 and tonghoadon1 > 500) or (H6 >= 2 and tonghoadon1 > 500):
    print("Ban du dieu kien giam 15%")
    print("tien goc: ", tonghoadon1,".000VND")
    print("Tien uu dai: ",tonghoadon * (15 / 100),".000VND")
elif tonghoadon >= 4 and H6 >= 2 and tonghoadon1 > 500:
    print("Ban du dieu kien giam 20%")
    print("tien goc: ", tonghoadon1,".000VND")
    print("Tien uu dai: ",tonghoadon * (20 / 100),".000VND")
    

    