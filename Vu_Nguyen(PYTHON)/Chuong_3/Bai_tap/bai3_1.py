x = float(input("X = "))
y = float(input("Y = "))

import math
bieu_thuc1 = (x * y) + (x / y)
bieu_thuc2 = x + 1 / (x + 1 / (x + 1 / (x + y)))
bieu_thuc_3 = math.sqrt(((3 * x + 2 * y) * (3 * x + 2 * y)) * (((5 * x) + 1) * ((5 * x) + 1) * ((5 * x) + 1)))
print( bieu_thuc1,"\n",bieu_thuc2,"\n",bieu_thuc_3)