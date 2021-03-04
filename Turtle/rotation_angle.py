import turtle
mypen = turtle.Pen()

mypen.pensize(4)
mypen.pencolor('steelblue')
mypen.left(60) #旋转角度
mypen.fd(50)
print(mypen.xcor())
turtle.done()