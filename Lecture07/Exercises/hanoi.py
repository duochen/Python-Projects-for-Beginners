from turtle import *

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

def count():
    global move
    move += 1
    c.clear()
    c.write(f"{move} moves", align="center", font=("Courier", 16, "bold"))
    
def hanoi(n, f, w, t):
    if n > 0:       
        hanoi(n-1, f, t, w)
        t.push(f.pop())
        count()
        hanoi(n-1, w, f, t)

def play():
    onkey(None,"space")
    clear()
    write("from\t\t   with   \t\tto", align="center", font=("Courier", 16, "bold"))
    try:
        hanoi(dn, T1, T2, T3)
    except Terminator:
        pass

def init(n):
    global T1, T2, T3
    T1 = Tower(-250); T2 = Tower(0); T3 = Tower(250)
    for i in range(n,0,-1):
        T1.push(Disc(i))

ht(); up(); goto(0, -200)
c=Turtle()
c.ht(); c.up(); c.goto(0,-250)
move = 0
dn=6
init(dn)
write("press spacebar to start game", align="center", font=("Courier", 16, "bold"))
onkey(play, "space")
listen()
