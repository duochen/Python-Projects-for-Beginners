from turtle import *
import random

class Book(Turtle):
    def __init__(self, size):
        self.size = size
        Turtle.__init__(self, shape="square", visible=False)
        self.up()
        self.shapesize(size *15/n, 1.5, 2) 
        self.fillcolor("black")
        self.st()
    def glow(self):
        self.fillcolor("red")
    def unglow(self):
        self.fillcolor("black")

class Shelf(list):
    def __init__(self, n, y):  
        self.y = y
        self.x = -17*n
    def closeigap(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos - 34)
    def openigap(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos + 34)
    def push(self, b):
        width, _, _ = b.shapesize()
        y_offset = width / 2 * 20 
        b.sety(self.y + y_offset)
        b.setx(self.x + 34 * len(self))
        self.append(b) 
    def pop(self, key):
        b = list.pop(self, key)
        b.glow()
        b.sety(200)
        self.closeigap(key)
        return b
    def insert(self, key, b):
        self.openigap(key)
        list.insert(self, key, b)
        b.setx(self.x + 34 * key)
        width, _, _ = b.shapesize()
        y_offset = width / 2 * 20
        b.sety(self.y + y_offset)
        b.unglow()

def isort():
    disable_keys()
    write("Insertion Sort", align="center", font=("Courier", 16, "bold"))
    length = len(s)
    for i in range(1, length):
        hole = i
        while hole > 0 and s[i].size < s[hole - 1].size:
            hole = hole - 1
        s.insert(hole, s.pop(i))
    enable_keys()

def ssort():
    disable_keys()
    write("Selection Sort", align="center", font=("Courier", 16, "bold"))
    length = len(s)
    for j in range(0, length - 1):
        imin = j
        for i in range(j + 1, length):
            if s[i].size < s[imin].size:
                imin = i
        if imin != j:
            s.insert(j, s.pop(imin))
    enable_keys()

def quick(left, right):
    if left < right:
        index = left
        pivot = s[index]
        s.insert(right, s.pop(index))
        for i in range(left, right): 
            if s[i].size < pivot.size:
                s.insert(index, s.pop(i))
                index += 1
        s.insert(index, s.pop(right)) 
        quick(left, index - 1)
        quick(index + 1, right)

def qsort():
    disable_keys()
    write("Quick Sort", align="center", font=("Courier", 16, "bold"))
    quick(0, n-1)
    enable_keys()

def bsort():
    disable_keys()
    write("Bubble Sort", align="center", font=("Courier", 16, "bold"))
    for i in range(n):
        for j in range(n - i - 1):
            if s[j].size > s[j + 1].size:
               s.insert(j+1, s.pop(j))
    enable_keys()

def osort():
    disable_keys()
    write("Odd-Even Sort", align="center", font=("Courier", 16, "bold"))
    while True:
        sorted = True
        for i in range(1, n-1, 2):
            if s[i].size > s[i+1].size:
               s.insert(i, s.pop(i+1)) 
               sorted = False
        for i in range(0, n-1, 2):
            if s[i].size > s[i+1].size:
               s.insert(i, s.pop(i+1)) 
               sorted = False
        if sorted:
            break
    enable_keys()

def gsort():
    disable_keys()
    write("Gnome Sort", align="center", font=("Courier", 16, "bold"))
    i = 0
    while i < n:
        if (i == 0 or s[i].size >= s[i-1].size):
            i += 1
        else:
            s.insert(i, s.pop(i-1)) 
            i -=  1
    enable_keys()

def randomize():
    disable_keys()
    write("Randomize", align="center", font=("Courier", 16, "bold"))
    target = list(range(n))
    random.shuffle(target)
    for i, t in enumerate(target):
        for j in range(i, len(s)):
            if s[j].size == t + 1:
                s.insert(i, s.pop(j))
    enable_keys()

def init_shelf():
    global n, s
    n = int(numinput('please advise','how many books to sort',10,2,20))
    target = list(range(1,n+1))
    random.shuffle(target)
    s = Shelf(n,-200) 
    for i in target:
        s.push(Book(i))

def disable_keys():
    onkey(None, "i")
    onkey(None, "s")
    onkey(None, "q")
    onkey(None, "b")
    onkey(None, "o")
    onkey(None, "g")
    onkey(None, "r")
    clear()

def enable_keys():
    clear()
    goto(0,-290 )
    write("r: randomize, spacebar: quit", align="center", font=("Courier", 16, "bold"))
    goto(0,-250)
    write("i: insertion sort, s: selection sort, q: quick sort", align="center", font=("Courier", 16, "bold"))
    goto(0,-270)
    write("b: bubble sort, o: odd-even sort, g: gnome sort", align="center", font=("Courier", 16, "bold"))  
    onkey(isort, "i")
    onkey(ssort, "s")
    onkey(qsort, "q")
    onkey(bsort, "b")
    onkey(osort, "o")
    onkey(gsort, "g")
    onkey(randomize, "r")
    onkey(bye, "space")

getscreen().clearscreen()
getscreen().setup(800,600)
ht()
up()
tracer(1,0)
init_shelf()
enable_keys()
listen()
