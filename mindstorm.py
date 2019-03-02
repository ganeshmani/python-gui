import turtle

def draw_sqaure(turtle,angle_interval):
    for i in range(1,5):
        if i == 4:
            turtle.forward(100)
            turtle.right(90 + angle_interval)
        else:
            turtle.forward(100)
            turtle.right(90)
def draw_art(angle_interval):

    window = turtle.Screen()
    window.bgcolor("green")

    sam = turtle.Turtle()
    sam.shape("turtle")
    sam.speed(20)

    angle = int(360/angle_interval)

    for i in range(1,angle):
        draw_sqaure(sam,angle_interval)
    

    window.exitonclick()


print("Enter angle Interval:")
angle_interval = int(input())

draw_art(angle_interval)    
