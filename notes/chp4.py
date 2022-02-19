import graphics

my_point = graphics.Point(50, 70)
point_a = graphics.Point(70, 90)
# print(point_a.getX()),print(point_a.getY())  # accessor methods
point_a.move(10, 0)
# print(point_a.getX()), print(point_a.getY())   # 80,90 now bc moving 10,0

# actual window we are working on
win = graphics.GraphWin("CSCI 220", 500, 600)
input("hit enter to close")     # pause program for a sec so doesnt continue running ... bc waiting on user input
middle = graphics.Point(350, 300)
middle.draw(win)
input('hit enter to close')


my_circle = Circle(middle, 40)
my_circle.draw(win)

input('hit enter to close')





