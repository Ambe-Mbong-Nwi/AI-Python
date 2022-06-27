# question 3
# for regular polygon with 18 sides the angle to turn the turtle at each corner is 360 / 18 = 20

import turtle

window = turtle.Screen()
pointer = turtle.Turtle()

pointer.penup()
pointer.left(-90)
pointer.forward(250)
pointer.left(90)
pointer.forward(-50)
pointer.pendown()

for i in range(18):
    pointer.forward(90)
    pointer.left(20)

window.mainloop()