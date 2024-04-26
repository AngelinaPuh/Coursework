from tkinter import *
from  random import choice
SIZE = 4
frm = []; btn = []
playArea = list(range(1, SIZE*SIZE)) + [0]
class puzzle(Button):
    def __init__(self, number=0, parent=None, **config):
        self.number = number
        Button.__init__(self, parent, **config)
        self.pack(side=LEFT, expand=YES, fill=BOTH)
        self.config(font=('mono', 20, 'bold'), width=3, height=2, command=self.play)
    def play(self):
        m = playArea.index(0)
        if (abs(m - self.number) + abs(self.number//SIZE - m//SIZE)) == 1 or abs(m - self.number) == SIZE:
            playArea[m], playArea[self.number] = playArea[self.number], playArea[m]
            btn[m].config(text=playArea[m])
            self.config(text=" ")
for i in range(0, SIZE): 
    frm.append(Frame())
    frm[i].pack(expand=YES, fill=BOTH)
    for j in  range(0, SIZE):
        btn.append(puzzle((i*SIZE+j), frm[i]))
for i in range(0, SIZE**6):
    btn[choice(range(0, SIZE*SIZE))].play()
mainloop()