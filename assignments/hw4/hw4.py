"""
Name: Darla Valderrama
hw4.py

Problem: I will develop simple Python programs that use Python Graphics.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        shape = Rectangle(Point(click.x - 10, click.y - 10), Point(click.x + 10, click.y + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)

        instant_pt = Point(width / 2, 10)
        instruct = Text(instant_pt, "Click here again to quit!")
        instruct.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    width = 400
    height = 400
    win = GraphWin("Rectangles", width, height)
    mensaje_uno = Text(Point(200, 10), "CLick on two points to create a rectangle! ")
    mensaje_uno.draw(win)
    point_uno = win.getMouse()
    point_uno.draw(win)
    point_dos = win.getMouse()
    point_dos.draw(win)

    rect_angle = Rectangle(point_uno, point_dos)
    rect_angle.setFill("blue")
    rect_angle.setOutline("blue")
    rect_angle.draw(win)

    length = abs(point_dos.getX() - point_uno.getX())
    width = abs(point_dos.getY() - point_uno.getY())
    message = Text(Point(90, 90), "Our Perimeter is: " + str(length + width))
    message.draw(win)
    message = Text(Point(70, 70), "Our area is: " + str(length * width))
    message.draw(win)

    instant_pt = Point(200, 300)
    instructions = Text(instant_pt, "Click again to close!")
    instructions.draw(win)

    win.getMouse()
    win.close()


def circle():
    width = 500
    height = 500
    win = GraphWin("Circle", width, height)
    point_i = Point(100, 100)
    instructions = Text(point_i, "Click on the center of the circle!")
    instructions.draw(win)
    user_clicky = win.getMouse()
    instructions_two = Text(Point(150, 50), "Click on the outside of the circle! ")
    instructions_two.draw(win)
    two_userclicks = win.getMouse()

    one_x = user_clicky.getX()
    two_x = two_userclicks.getX()
    one_y = user_clicky.getY()
    two_y = two_userclicks.getY()
    radius = math.sqrt((two_x - one_x) ** 2 + (two_y - one_y) ** 2)

    another_text = Text(Point(250, 250), 'Radius: ' + str(radius))
    another_text.draw(win)
    shapey = Circle(user_clicky, radius)
    shapey.draw(win)

    closing_win = Text(Point(250, 150), "Click to close window!")
    closing_win.draw(win)

    win.getMouse()
    win.close()


def pi2():
    n_one = eval(input("Enter the number of terms wanted: "))
    acc = 0
    for i in range(n_one):
        num = 4
        denom = 1 + 2 * i
        fraction = num / denom * ((-1) ** i)
        acc += fraction
    print(acc)
    print(math.pi - acc)


if __name__ == '__main__':
    # squares()
    # rectangle()
    # circle()
    # pi2()
    pass
