from graphics import Point, GraphWin, Circle, Text

win = GraphWin('Face', 700, 700)
win.setCoords(0, 0, 10, 10)
label = Text(Point(5, 1), "Your name")
label.draw(win)
user_input = Entry(Point(5, 5), 50)
user_input.setText("enter your name here")
user_input.draw(win)
win.getMouse()
name = user_input
face = Circle(Points(5, 7), 3)


left_eye = Circle(Point(325, 60), 25)
left_eye.setFill('yellow')
left_eye.setOutline('green')
left_eye.setWidth(10)
right_eye = left_eye.clone()
right_eye.move(50, 0)

face.draw(win)
left_eye.draw(win)
right_eye.draw(win)
label.draw(win)

text_point = Point(350, 600)
label = Text(text_point, "Bob")


def convert_gui():
    win = GraphWin("Converter", 700, 500)
    win.setCoords(0, 0, 10, 10)
    celsius_text = Text(Point(3, 8), "Enter Celsius: ")
    celsius_entry = Entry(Point(7, 8), 30)
    click_text = Text(Point(5, 5), "Click to convert!")
    result_text = Text(Point(5, 1), '')

    celsius_text.draw(win)
    celsius_entry.draw(win)
    click_text.draw(win)
    result_text.draw(win)

    win.getMouse()
    celsius_temp = eval(celsius_entry.getText())
    fahrenheit = celsius_temp * 9 / 5 + 32
    result_text.setText(fahrenheit)
    win.getMouse()
    


convert_gui()
