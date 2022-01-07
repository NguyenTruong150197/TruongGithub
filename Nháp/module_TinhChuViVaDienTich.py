#Hình tròn
import math

def HnhTron(r):
    print("Chu vi hình tròn là:",2*math.pi*r)
    print("Diện tích hình tròn là:",math.pi*r*r)
    
#Hình chữ nhật
def HinhChuNhat(a,b):
    print("Chu vi hình chữ nhật là:",2*(a + b))
    print("Diện tích hình chữ nhật là:",a*b)
    
#Hình tam giác
def HinhTamGiac(a,b,c):
    if (a + b) > c and (b + c) > a and (c + a) > b:
        p = (a + b +c)/2
        s = math.sqrt(p*(p - a)*(p - b)*(p - c))
        print("Chu vi tam giác là:",p)
        print("Diện tích tam giác là:",s)
    else:
        print("Không phải 3 cạnh của tam giác")