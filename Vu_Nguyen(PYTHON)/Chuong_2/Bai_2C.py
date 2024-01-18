# Nhập xuất dữ liệu với biến 
data_name = input("Nhập dữ liệu vào! ")
data_age = int(input("Nhập tuổi vào đi bạn eey! "))
data_height, data_weight = input("Nhập chiều cao và cân nặng vào đi!: ").split()
print("Người vừa nhập có tên là: ",data_name, ".anh ấy rất đẹp trai")
print(f"Năm nay anh ấy {data_age} tuổi rồi")
print("Chiều cao =", data_height, ". Cân nặng =", data_weight, sep="")

# split() cắt khoảng trắng 
# muốn nối tiếp print dùng end = "" 