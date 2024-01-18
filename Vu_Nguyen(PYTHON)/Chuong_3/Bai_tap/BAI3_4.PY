N = int(input("Nhap so can dao: "))
chuc = ()
don_vi = ()
chuc = N % 100 // 10
tram = N // 100 % 10
don_vi = N % 10 
dao_nguoc = (don_vi * 100) + (chuc * 10) + tram 
print(dao_nguoc)