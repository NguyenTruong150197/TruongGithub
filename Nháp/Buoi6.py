#Bài 1
#listNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# tongchan = 0
# tongle = 0
# for val in listNumber:
#     if val % 2 == 0:
#         tongchan += val
#     else:
#         tongle += val
# print("Tổng chẵn là {}, tổng lẻ là {}".format(tongchan,tongle))

#Bài 2
# listNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# tongcacso = 0
# for val in listNumber:
#     tongcacso += (val**2)
# print("Tổng bình phương các số trong list là:",tongcacso)

#Bài 3
# list = [4, 6, 0, 3, 34, 27, 19, 56, 48]
# tong_cac_so = 0
# Min = 0
# Max = 0
# for val in list:
#     tong_cac_so += val
#     if Min > val:
#         Min = val
#     if Max < val:
#         Max = val
# print("Số lớn nhất là", Max)
# print("Số bé nhất là",Min)
# print("Tổng các số là",tong_cac_so)

#Bài 4
# n = 5
# k = 5
# for i in range(0, n + 1):
#     for j in range(k - i, 0, - 1):
#         print(j, end=" ")
#     print()

#Bài 5
# so_dau = int(input("Nhập số đầu: "))
# so_cuoi = int(input("Nhập số cuối: "))
# if so_dau > so_cuoi:
#     print("Số kết thúc cần lớn hơn số bắt đầu")
# else:
#     for i in range(so_dau,so_cuoi + 1):
#         if i % 3 == 0 and i % 5 != 0:
#             print("Fizz")
#         elif i % 5 == 0 and i % 3 != 0:
#             print("Buzz")
#         elif i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         else:
#             print(i)

#Bài 6
import random
while True:
    current_number = 0
    if random.randint(0,1) == 0:
        current_player = "human"
    else:
        current_player = "computer"
    while current_number <= 21:
        print("Số điểm tổng hiện tại là",current_number)
        print()
        if current_player == "human":
            print("Hãy nhập thêm 1, 2 hoặc 3 vào. Đừng để số điểm tổng lớn hơn 21")
            player_choice = ""
            while player_choice not in [1, 2, 3]:
                player_choice = int(input("Nhập số điểm muốn thêm vào điểm tổng: "))
                current_number += player_choice
                print()
                if current_number >= 21:
                    print("Số điểm tổng hiện tại là:",current_number)
                    print()
                    print("Bạn đã thua")
                    break
                current_player = "computer"
        else:
            computer_choice = random.randint(1,3)
            current_number += computer_choice
            print("Đang là lượt của máy tính. Máy tính sẽ chọn thêm",computer_choice,"điểm")
            print()
            if current_number >= 21:
                print("Điểm tổng hiện tại là:",current_number)
                print()
                print("Bạn đã dành chiến thắng")
                break
            current_player = "human"
    print()
    play_again = input("Bạn có muốn chơi tiếp không? ")
    if play_again.lower().startswith("y"):
        continue
    else:
        print("Cám ơn bạn đã chơi game")
        break