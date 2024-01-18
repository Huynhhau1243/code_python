x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

if (x > y and x > z): 
    print("số lớn nhất: ", x)
elif(y > x and y > z):
    print("số lớn nhất: ", y)
else:
    print("số lớn nhất: ", z)
    # số bé nhất    
if (x < y and x < z):
    print("Số bé nhất: ", x)
elif(y < x and y < z):
    print("Số bé nhất: ", y)
else:
    print("Số bé nhất: ", z)

if x * y * z > 0: 
    print("ba so cung dấu")
else: 
    print("ba số trái dấu")

if (x * y < 0 and x * z < 0):
    print("(",x,",",y,")",",", "(", x,",",z,")")
elif (y * x < 0 and y * z < 0):
    print("(",y,",",x,")",",", "(", y,",",z,")")
else:
    print("(",z,",",x,")",",", "(", z,",",y,")")