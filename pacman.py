import turtle

screen = turtle.Screen()

ball = turtle.Turtle()
ball.shape("circle")
ball.penup()
ball.shapesize(3)

food_list = []
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(-360, -300)
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(-330, -300)
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(-300, -300)
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(-270, -300)
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(-240, -300)
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(-210, -300)
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(-180, -300)
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(-150, -300)
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(-120, -300)
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.goto(-90, -300)


def move_up():
    ball.setheading(90)


def move_down():
    ball.setheading(270)


def move_left():
    ball.setheading(180)


def move_right():
    ball.setheading(0)


screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.listen()


while True:
    screen.update()
    ball.forward(1)

