import random


board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def show_board(x1, x2, x3):
    print("|",board[x1],"|",board[x2],"|",board[x3],"|")
    print("-------------")
    
def print_board():
    show_board(1, 2, 3)
    show_board(4, 5, 6)
    show_board(7, 8, 9)

def con_o_trong():
    for i in range(1, 10):
        if board[i] != "x" and board[i] != "o":
            return True

def check_line(ch, x1, x2, x3):
    if board[x1] == ch and board[x2] == ch and board[x3] == ch:
        return True
    return False

def check_all(ch):
    if check_line(ch, 1, 2, 3):
        return True
    if check_line(ch, 1, 5, 9):
        return True
    if check_line(ch, 1, 4, 7):
        return True
    if check_line(ch, 2, 5, 8):
        return True
    if check_line(ch, 3, 5, 7):
        return True
    if check_line(ch, 3, 6, 9):
        return True
    if check_line(ch, 4, 5, 6):
        return True
    if check_line(ch, 7, 8, 9):
        return True
    return False
    
print("Chào mừng bạn chơi cờ ca rô 3x3")
print_board()
win = 0
while con_o_trong():
    nuoc_di = int(input("Mời nhập số muốn đi vào (1-9): "))
    if board[nuoc_di] == "x" or board[nuoc_di] == "o":
        print("Ô này đã được điền rồi")
    else:
        board[nuoc_di] = "x"
        while con_o_trong():
            computer = random.randint(1, 9)
            if board[computer] == "x" or board[computer] == "o":
                pass
            else:
                board[computer] = "o"
                break
    print_board()
    if check_all("x"):
        win = "Bạn"
        break
    
    if check_all("o"):
        win = "Máy tính"
        break
    
if win == 0:
    print("Hoà nhau")
else:
    print(win,"dành chiến thắng")  