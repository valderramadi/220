"""
Darla Valderrama
hw4.py

Problem: I will develop simple Python programs that use Python Graphics.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *
import math


def squares():
    width = 400
    height = 400
    win = GraphWin("HW 4", width, height)   # Creates graphical window
    num_clicks = 5

    instant_pt = Point(width / 2, height - 10)
    instruct = Text(instant_pt, "Click to move rectangle")
    instruct.draw(win)

    shape = Rectangle(Point(50, 50), Point(70, 70))   # Builds circle
    shape.setOutline("blue")
    shape.setFill("blue")
    shape.draw(win)

    for i in range(num_clicks):     # allowing user to click mult times to move circ
        user_click = win.getMouse()
        shape = Rectangle(Point(user_click.x - 10, user_click.y - 10), Point(user_click.x + 10, user_click.y + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)


    instant_pt = Point(width / 2, 10)
    instruct = Text(instant_pt, "Click here again to quit!")
    instruct.draw(win)

    win.getMouse()
    win.close()



def rectangle():
    width = 400
    height = 400
    length = 400
    win = GraphWin("Rectangles", width, height)
    Point_uno = win.getMouse()
    Point_dos = win.getMouse()
    length = abs(Point_uno.getX() - Point_uno.getX())
    width = abs(Point_dos.getY() - Point_dos.getY())
    area = length * width
    text = Text(Point(50, 50), "The area is: " + str(area))
    perimeter = 2 * length * width

    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Circle from radius and center", width, height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    one_x = p1.getX()
    two_x = p2.getX()
    one_y = p1.getX()
    two_y = p2.getX()
    radius = math.sqrt((two_x - one_x) ** 2 + (two_y - one_y) ** 2)
    circle_a = Circle(p1, radius)
    circle_a.draw(win)

    text = Text(Point(50, 50), "Radius: " + str(radius))
    text.draw(win)
    instruct = Text(Point(width / 2, height - 10), "Click again to quit ")
    win.getMouse()
    win.close()


def pi2():
    n = eval(input("Enter the number of terms wanted: "))
    acc = 0
    for i in range(n):
        num = 4
        denom = 1 + 2*i
        fraction = num / denom * ((-1) * i)
        acc = acc + fraction
    print(math.pi - acc)
    print(acc)

if __name__ == '__main__':
    # squares()
    rectangle()
    # circle()
    pass