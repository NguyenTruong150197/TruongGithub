#a*x^2 + b*x + c = 0
import math

def GiaiPTBacHai(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm")
            else:
                print("Phương trình vô nghiệm")
        else:
            print("Phương trình có 1 nghiệm duy nhất là:",-c/b)
    else:
        delta = b*b - 4*a*c
        if delta == 0:
            print("Phương trình có nghiệm kép là:",-b/(2*a))
        elif delta > 0:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print("Phương trình có 2 nghiệm là:",x1,x2)
        else:
            print("Phương trình vô nghiệm")