import turtle as t
import random as r

# tim = t.Turtle()
# tim.shape("turtle")
# tim.color("DodgerBlue")


# challenge 1
# tim = t.Turtle()
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# challenge 2
# tim = t.Turtle()
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# challenge 3
# tim = t.Turtle()
# corner = 3
# colors = ["red", "blue", "green", "yellow", "brown"]
# for _ in range(7):
#     angle = 360 / corner
#     tim.color(r.choice(colors))
#     for _ in range(corner):
#         tim.forward(50)
#         tim.right(angle)
#     corner += 1


# challenge 4
# tim = t.Turtle()
# t.colormode(255)
#
# directions = [0, 90, 180, 270]
# tim.speed("fastest")
# tim.width(10)
#
#
# def random_color():
#     red = r.randint(0, 255)
#     green = r.randint(0, 255)
#     blue = r.randint(0, 255)
#     return red, green, blue
#
#
# def random_walk():
#     tim.color(random_color())
#     tim.forward(25)
#     tim.setheading(r.choice(directions))
#
#
# for _ in range(200):
#     random_walk()


# challenge 5
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)


def random_color():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    return red, green, blue


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(7)


screen = t.Screen()
screen.exitonclick()
