x = int(input("X = "))
if (0 <= x): 
    print(True)
if ((-1 <= x <= 2) and (4 <= x <= 6)):
    print(True)
if (-2 < x < 2):
    print(True)
else: 
    print(False)
    
if ((-4 < x <= 0) and (4 < x)):
    print(True)
else: 
    print(False)