#a*x + b = 0
def GiaiPTBacNhat(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có nghiệm là:",-b/a)