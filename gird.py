import turtle


x = 0
y = 0
turtle.penup()

while (x < 6):
    turtle.penup()
    turtle.right(90)
    turtle.goto(100*x,400)
    turtle.pendown()
    turtle.forward(500)
    turtle.left(90)
    x = x + 1

while (y < 6):
    turtle.penup()
    turtle.goto(0,-100*y +400)
    turtle.pendown()
    turtle.forward(500)
    y = y + 1    
    
turtle.exitonclick
