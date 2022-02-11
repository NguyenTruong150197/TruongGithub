# dept_db = {
#  101 : 'HRD',
#  102 : 'FINANCE',
#  103 : 'ACCOUNTS',
#  104 : 'SALES',
#  105 : 'ENGINEERING',
#  106 : 'SUPPORT'
#  }
# employee_db = {
# 1000: dict(name="Alex", doj='01-10-89',dept=103),
# 1001: dict(name="Mary", doj='01-11-88', dept=101),
# 1002: dict(name="John", doj='01-10-87', dept=104),
# 1003: dict(name="David", doj='01-06-89', dept=105),
# 1004: dict(name="Anne", doj='01-01-86', dept=106),
# 1005: dict(name="Samson", doj='01-02-89', dept=101)
# }

# def get_employee_info(emp_id):
#     if emp_id in employee_db:
#         return employee_db[emp_id]
#     else:
#         print(emp_id,"Employee doesn`t exist")
#         return
    
# def get_department_info(dept_id):
#     if dept_id in dept_db:
#         return dept_db[dept_id]
#     else:
#         print(dept_id,"Department doesn`t exist")
#         return
    
# def display_emp_data(emp_data):
#     for key, value in emp_data.items():
#         if key == "dept":
#             print(key,":",get_department_info(value))
#         else:
#             print(key,":",value)
            
# emp_id = int(input("Please enter Employee ID: "))

# emp_data = get_employee_info(emp_id)

# if emp_data:
#     display_emp_data(emp_data)


# products = {
#  'SMART WATCH': 550,
#  'PHONE' : 1000,
#  'PLAYSTATION': 500,
#  'LAPTOP' : 1550,
#  'MUSIC PLAYER' : 600,
#  'TABLET' : 400
#  }

# def display_product(product_from_db, price):
#     for item in product_from_db:
#         if product_from_db[item] <= price:
#             print(item,":",product_from_db[item])
            
# input_price = int(input("Enter the price: "))

# display_product()



# dictionary = {"hello":"Xin chào",
#               "school":"Trường học",
#               "table":"Cái bàn",
#               "student":"Học sinh",
#               "class":"Lớp học"
#               }

# user_input = input("Nhập từ cần tra cứu: ")
# if user_input in dictionary.keys():
#     result = dictionary[user_input]
#     print(f"Nghĩa của từ {user_input} là: {result}")
# else:
#     print(f"Không tìm thấy từ {user_input} trong từ điển")



my_list = {1:"Apple",
           2:"Banana",
           3:"Orange",
           4:"Melon",
           5:"Coconut"}

def display_list():
    print("Danh sách sản phẩm: ")
    for key, value in my_list.items():
        print(key,":",value)
        
