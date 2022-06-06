# FILE NAME: TicTacToe.py
# 
# FILE DISCRIPTION:
# code for handling tic tac toe game using the GUI
# 
# 
# FILE AUTHOT:  Sneh Mistry
# DATE: May 25, 2022
# VERSION: 1.0.00


import turtle as tr
import tkinter as tk
import board as b
import random as r
import fire as f

def tic_tac_toe():
    global sc, arr, count, nextPlayer, player, player1, player2
    sc = b.set_screen()
    arr = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    count = 0
    nextPlayer = {
        "name" : "",
        "symbol" : 1,
        "score" : 0
    }
    player = {
        "name" : "",
        "symbol" : 0,
        "score" : 0
    }
    player1 = {
        "name" : "",
        "symbol" : 0,
        "score" : 0
    }
    player2 = {
        "name" : "",
        "symbol" : 0,
        "score" : 0
    }
    # Setup player 1 and playe 2's setup will be 
    # handled in the click event
    setup_player1()
    tr.mainloop()


# Choose the first player
def choose_first():
    global player1, player2
    ran = r.randint(0,1)
    if not ran:
        temp = player1
        player1 = player2
        player2 = temp

# check the result 
def checkResult():
    global arr
    if (arr[0][0] == arr[0][1] == arr[0][2]) and arr[0][0] != " ":
        return 1
    elif (arr[1][0] == arr[1][1] == arr[1][2]) and arr[1][0] != " ":
        return 2
    elif (arr[2][0] == arr[2][1] == arr[2][2]) and arr[2][0] != " ":
        return 3
    elif (arr[0][0] == arr[1][0] == arr[2][0]) and arr[0][0] != " ":
        return 4
    elif (arr[0][1] == arr[1][1] == arr[2][1]) and arr[0][1] != " ":
        return 5
    elif (arr[0][2] == arr[1][2] == arr[2][2]) and arr[0][2] != " ":
        return 6
    elif (arr[0][0] == arr[1][1] == arr[2][2]) and arr[0][0] != " ":
        return 7
    elif (arr[0][2] == arr[1][1] == arr[2][0]) and arr[0][2] != " ":
        return 8
    else:
        # Check for the match draw or not
        space = 9
        for row in arr:
            for mark in row:
                if mark != " ":
                    space -= 1
        if not space:
            return 9
    return 0

# Update the player's turn
def updatePlayerTurn():
    global player, nextPlayer, count
    count += 1
    if count%2:
        player = player1
        nextPlayer = player2
    else:
        player = player2
        nextPlayer = player1

# Play the game
def play(x,y):
    global arr, eraseble, fireStop, player1, player2, player, score
    # Disable the event handler until the decision made
    sc.onclick(None)

    # calculate the cordinates according the board size
    j = (y+5)//2 - 2
    i = (x+5)//2 - 2

    if abs(i)>1 or abs(j)>1 or (arr[int(i)+1][1-int(j)] in [0,1]):
        # Skip if click is out side the board or 
        #         clicked on the occupied space
        pass
    else:
        # Genuine move has been played
        
        # Update the player turn
        updatePlayerTurn()

        arr[int(i)+1][1-int(j)] = player["symbol"]
        b.drw_symbol(player["symbol"], 2*i, 2*j)
        
        style = ("Arial", 20)
        # Check the result after every play
        res = checkResult()

        # If match draw or any player wins
        if res:
            eraseble.clear()

            if res != 9:
                if player == player1:
                    player1["score"] += 1
                    player = player1
                else:
                    player2["score"] += 1
                    player = player2
                # Player win the game
                b.set_string(f"{player['name']} Won", 0, 3.3, "white smoke", ('Chiller', 30, 'normal'))
                # eraseble = erasableWrite(tr, f"※ {player['name']} Won ※", font= style, align="center", color="cyan")
                score.clear()
                score = erasableWrite(tscore, f"{player1['name']} = {player1['score']}\n{player2['name']} = {player2['score']}",
                            font=("Arial", 15), align="center")
                b.drw_result(res)
            else:
                # Match draw
                
                b.set_string("Match Draw", 0, 3.3, "white smoke", ('Chiller', 30, 'normal'))
                # eraseble = erasableWrite(tr, "Match Draw", font= style, align="center", color="cyan")

            fireStop = 0
            # Runs until any click event has been occured
            while not fireStop:
                # If match is not draw, set the fire
                if res != 9:
                    f.fire()
                else:
                    f.move()
            # eraseble.clear()
            sc.reset()
            beginGame()

        # Update the next players turn
        eraseble.clear()
        eraseble = erasableWrite(tr, "{}'s turn".format(nextPlayer['name']), font=style, align="center")
    # Reinitialise the event handler as decision has been made
    sc.onclick(play)
    
# Erasable wrtie function
def erasableWrite(tortoise, name, font, align, reuse=None, color="grey"):
    eraser = tr.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.color(color)
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser

