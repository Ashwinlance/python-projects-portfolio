import turtle

screen = turtle.Screen()
screen.bgcolor("white")

score_card = turtle.Turtle()
score_card.hideturtle()
score_card.penup()
score_card.goto(0, 200)
score_card.write("Score: 0", align="center", font=("Arial", 24, "normal"))

score = 0

def update_score():
    global score
    score += 1
    score_card.clear()
    score_card.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

screen.onkeypress(update_score, "space")
screen.listen()

turtle.exitonclick()
