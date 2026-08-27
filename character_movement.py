import turtle

screen = turtle.Screen()
screen.bgcolor("white")

character = turtle.Turtle()
character.shape("turtle")
character.color("blue")
character.penup()
character.speed(0)

def move_left():
    character.setx(character.xcor() - 10)

def move_right():
    character.setx(character.xcor() + 10)

screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.listen()

turtle.exitonclick()
