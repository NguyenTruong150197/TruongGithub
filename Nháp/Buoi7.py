import turtle

# window = turtle.Screen()
# window.bgcolor("black")
# window.title("Vẽ hình vuông")

# myPen = turtle.Turtle()
# myPen.speed(1)
# myPen.color("#FF0000")

# for i in range(4):
#     myPen.forward(100)
#     myPen.left(90)
    
# turtle.done()

# window = turtle.Screen()
# window.bgcolor("black")
# window.title("Vẽ ngôi sao lồng nhau")

# myPen = turtle.Turtle()
# myPen.speed(10)
# myPen.color("#FF0000")

# for j in range(1,100):
#     for i in range(1,6):
#         myPen.left(144)
#         myPen.forward(200)
#     myPen.left(5)

# turtle.done()


#Bài 1
# n = 5
# k = 5
# for i in range(0,n + 1):
#     for j in range(k - i,0,-1):
#         print(j,end=" ")
#     print()


#Bài 2
# list1 = [10, 20, 30, 40, 50]
# for i in reversed(list1):
#     print(i)


#Bài 3
# for i in range(-10,0):
#     print(i)
#     print()



#Bài 4
# def kiem_tra_so_nguyen_to(i):
#     flag = 1
#     if (i <2):
#         flag = 0
#         return flag
#     for p in range(2, i):
#         if i % p == 0:
#             flag = 0
#             break
#     return flag
# number = int(input("Nhập số bắt đầu: "))
# number2 = int(input("Nhập số kết thúc: "))
# print("Các số nguyên tố có trong khoảng là:")
# for i in range(number,number2):
#     if kiem_tra_so_nguyen_to(i) == 1:
#         print(i,end=" ")
        


#Bài 5
# for i in range(1,100):
#     if i % 7 == 0:
#         print(i,end=" ")



#Bài 6
# for i in range(300,2,-1):
#     if i % 3 == 0:
#         print(i,end=" ")



#Bài 7
# chuoi = str(input("Nhập chuỗi bất kì: "))
# sub = "a"
# chuoi1 = chuoi.count(sub)
# print('Số kí tự "a" xuất hiện trong chuỗi đã nhập là',chuoi1)



#Bài 8
# chuoi = str(input("Nhập chuỗi từ bàn phím: "))
# chuoi_so = ""
# for i in chuoi:
#     if i.isdigit():
#         chuoi_so += i
# so_luong_ky_tu_so = len(chuoi_so)
# print("Số lương ký tự số có trong chuỗi đã nhập là:",so_luong_ky_tu_so)



#Bài 9
# S = "Bai Tap Mon Lap Trinh Python"
# S1 = S.split()
# print(S1)



#Bài 10
# def kiem_tra_so_nguyen_to(n):
#     flag = 1
#     if (n <2):
#         flag = 0
#         return flag
#     for p in range(2, n):
#         if n % p == 0:
#             flag = 0
#             break
#     return flag
# n = int(input("Nhập số n cần kiểm tra: "))
# kiem_tra = kiem_tra_so_nguyen_to(n)
# if kiem_tra == 1:
#     print(n,"là số nguyen tố")
# else:
#     print(n,"không phải là số nguyên tố")