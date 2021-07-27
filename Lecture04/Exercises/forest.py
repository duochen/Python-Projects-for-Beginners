from turtle import Turtle, colormode, tracer
from random import randrange as rr

def randomize(blist, adist, sdist):
    return [(angle+rr(-adist,adist+1),sfactor*1.01**rr(-sdist,sdist+1)) for angle, sfactor in blist]

def randomfd(t, dist, parts, adist):
    for i in range(parts):
        t.left(rr(-adist,adist+1))
        t.forward(dist/parts)

def start(t,x,y):
    colormode(255)
    t.reset()
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.penup()
    t.setpos(x,y)
    t.pendown()

def tree(tlist, size, level, wfactor, blists, adist=10, sdist=5):
    if level > 0:
        lst = []
        brs = []
        for t, blist in list(zip(tlist,blists)):
            t.pensize(size * wfactor)
            t.pencolor(255 - (180 - 11 * level + rr(-15,16)),  180 - 11 * level + rr(-15,16),  0)
            t.pendown()
            randomfd(t, size, level, adist)
            yield 1
            for angle, sfactor in blist:
                t.left(angle)
                lst.append(t.clone())
                brs.append(randomize(blist, adist, sdist))
                t.right(angle)
        for x in tree(lst, size*sfactor, level-1, wfactor, brs,  adist, sdist):
            yield None

def doit1(level, pen):
    pen.hideturtle()
    start(pen, 20, -208)
    t = tree([pen], 80, level, 0.1, [[(45,0.69), (0,0.65), (-45,0.71)]])
    return t

def doit2(level, pen):
    pen.hideturtle()
    start(pen, -135, -130)
    t = tree([pen], 120, level, 0.1, [[(45,0.69), (-45,0.71)]])
    return t

def doit3(level, pen):
    pen.hideturtle()
    start(pen, 190, -90)
    t = tree([pen], 100, level, 0.1, [[(45,0.7), (0,0.72), (-45,0.65)]])
    return t

p = Turtle()
p.ht()
tracer(75,0)
u = doit1(6, Turtle(undobuffersize=1))
s = doit2(7, Turtle(undobuffersize=1))
t = doit3(5, Turtle(undobuffersize=1))

while True:
    done = 0
    for b in u,s,t:
        try:
            b.__next__()
        except:
            done += 1
    if done == 3:
        break
