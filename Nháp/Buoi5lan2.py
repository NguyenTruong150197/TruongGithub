#Bài 1
# ds = 95.5
# y = 2017
# tl = 0.012
# while ds <= 150:
#     y += 1
#     ds += (ds*tl)
# print("Đến năm {} thì dân số đạt 150tr người".format(y))



#Bài 2
# number = int(input("Nhập số thập phân vào: "))
# ds = ""
# while number != 0:
#     ds += str(number % 2)
#     number //= 2
# ds1 = ds[::-1]
# print(ds1)



#Bài 3
# number = int(input("Nhập số: "))
# tong = 0
# while number > 0:
#     tong = tong + number%10
#     number = int(number/10)
# print("Tổng các chữ số là:",tong)



#Bài 4
# n = int(input("Nhập số cần đảo ngược vào: "))
# ds = ""
# while n != 0:
#     ds += str(n % 10)
#     n = n // 10
# print("Số đã đảo ngược là:",ds)



#Bài 5
# n = 0
# mark = "*"
# while n < 4:
#     print(mark)
#     n += 1
#     mark += " *"