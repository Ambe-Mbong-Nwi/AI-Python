# star with 5 sides.
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

tess.speed(3)
tess.pensize(3)

for x in range(5):
    tess.forward(200)
    tess.right(144)

tess.hideturtle()
wn.mainloop()