# collect the player1 info
def setup_player1():
    global player1
    sc.reset()
    tr.up()
    tr.ht()
    # set the game title
    b.set_string("TIC TAC TOE", 0, 4.2, "hot pink", ('Chiller', 30, 'bold'))
    # Ask for the player names
    while not player1['name'] or player1["name"].isspace():
        player1["name"] = tr.textinput("Welcome", "Player 1 name :")
    drw_symbol_selection_board()

# collect the player2 info
def setup_player2():
    global player2
    tr.hideturtle()
    tr.up()
    # set the game title
    b.set_string("TIC TAC TOE", 0, 4.2, "hot pink", ('Chiller', 33, 'bold'))
    # Ask for the player names
    while not player2['name'] or player2["name"].isspace():
        player2["name"] = tr.textinput("Welcome", "Player 2 name :") 
    drw_symbol_selection_board(player1["symbol"])

# Begin te game 
def beginGame():
    global eraseble, count, arr, player, nextPlayer, score, tscore
    count = 0           
    arr = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    canvas = sc.getcanvas()
    btn_restart = tk.Button(canvas.master, text="R E S T A R T", fg="hot pink", bg="black", command=restart)
    canvas.create_window(190,  -295, height=30, width=75 , window=btn_restart)

    canvas = sc.getcanvas()
    btn_quit = tk.Button(canvas.master, text="Q U I T", fg="hot pink", bg="black", command=quit)
    canvas.create_window(265,  -295, height=30, width=60 , window=btn_quit)

    canvas = sc.getcanvas()
    btn_home = tk.Button(canvas.master, text="H O M E", fg="hot pink", bg="black", command=home)
    canvas.create_window(-265,  -295, height=30, width=60 , window=btn_home)

    canvas = sc.getcanvas()
    btn_reset = tk.Button(canvas.master, text="R E S E T", fg="hot pink", bg="black", command=reset)
    canvas.create_window(-200,  -295, height=30, width=60 , window=btn_reset)

    choose_first()
    # Draw the empty board
    player = player2
    nextPlayer = player1
    tr.hideturtle()
    b.set_string("TIC TAC TOE", 0, 4.2, "hot pink", ('Chiller', 33, 'bold'))
    b.drw_board()
    sc.onclick(play)
    tr.up()
    tr.goto(0,3.4)
    tr.down()
    eraseble = erasableWrite(tr, f"{nextPlayer['name']}'s turn", font=("Arial", 20), align="center")
    tscore = tr.Turtle()
    tscore.ht()
    tscore.up()
    tscore.goto(0,-4)
    tscore.down()
    score = erasableWrite(tscore, f"{player1['name']} = {player1['score']}\n{player2['name']} = {player2['score']}",
                            font=("Arial", 15), align="center")
    

def drw_symbol_selection_board(occupiedSymbol = 0):
    sc.onclick(None)
    if occupiedSymbol != 1:
        b.drw_circle(-2, 0)
    if occupiedSymbol != 2:
        b.drw_triangle(0, 0)
    if occupiedSymbol != 3:
        b.drw_square(2, 0)
    if occupiedSymbol != 4:
        b.drw_x(-2, -2)
    if occupiedSymbol != 5:
        b.drw_heart(0, -2)
    if occupiedSymbol != 6:
        b.drw_star(2, -2)
    sc.onclick(select_symbol)

def select_symbol(x,y):
    global count, button
    sc.onclick(None)
    # calculate the cordinates according the board size
    i = (x+5)//2 - 2
    j = (y+5)//2 - 2

    if abs(i)>1 or abs(j)>1 or j==1:
        # Skip if click is out side the board
        pass
    else:
        sym = 1
        if (i,j) == (-1,0):
            sym = 1
        elif (i,j) == (0,0):
            sym = 2
        elif (i,j) == (1,0):
            sym = 3
        elif (i,j) == (-1,-1):
            sym = 4
        elif (i,j) == (0,-1):
            sym = 5
        elif (i,j) == (1,-1):
            sym = 6
        if count == 0:
            player1["symbol"] = sym
            count += 1
            sc.reset()
            setup_player2()
        else:
            if sym != player1["symbol"]:
                player2["symbol"] = sym
                count = 0
                sc.reset()
                canvas = sc.getcanvas()
                button = tk.Button(canvas.master, fg="hot pink", bg="black",
                                    text="L E T ' S  P L A Y", font=("Chiller", 20), command=press)
                canvas.create_window(0,  0, height=50, width=200 , window=button)


# Button definition
def press():
    button.destroy()
    beginGame()

def restart():
    global fireStop
    res = checkResult()
    if res == 0:
        eraseble.clear()
        sc.reset()
        beginGame()
    else:
        fireStop = 1

def quit():
    tr.bye()

def home():
    tic_tac_toe()

def reset():
    global player1, player2
    player1["score"] = 0
    player2["score"] = 0
    restart()

if __name__ == '__main__':
    tic_tac_toe()