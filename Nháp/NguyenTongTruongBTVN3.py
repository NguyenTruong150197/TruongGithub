#Bài 1
# def func1(*number):
#     return print(number)

# func1(3,5,76,74,2,8)

#Bài 1 (Thầy chữa)
# def func1(*args):
#     for i in range(0, len(args)):
#         if i == len(args) - 1:
#             print(args[i])
#         else:
#             print(args[i],end = ", ")

# func1(3,5,76,74,2,8)
# func1(3,5,7)



#Bài 2
# def calculation(a,b):
#     tong = a + b
#     hieu = a - b
#     tich = a*b
#     thuong = a/b
#     return print("Tổng là {}, phép trừ là {}, phép nhân {}, phép chia {}".format(tong,hieu,tich,thuong))

# calculation(9,3)

#Bài 2 (Thầy chữa)
#Cách 1
# def calculation(a, b):
#     print("Tổng 2 số là:",a + b)
#     print("Hiệu 2 số là:",a - b)
#     print("Tích 2 số là:",a*b)
#     print("Thuong 2 số là:",a/b)
    
# calculation()

#Cách 2
# def calculation(a,b):
#     list = []
#     sum = a + b
#     list.append(sum)
    
#     minus = a - b
#     list.append(minus)
    
#     multiple = a*b
#     list.append(multiple)
    
#     divide = a/b
#     list.append(divide)
    
#     return list

# result = calculation(5,9)
# print("Tổng 2 số là:",result[0])
# print("Hiệu 2 số là:",result[1])
# print("Tích 2 số là:",result[2])
# print("Thương 2 số là:",result[3])



#Bài 3
#a
# def show_employee(name,salary):
#     return print("Tên nhân viên là",name,"\nMức lương là",salary)

# show_employee("Truong",9000)

#b
# def show_employee(name):
#     salary = 9000
#     return print("Tên nhân viên là",name,"\nMức lương là",salary)

# show_employee("Truong")

#Bài 3 (Thầy chữa)
# def show_employee(name,salary = 9000):
#     print(f"Tên nhân viên là {name} với mức lương {salary}")
    
# show_employee("Nam", 4500)
# show_employee("Khôi")



#Bài 4
# def outer_func(a,b):
#     addition = a + b
#     return print(addition + 5)

# outer_func(4,5)

#Bài 4 (Thầy chữa)
# def outer_func(a,b):
#     def addition(c,d):
#         return c + d
#     return 5 + addition(a,b)

# print(outer_func(3,5))



#Bài 5
# def tinh_tong(n):
#     if n == 0:
#         return 0
#     else:
#         return (n + tinh_tong(n - 1))
    
# number = 10
# print("Tổng của các số từ 0 đến 10 là",tinh_tong(number))

#Bài 5 (Thầy chữa)
# def sum(n):
#     if n < 1:
#         return 0
#     else:
#         return n + sum(n - 1)
    
# print("Tổng là:",sum(10))



#Bài 6
# import math
#1
# def phuong_trinh_bac_1(a,b):
    # """Hàm giải phương trình bậc 1 có dạng
    # a*x + b = 0
    # """
    # if a == 0:
    #     if b == 0:
    #         return print("Phương trình có vô số nghiệm")
    #     else:
    #         return print("Phương trình vô nghiệm")
    # else:
    #     return print("Phương trình có nghiệm là:",- b/a)

#2
# def phuong_trinh_bậc_2(a,b,c):
    # """Hàm giải phương trình bậc 2 có dạng
    # a*x*x + b*x + c = 0
    # """
    # if a == 0:
    #     if b == 0:
    #         return print("Phương trình vô nghiệm")
    #     else:
    #         return print("Phương trình có nghiệm là:",-c/b)
    # else:
    #     delta = b*b - 4*a*c
    #     if delta < 0:
    #         return print("Phương trình vô nghiệm")
    #     elif delta == 0:
    #         return print("Phương trình có nghiệm kép x1 = x2 =",-b/(2*a))
    #     else:
    #         x1 = float((-b + math.sqrt(delta))/(2*a))
    #         x2 = float((-b - math.sqrt(delta))/(2*a))
    #         return print("Phương trình có 2 nghiệm là: x1 =",x1,"và x2 =",x2)

#3

#Bài 6 (Thầy chữa)
# import module_GiaiPhuongTrinhBacNhat
# import module_GiaiPhuongTrinhBacHai
# import module_TinhChuViVaDienTich

# while True:
#     print("Nhập chức năng bạn muốn thực hiện (Enter số tương ứng)\
#         [1] - Giải PT Bậc Nhất\
#         [2] - Giải PT Bậc Hai\
#         [3] - Tính chu vi, diện tích các hình\
#         [0] - Kết thúc")
#     choice = int(input("Xin mời nhập: "))
#     if choice == 1:
#         a = float(input("Nhập số a = "))
#         b = float(input("Nhập số b = "))
#         module_GiaiPhuongTrinhBacNhat.GiaiPTBacNhat(a,b)
#     elif choice == 2:
#         a = float(input("Nhập số a = "))
#         b = float(input("Nhập số b = "))
#         c = float(input("Nhập số c = "))
#         module_GiaiPhuongTrinhBacHai.GiaiPTBacHai(a,b,c)
#     elif choice == 3:
#         while True:
#             print("Chọn hình muốn tính Chu vi và Diện tích\
#                 [1] - Hình Tròn \
#                 [2] - Hình Chữ Nhật \
#                 [3] - Hình Tam Giác \
#                 [0] - Thoát")
#             shape_choice = int(input("Chọn loại hình: "))
#             if shape_choice == 1:
#                 r = float(input("Nhập bán kính hình tròn r = "))
#                 while r > 0:
#                     module_TinhChuViVaDienTich.HinhTron(r)
#                     break
#             elif shape_choice == 2:
#                 a = float(input("Nhập cạnh a = "))
#                 b = float(input("Nhập cạnh b = "))
#                 while (a > 0 and b > 0):
#                     module_TinhChuViVaDienTich.HinhChuNhat(a,b)
#                     break
#             elif shape_choice == 3:
#                 a = float(input("Nhập cạnh thứ nhất a = "))
#                 b = float(input("Nhập cạnh thứ 2 b = "))
#                 c = float(input("Nhập cạnh thứ 3 c = "))
#                 while (a > 0 and b > 0 and c > 0):
#                     module_TinhChuViVaDienTich.HinhTamGiac(a,b,c)
#                     break
#             elif shape_choice == 0:
#                 break
#             else:
#                 print("Hãy nhập lại !")
#     elif choice == 0:
#         break
#     else:
#         print("Xin mời nhập lại")



#Bài 7 (Thầy chữa)
import module_TongCacChuSo
import module_UocSo
import module_UocSoNguyenTo
import module_PhanTichThuaSoNguyenTo

n = int(input("Nhập số dương n = "))
if (n < 1):
    print("Nhập n không đúng")
else:
    print("Hãy chọn\
        [1] - Phân tích thừa số nguyên tố\
        [2] - Tổng chữ số\
        [3] - Ước số\
        [4] - Ước số nguyên tố\
        [0] - Thoát")
    while True:
        user_choice = int(input("Nhập lựa chọn: "))
        if user_choice == 1:
        elif user_choice == 2:
        elif user_choice == 3:
        elif user_choice == 4:
        elif user_choice == 0:
        else:
            print("Lựa chọn bạn nhập không đúng. Mời nhập lại")