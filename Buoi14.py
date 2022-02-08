# Bài 1

# word = 'brontosaurus'
# dict_1 = {}
# for i in word:
#     dict_1[i] = word.count(i)
# print(dict_1)



# Bài 2

# f = open(r"C:\Users\Administrator.DESKTOP-2022LYM\TruongGithub\romeo.txt")
# r = f.read()
# dict_1 = {}
# for i in r:
#     dict_1[i] = r.count(i)
# print(dict_1)



# Bài 3

dept_db = {
101 : 'HRD',
102 : 'FINANCE',
103 : 'ACCOUNTS',
104 : 'SALES',
105 : 'ENGINEERING',
106 : 'SUPPORT'}

employee_db = {
1000: dict(name="Alex",   doj='01-10-89',dept=103),
1001: dict(name="Mary",   doj='01-11-88', dept=101),
1002: dict(name="John",   doj='01-10-87', dept=104),
1003: dict(name="David",  doj='01-06-89', dept=105),
1004: dict(name="Anne",   doj='01-01-86', dept=106),
1005: dict(name="Samson", doj='01-02-89', dept=101)}

def input_number(number):
      if number in employee_db:
            return(employee_db[number])
      else:
            print("Số nhập vào không hợp lệ!")
            return
            
def dept_info(dept_number):
      if dept_number in dept_db:
            return(dept_db[dept_number])
      else:
            print("Không có giá trị này!")
            return
            
