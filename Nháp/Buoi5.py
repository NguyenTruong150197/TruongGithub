#Bài 1
# km = float(input("Nhập số km vào từ bàn phím: "))
# tien = 5000
# if 0 < km <= 1:
#     print("Số tiền phải trả sau khi chạy {} km là {} đồng".format(km,tien))
# elif 1 < km <= 5:
#     tien2 = (km - 1)*4500 + 5000
#     print("Số tiền phải trả sau khi chạy {} km là {} đồng".format(km,tien2))
# elif 5 < km <= 120:
#     tien3 = (km - 5)*3500 + 4500*4 + 5000
#     print("Số tiền phải trả sau khi chạy {} km là {} đồng".format(km,tien3))
# else:
#     tien4 = (((km - 5)*3500 + 4500*4 + 5000)*1/10)
#     print("Số tiền phải trả sau khi chạy {} km là {} đồng".format(km,tien4))    



#Bài 2
bd = float(input("Nhập thời gian bắt đầu sử dụng máy tính: "))
kt = float(input("Nhập thời gian kết thúc sử dụng máy tính: "))
sd = kt - bd
m = 5000
if 0 <= bd <= 7:
    if sd >= 7:
        m1 = (sd*m*300*60)/0.15
        print("Số tiền phải trả là:",m1,"đồng")
    elif 0 < sd < 7:
        m2 = sd*m*300
        print("Số tiền phải trả là:",m2,"đồng")
    else:
        print("Không sử dụng máy tính")
elif 7 < bd <= 17:
    if sd >= 6:
        m3 = (sd*m*400*60)/0.1
        print("Số tiền phải trả là:",m3,"đồng")
    elif 0 < sd < 6:    
        m4 = sd*m*400
        print("Số tiền phải trả là:",m4,"đồng")
    else:
        print("Không sử dụng máy tính")
else:
    if sd >= 4:
        m5 = (sd*m*350*60)/0.12
        print("Số tiền phải trả là:",m5,"đồng")
    elif 0 < sd < 4:
        m6 = sd*m*350
        print("Số tiền phải trả là:",m6,"đồng")
    else:
        print("Không sử dụng máy tính")