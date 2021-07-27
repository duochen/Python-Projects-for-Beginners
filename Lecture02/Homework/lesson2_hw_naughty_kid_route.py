from turtle import *
from time import sleep
global level

def replace( seq, repRules, n ):
    for i in range(n):
        newseq = ""
        for element in seq:
            newseq = newseq + repRules.get(element,element)
        seq = newseq
    return seq
def draw( commands, rules ):
    for x in commands:
            rules[x]()

def r():
    right(45)
def l():
    left(90)
def f():
    forward(200/2**(level/2))

rules1 = {"r":r, "l":l, "f":f}
repRules1 = {"f": "rflfr"}
start1 = "f"

speed(0)

for level in range(13):
    tracer(16381,0)
    reset()
    ht()
    up()
    sety(100)
    down()
    seth(270)
    drawing = replace(start1, repRules1, level)
    draw(drawing, rules1)
    sleep(1)
