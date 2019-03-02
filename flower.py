import turtle


def draw_art(sam):
     sam.forward(100)
     sam.right(45)
     sam.forward(100)
     sam.right(135)
     sam.forward(100)
     sam.right(45)
     sam.forward(100)
     sam.right(135+5)

window = turtle.Screen()
window.bgcolor("green")
sam = turtle.Turtle()
sam.shape("turtle")
sam.speed(20)
angle = int(360/5)
for x in range(angle):
    draw_art(sam)


draw_art(sam)

window.exitonclick()