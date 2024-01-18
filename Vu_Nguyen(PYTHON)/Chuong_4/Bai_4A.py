# cấu trúc if-else cơ bản --> cấu trúc điều khiển 
tuoi = int(input("Nhập tuổi "))
gt = False # True -> Nam
if tuoi > 18 : # if + biểu thức logic + :
    print("đủ tuổi đi tù")
    if gt == True:
        print("Đi tù 10 năm")
    else:
        print("Đi tù 6 năm")
elif (16 <= tuoi <= 18): 
    print("Đủ tuổi đi trại giáo dưỡng")
else :  # lệnh còn lại khi biểu thức trên khi chưa đến
    print("Chưa đủ tuổi đi tù")