from turtle import Turtle, Screen 
import random


# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

# Challenge 1

#for _ in range(4):
#    tim.forward(100)
#    tim.left(90)

# -------------------------

# Challenge 2 

#for _ in range(15):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()

# -------------------------

# Challenge 3

# colours = ["magenta", "dark magenta", "purple", "medium violet red", "dark orchid"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides

#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# -------------------------

# Challenge 4

# colours = ["magenta", "dark magenta", "purple", "medium violet red", "dark orchid"]
# directions = [0, 90, 180, 270]
# tim.penzise(15)
# tim.speed("fast")

# for _ in range(280):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))



# ------------------------------------------------

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color



# directions = [0, 90, 180, 270]
# tim.penzise(15)
# tim.speed("fast")

# for _ in range(280):
#     tim.color(random_color)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# -------------------------

# Challenge 5

import turtle as t


tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range (int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()