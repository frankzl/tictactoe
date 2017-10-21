from tkinter import *
from tkinter import font
top = Tk()

# MODIFY THESE TWO VALUES
winCondition = 4
fieldSize = 5

turn = True;
f1 = font.Font(family='Helvetica', size=70, weight='bold')
f2 = font.Font(family='Helvetica', size=20, weight='bold')

bArray = []

def setMark(x,y):
    print("yo" + str(x) + ';' + str(y))
    btn = bArray[x][y];
    global turn
    btn['text'] = 'X' if turn else 'O';
    turn = not turn;
    isGameOver(x,y);


def isGameOver(x,y):

    winDirection = [1,1,1,1]
    reverseShift = [0, 0, 0, 0]

    btn = bArray[x][y]
    symbol = btn['text']

    for i in range(1, winCondition):
        winDirection[0] += checkField((x+i) % winCondition,y)
        winDirection[1] += checkField(x,(y+i)%winCondition)
        winDirection[2] += checkField((x+i)%winCondition,(y+i)%winCondition)
        winDirection[3] += checkField((x-i)%winCondition,(y+i)%winCondition)
    win = max(winDirection) >= winCondition;
    print(winDirection)
    w['text'] = ('Player ' + symbol + ' WINS!') if win else 'TIC TAC TOE'
    return win;



def getShiftValue(steps):
    return winCondition - steps;

def checkField(x,y, symbol):
    return bArray[x][y].cget('text') == symbol

def generateButtonArray():
    for i in range(fieldSize):
        bArray.append([])
        for j in range(fieldSize):
            btn = Button(top, font=f1, height=1, width=2, text=" ")
            btn.configure(command=lambda x=i, y=j: setMark(x,y))
            bArray[i].append(btn)
            bArray[i][j].grid(row=i, column=j)

generateButtonArray()

w = Label(top, font=f2, text="TIC TAC TOE")
w.grid(row=fieldSize+1, columnspan=fieldSize)


top.mainloop()
