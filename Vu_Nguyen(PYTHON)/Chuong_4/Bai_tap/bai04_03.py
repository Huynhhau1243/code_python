month = int(input("Nhap thang: "))

if (1 <= month < 4): 
    print("Qúy 1")
elif (4 <= month < 7 ):
    print("Qúy 2")
elif (7 <= month < 10):
    print("Qúy 3")
elif (10 <= month < 13):
    print("Qúy 4")
else:
    print("Khong có thang", month)    