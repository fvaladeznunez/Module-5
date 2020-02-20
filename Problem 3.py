# Fernando Valadez-Nunez
# 02/13/2020

# Program asks user for the number of sides, lenght of the side, the color of
# the line and the fill color of a regular polygon, program should draw the polygon
# and fill it

numsides= int (input("What are the number of sides of the polygon?"))

lensides= int (input("What is the lenght of the side of the polygon?"))

linecolor= input("What are the color of the lines?")

fillcolor= input("What is the fill color of the polygon?")

import turtle

t= turtle.Turtle()

t.color(linecolor)

angle= 360/numsides

t.begin_fill()
for f in range (numsides):
    t.forward(lensides)
    t.right(angle)
t.color(fillcolor)
t.end_fill()

