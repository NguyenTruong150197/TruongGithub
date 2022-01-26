import random


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winer = None
gameRunning = True
# Module xây dựng bảng cờ ca rô
def printBoard(board):
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("-------------")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("-------------")
    print("|",board[6],"|",board[7],"|",board[8],"|")
# Module người chơi chọn nước đi từ 1-9 
def playerChoice(board):
    inp = int(input("Nhập nước muốn đi từ 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print("Bạn nhập nước đi không hợp lệ!")
# Check điều kiện thắng hàng ngang
def checkLine(board):
    global winer
    if board[0] == board[1] == board[2] and board[1] != "-":
        winer = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winer = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winer = board[6]
        return True
# Check điều kiện thắng hàng dọc    
def checkRow(board):
    global winer
    if board[0] == board[3] == board[6] and board[0] != "-":
        winer = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winer = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winer = board[2]
        return True
# Check diều kiện thắng hàng chéo    
def checkCross(board):
    global winer
    if board[0] == board[4] == board[8] and board[0] != "-":
        winer = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winer = board[2]
        return True
# Check điều kiện hòa   
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Hòa nhau")
        gameRunning = False
# Module check toàn bộ điều kiện thắng        
def checkWin():
    global gameRunning
    if checkLine(board) or checkRow(board) or checkCross(board):
        print(f"Bên {winer} dành chiến thắng")
        gameRunning = False
    
# Module để chuyển người chơi qua lại giữa O và X       
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
# Module để gán người chơi dấu O thành computer        
def computer(board):
    while currentPlayer == "O":
        computerChoice = random.randint(0, 8)
        if board[computerChoice] == "-":
            board[computerChoice] = "O"
            switchPlayer()
        
# Vòng lặp chạy game
while gameRunning:
    printBoard(board)
    playerChoice(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)