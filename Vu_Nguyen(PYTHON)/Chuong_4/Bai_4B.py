# cấu trúc if else rút gọn 
tuoi = 17
# tuổi >= 18
# ket_luan = "du tuoi di tu" if tuoi >= 18 else "Vao trai cai tao" if 16 < tuoi < 18 else "chua du tuoi di tu"
ket_luan = ("Chua du tuoi di tu", "Du tuoi di tu")(tuoi >= 18)
                    #0                  1         
# 0 là false, 1 la true
print(ket_luan)
