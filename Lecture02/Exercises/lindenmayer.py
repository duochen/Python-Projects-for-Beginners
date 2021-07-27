# Lindenmayer systems
from turtle import *
from time import sleep
from math import sqrt

def replace( seq, repRules, n ):
    for i in range(n):
        newseq = ""
        for element in seq:
            newseq = newseq + repRules.get(element,element)
        seq = newseq
    return seq
def draw( commands, rules ):
    for x in commands:
        try:
            rules[x]()
        except TypeError:
            try:
                draw(rules[x], rules)
            except:
                pass

# Example 1: --------------------------------------
def r():
    right(45)
def l():
    left(45)
def f():
    forward(7.5)

rules1 = {"-":r, "+":l, "f":f, "g":"f+f+f--f--f+f+f"}
repRules1 = {"g": "g+f+g--f--g+f+g"}
start1 = "g--f--g--f"

reset()
speed(0)
tracer(3,0)
ht()
up()
backward(195)
down()
drawing = replace(start1, repRules1, 3)
draw(drawing, rules1)

sleep(3)

# Example 2: --------------------------------------
def a():
    color("red")
    circle(10,90)
def b():
    color("black")
    l = 5/sqrt(2)
    forward(l)
    circle(l, 270)
    forward(l)
def c():
    color("green")
    forward(10)

rules2 = {"-":a, "+":b, "c":c}
repRules2 = {"-" : "-c+c-", "+" : "-c+c+c+c-" }
start2 = "c+c+c+c+"

reset()
speed(0)
tracer(3,0)
ht()
left(45)
drawing = replace(start2, repRules2, 3)
draw(drawing, rules2)
