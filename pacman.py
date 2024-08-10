import turtle

turtle.addshape(name="turtle1.gif", shape=None)
turtle.addshape(name="pacman1.gif", shape=None)
screen = turtle.Screen()
screen.setup(800, 800, 0, 0)
screen.tracer(0)

'''
turtle_icon = turtle.Turtle()
turtle_icon.shape("turtle1.gif")
'''

pacman_icon = turtle.Turtle()
pacman_icon.shape("pacman1.gif")

ball = turtle.Turtle()
ball.shape("circle")
ball.penup()
ball.shapesize(3)
ball_speed = 0.1

'''
food = turtle.Turtle()
food.shape("circle")
food.shapesize(3, 3)
'''
food_list = []
food_grid_list = [
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

for row in range(0, 10, 1):
    for column in range(0, 10, 1):
        if food_grid_list[row][column] == 1:
            new_food = turtle.Turtle()
            new_food.shape("square")
            new_food.penup()
            new_food.goto(-300 + (column * 60), 300 - (row * 60))
            food_list.append(new_food)

enemy1 = turtle.Turtle()
enemy1.shape("triangle")
enemy1.shapesize(2.5)
enemy1.penup()
enemy1.goto(-360, 290)

enemy2 = turtle.Turtle()
enemy2.shape("triangle")
enemy2.shapesize(2.5)
enemy2.penup()
enemy2.goto(-350, -290)

enemy3 = turtle.Turtle()
enemy3.shape("triangle")
enemy3.shapesize(2.5)
enemy3.penup()
enemy3.goto(-360, -290)
enemy_speed = 0.2

score_board = turtle.Turtle()
score_board.hideturtle()
score_board.penup()
score_board.goto(-370, -370)
score = 0
score_board.write("score = "+str(score), font=("Arial", 30, "bold"))


def move_up():
    ball.setheading(90)


def move_down():
    ball.setheading(270)


def move_left():
    ball.setheading(180)


def move_right():
    ball.setheading(0)


def enemy_1_r():
    enemy1.setheading(0)


def enemy_1_l():
    enemy1.setheading(180)


def enemy_2_u():
    enemy2.setheading(90)


def enemy_2_d():
    enemy2.setheading(270)


def enemy_3_r():
    enemy3.setheading(0)


def enemy_3_l():
    enemy3.setheading(180)


screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.listen()

while True:
    screen.update()
    ball.forward(ball_speed)
    for food in food_list:
        if food.distance(ball) < 30:
            score = score + 1
            score_board.clear()
            score_board.write("score = " + str(score), font=("Arial", 30, "bold"))
            food.hideturtle()
            food_list.remove(food)
            break
    if ball.xcor() >= 330:
        ball.goto(330, ball.ycor())
    if ball.xcor() <= -360:
        ball.goto(-360, ball.ycor())
    if ball.ycor() >= 300:
        ball.goto(ball.xcor(), 300)
    if ball.ycor() <= -290:
        ball.goto(ball.xcor(), -290)
    enemy1.forward(ball_speed)
    if enemy1.xcor() >= 330:
        enemy_1_l()
    if enemy1.xcor() <= -360:
        enemy_1_r()
    enemy3.forward(enemy_speed)
    if enemy3.xcor() >= 330:
        enemy_3_l()
    if enemy3.xcor() <= -360:
        enemy_3_r()
    if enemy2.ycor() <= -290:
        enemy_2_u()
    enemy2.forward(enemy_speed)
    if enemy2.ycor() >= 300:
        enemy_2_d()
    if ball.distance(enemy1) < 20 or ball.distance(enemy2) < 20 or ball.distance(enemy3) < 20:
        ball_speed = 0
        enemy_speed = 0
