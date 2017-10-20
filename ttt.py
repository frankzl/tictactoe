from tkinter import *
from tkinter import font
top = Tk()

winCondition = 3

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

    btn = bArray[x][y]
    symbol = btn['text']

    for i in range(1, winCondition):
        winDirection[0] += (bArray[(x+i) % winCondition][y].cget('text') == symbol)
        winDirection[1] += (bArray[x][(y+i)%winCondition].cget('text') == symbol)
        winDirection[2] += (bArray[(x+i)%winCondition][(y+i)%winCondition].cget('text') == symbol)
        winDirection[3] += (bArray[(x-i)%winCondition][(y-i)%winCondition].cget('text') == symbol)
    win = max(winDirection) >= winCondition;
    print(winDirection)
    w['text'] = ('Player ' + symbol + ' WINS!') if win else 'TIC TAC TOE'
    return win;



def generateButtonArray():
    for i in range(3):
        bArray.append([])
        for j in range(3):
            btn = Button(top, font=f1, height=1, width=2, text=" ")
            btn.configure(command=lambda x=i, y=j: setMark(x,y))
            bArray[i].append(btn)
            bArray[i][j].grid(row=i, column=j)

generateButtonArray()

w = Label(top, font=f2, text="TIC TAC TOE")
w.grid(row=4, columnspan=3)


top.mainloop()
