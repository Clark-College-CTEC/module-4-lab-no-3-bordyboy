# Lab No. 3
# CTEC 121
# Bogdan Livadaru

from graphics import *

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    win.setCoords (0,0,5,5)
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3

    circle1 = Circle(Point(2.5,3.5), .5)
    circle1.draw(win)

    circle2 = Circle(Point(2.5,2.4), .6)
    circle2.draw(win)

    circle3 = Circle(Point(2.5,1.1), .7)
    circle3.draw(win)



    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2

    eye1 = Circle(Point(2.3,3.6), .1)
    eye1.draw(win)

    eye2 = Circle(Point(2.7,3.6), .1)
    eye2.draw(win)


    eyeball1 = Circle(Point(2.3,3.6), .02)
    eyeball1.setFill('blue')
    eyeball1.draw(win)

    eyeball2 = Circle(Point(2.7,3.6), .02)
    eyeball2.setFill('blue')
    eyeball2.draw(win)

    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose

    nose = Polygon(Point(2.55,3.35), Point(2.25,3.28), Point(2.55,3.25))
    nose.setFill('orange')
    nose.draw(win)


    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat

    hat = Rectangle(Point(1.9,4), Point(3.1,4.25))
    hat.setFill('black')
    hat.draw(win)


    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline

    hatline = Line(Point(1.5,4), Point(3.5,4))
    hatline.setWidth(3)
    hatline.draw(win)


    # draw 2 arms
    
    arm1 = Line(Point(3.1,2.5), Point(4,3.5))
    arm1.draw(win)

    arm2 = Line(Point(1.9,2.5), Point(0.8, 3.5))
    arm2.draw(win)

    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()