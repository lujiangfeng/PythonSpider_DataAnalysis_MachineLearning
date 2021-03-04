import turtle
t = turtle.Pen()
t.forward(100)
t.goto(100,100)
i =0
while i<180:
    t.forward(1)
    t.right(1)
    i = i+1
turtle.done() # 默认向右