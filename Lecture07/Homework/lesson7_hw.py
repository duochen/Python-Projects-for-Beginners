from turtle import *
from random import choice

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*1.5, 2) 
        self.fillcolor(n/dn, 0, 1-n/dn)
        self.st()
        self.speed(dn)

class Tower(list):
    def __init__(self, x):
        self.x = x
    def push(self, d):       
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)     
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, t):
    global move
    if n > 0:
        f=pos[n-1]
        if f!=t:
            w=[i for i in [T1,T2,T3] if i!=f and i!=t][0]
            hanoi(n-1, w)
            t.push(f.pop())
            pos[n-1]=t
            move += 1
            c.clear()
            c.write(f"{move} moves", align="center", font=("Courier", 16, "bold"))   
        hanoi(n-1, t)
             
def play():
    onkey(None,"space")
    clear()
    write("from\t\t   with   \t\tto", align="center", font=("Courier", 16, "bold"))
    try:
        hanoi(dn, T2)
    except Terminator:
        pass  

def init(n):
    global T1, T2, T3, pos
    T1 = Tower(-250); T2 = Tower(0); T3 = Tower(250)
    pos=[]
    for i in range(n,0,-1):
        pos.append(choice([T1,T2,T3]))
        pos[n-i].push(Disc(i))
    pos.reverse()

ht(); up(); goto(0, -200)
c=Turtle()
c.ht(); c.up(); c.goto(0,-250)
move = 0
dn=6
init(dn)
write("press spacebar to start game", align="center", font=("Courier", 16, "bold"))
onkey(play, "space")
listen()
