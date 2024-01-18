km = int(input("Nhập số km đã đi: "))

if km == 1: 
    km1 = km * 15
    print(km1)
elif 2 <= km <= 30:
    tien = (15 + (km - 1) * 13)
    print(tien) 
elif km >= 31:
    tien_2 = (15 + 29 * 13 + (km - 30) * 10)
    print(tien_2)