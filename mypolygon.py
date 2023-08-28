import turtle
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    t.lt(45)
    t.fd(math.sqrt(length**2 + length**2))
    t.lt(135)
    t.fd(length)
    t.lt(135)
    t.fd(math.sqrt(length**2 + length**2))
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length);
        t.lt(angle)
def polygon(t, length, n):
    angle = 360.0 / n
    polyline(t, n, length, angle)
def arc(t, r, angle):
    arc_length = 2*math.pi*r*angle/360
    sides = int(arc_length / 3) + 1
    step_length = arc_length / sides
    step_angle = angle / sides
    polyline(t, sides, step_length, step_angle)
def circle(t, r):
    arc(t, r, 360)
bob = turtle.Turtle()
print(bob)
# square(bob, 25)
# polygon(bob, 100, 10)
circle(bob, 100)
# arc(bob, 100, 180)

turtle.mainloop()