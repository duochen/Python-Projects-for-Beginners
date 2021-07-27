from turtle import Turtle
def tree(plist, l, a, f):
    if l > 2:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        for x in tree(lst, l*f, a, f):
            yield None

p = Turtle()
p.setundobuffer(None)
p.hideturtle()
p.speed(1)
p.getscreen().tracer(1,0)
p.left(90)
p.penup()
p.forward(-200)
p.pendown()
t = tree([p], 200, 60, 0.618)
for x in t:
    pass
