import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

screen = turtle.Screen()
screen.bgcolor("black")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 200)
ball.dy = -2

while True:
    ball.dy -= 0.1
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() < -200:
        ball.dy *= -1

turtle.exitonclick()
