from turtle import Turtle

def tree(plist, l, a, f):
    if l > 0.5:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            r = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
            lst.append(r)
        for x in tree(lst, l*f, a, f):
            yield None

def maketree():
    p = Turtle()
    p.setundobuffer(None)
    p.hideturtle()
    p.speed(0)
    p.getscreen().tracer(1000,0)
    p.getscreen().bgcolor('black')
    p.color('white')
    p.left(90)
    p.penup()
    p.forward(-200)
    p.pendown()
    t = tree([p], 200, 120, 0.5)
    for x in t:
        pass

maketree()
