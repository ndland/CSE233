from graphics import *
import math


def main():
    """This is the main function"""

    win = GraphWin("Draw a triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    point_1 = win.getMouse()
    point_1.draw(win)
    point_2 = win.getMouse()
    point_2.draw(win)
    point_3 = win.getMouse()
    point_3.draw(win)

    triangle = Polygon(point_1, point_2, point_3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    side_one = point_1.getY() - point_2.getY()
    side_two = point_2.getX() - point_3.getX()
    side_three = point_1.getY() - point_3.getY()

    perimeter = side_one + side_two + side_three

    s = (perimeter) / 2

    area = abs((s * (s - side_one) * (s - side_two) * (s - side_three)))
    area = math.sqrt(area)

    message.setText("The perimeter of the triangle is " +
                    str(round(perimeter, 2)))
    win.getMouse()
    message.setText("The area of the triangle is " + str(round(area, 2)))
    win.getMouse()

    message.setText("Click anywhere to quit.")
    win.getMouse()


main()
