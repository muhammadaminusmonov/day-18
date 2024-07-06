import random
import turtle


COLORS = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
turtle.colormode(255)
tim = turtle.Turtle()
tim.up()
tim.hideturtle()
tim.speed("fastest")


def draw_line(num_dots):
    for _ in range(num_dots):
        tim.dot(20, random.choice(COLORS))
        tim.forward(50)


def update_position(x_position, y_position):
    y_position += 50
    tim.goto(x_position, y_position)
    return y_position


def turtle_position(dot_num):
    starting_position = -((dot_num - 1) * 50) / 2
    x_position = starting_position
    y_position = starting_position
    tim.goto(x_position, y_position)
    for _ in range(dot_num):
        draw_line(dot_num)
        y_position = update_position(x_position, y_position)


turtle_position(10)


screen = turtle.Screen()
screen.exitonclick()
