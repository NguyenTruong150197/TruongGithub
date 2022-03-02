# Bài 1
# import turtle
# import math


# class Circle:
#     def __init__(self, r, x, y):
#         """
#             Khởi tạo các tham số 
#             r : là bán kính
#             x : là hoành độ của tâm hình tròn
#             y : là tung độ của tâm hình tròn
#         """
#         self.r = r
#         self.x = x
#         self.y = y
        
#     def draw(self):
#         """
#             Phương thức vẽ hình tròn
#         """
#         obj = turtle.Turtle()
#         obj.hideturtle()
#         obj.penup()
#         obj.goto(self.x, self.y)
#         obj.pendown()
#         obj.circle(self.r)
        
#     def area(self):
#         """
#             Phương thức tính diện tích hình tròn
#         """
#         return math.pi*(self.r**2)
    
#     def perimeter(self):
#         """
#             Phương thức tính chu vi hình tròn
#         """
#         return 2*math.pi*self.r
    
    
# c = Circle(100, 0, 0)
# c.draw()
# print("Diện tích hình tròn là:",c.area())
# print("Chu vi hình tròn là:",c.perimeter())



# Bài 2 ()
# import random


# class Flashcard:
#     lst = ["Ngôi nhà", "Tiếng anh", "Cái bàn"]
#     lst1 = lst[random.randint(0,2)]
#     def __init__(self):
#         """
#             Phương thức hiện thị từ tiếng việt
#         """
#         print("Từ cần dịch là:",self.lst1)
    
#     def input1(self):
#         self.write = input("Nhập từ dịch vào: ")
        
#     def translate(self):
#         if self.lst1 == "Ngôi nhà":
#             if self.write == "home" or self.write == "Home":
#                 print("Bạn đã đúng")
#             else:
#                 print("Bạn đã sai")
#         elif self.lst1 == "Tiếng anh":
#             if self.write == "english" or self.write == "English":
#                 print("Bạn đã đúng")
#             else:
#                 print("Bạn đã sai")
#         else:
#             if self.write == "table" or self.write == "Table":
#                 print("Bạn đã đúng")
#             else:
#                 print("Bạn đã sai")
                
# q = Flashcard()
# q.input1()
# q.translate()



# Bài 3 (Thầy đã làm nhưng chưa chép xong)
# import turtle
# import datetime
# import math


# screen = turtle.Screen()
# screen.title("Draw Clock")
# screen.bgcolor("sky blue")
# screen.setup(1000, 1000)
# screen.setworldcoordinates(-1000, -1000, 1000, 1000)
# screen.tracer(0, 0)

# class Clock:
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#         self.microsecond = 0
#         self.face = turtle.Turtle()
#         self.hand = turtle.Turtle()
#         self.face.hideturtle()
#         self.hand.hideturtle()


# Bài 4
class Student:
    def __init__(self, studentpass, name, dateofbirth, address, specialized, grade):
        self.studentpass = studentpass
        self.name = name
        self.dateofbirth = dateofbirth
        self.address = address
        self.specialized = specialized
        self.grade = grade
        
    def 