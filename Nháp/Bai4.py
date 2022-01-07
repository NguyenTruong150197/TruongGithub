import math
a = float(input("Nhập số a = "))
b = float(input("Nhập số b = "))
c = float(input("Nhập số c = "))

delta = b*b - 4*a*c
delta >=0
x1=float((-b + math.sqrt(delta))/(2*a))
x2=float((-b - math.sqrt(delta))/(2*a))
print("Phương trình có 2 nghiệm là x1= ",x1,"và x2 là: ",x2)