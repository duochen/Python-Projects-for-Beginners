from turtle import Turtle, colormode, tracer
from random import randrange as rr

def randomize(blist, adist, sdist):
    return [(angle+rr(-adist,adist+1),sfactor*1.01**rr(-sdist,sdist+1)) for angle, sfactor in blist]

def randomfd(t, dist, segs, adist):
    for i in range(segs):
        t.left(rr(-adist,adist+1))
        t.forward(dist/segs)

def start(t,x,y):
    colormode(255)
    t.ht()
    t.speed(0)
    t.left(90)
    t.up()
    t.setpos(x,y)
    t.down()

def tree(tlist, size, level, wfactor, blists, adist=10, sdist=5):
    if level > 0:
        for t, blist in list(zip(tlist,blists)):
            lst = []
            brs = []
            t.width(size * wfactor)
            t.color(255 - (180 - 11 * level + rr(-15,16)),  180 - 11 * level + rr(-15,16),  0)
            randomfd(t, size, level, adist)
            yield None
            for angle, sfactor in blist:
                t.left(angle)
                lst.append(t.clone())
                brs.append(randomize(blist, adist, sdist))
                t.right(angle)
            for x in tree(lst, size*sfactor, level-1, wfactor, brs,  adist, sdist):
                yield None

tracer(75,0)
a,b,c=Turtle(),Turtle(),Turtle()
start(a, 20, -208)
u=tree([a], 80, 6, 0.1, [[(45,0.69), (0,0.65), (-45,0.71)]])
start(b, -135, -130)
v=tree([b], 120,7, 0.1, [[(45,0.69), (-45,0.71)]])
start(c, 190, -90)
w=tree([c], 100, 5, 0.1, [[(45,0.7), (0,0.72), (-45,0.65)]])

while True:
    done = 0
    for tr in u,v,w:
        try:
            next(tr)
        except:
            done += 1
    if done == 3:
        break
