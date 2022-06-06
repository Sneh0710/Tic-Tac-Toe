import os
os.system("")
namePlayer1, namePlayer2 = "",""
arr = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],
]
def clearScreen():
    print("\x1b[2J")
    print("\x1b[1;1H")

def goto(x,y):
    print(f"\x1b[{x};{y}H",end='')

def beginScreen():
    # print("\x1b[1;0mTIC TAC TOE")
    global namePlayer1, namePlayer2
    namePlayer1 = input("Enter player 1's name = ")
    namePlayer2 = input("Enter player 2's name = ")
    print(f"Welcome to the game {namePlayer1} and {namePlayer2}")

def printGameBoard():
    print(f"{arr[0][0]} | {arr[0][1]} | {arr[0][2]}")
    print("--+---+--")
    print(f"{arr[1][0]} | {arr[1][1]} | {arr[1][2]}")
    print("--+---+--")
    print(f"{arr[2][0]} | {arr[2][1]} | {arr[2][2]}")

def checkResult():
    return (
        ((arr[0][0] == arr[0][1] == arr[0][2]) and arr[0][0] != " ") or
        ((arr[1][0] == arr[1][1] == arr[1][2]) and arr[1][0] != " ") or
        ((arr[2][0] == arr[2][1] == arr[2][2]) and arr[2][0] != " ") or
        ((arr[0][0] == arr[1][0] == arr[2][0]) and arr[0][0] != " ") or
        ((arr[0][1] == arr[1][1] == arr[2][1]) and arr[0][1] != " ") or
        ((arr[0][2] == arr[1][2] == arr[2][2]) and arr[0][2] != " ") or
        ((arr[0][0] == arr[1][1] == arr[2][2]) and arr[0][0] != " ") or
        ((arr[0][2] == arr[1][1] == arr[2][0]) and arr[0][2] != " ")
    )

clearScreen()
beginScreen()
count = 0
while True:
    clearScreen()
    printGameBoard()
    count += 1
    if count%2:
        player = namePlayer1
    else:
        player = namePlayer2
    ch = int(input(f"{player} : Enter choice [1-9] = "))
    if not 1<=ch<=9:
        count -= 1
        continue
    if count%2:
        arr[(ch-1)//3][ch%3-1] = "X"
    else:
        arr[(ch-1)//3][ch%3-1] = "O"   
    if checkResult():
        clearScreen()
        printGameBoard()
        print(f"{player} WON")
        print("\7")
        break
        
