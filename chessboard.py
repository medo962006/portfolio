import turtle
t = turtle.Turtle()
s = t.getscreen()
t.penup()
t.goto(200,-200)
t.pendown()
t._rotate(90)
for i in range(4):
    t.forward(400)
    t._rotate(90)

for i in range(4):
    t.forward(50)
    t.left(90)
    t.forward(400)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(400)
    t.left(90)
for i in range(4):
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(400)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(400)
