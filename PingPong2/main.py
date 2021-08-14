import turtle
def main_game():
    pen3.clear()
    def game_over():
        win1 = turtle.Screen()
        win1.bgcolor("black")
        win1.setup(width=800, height=600)
        win1.tracer(0)
        pen.clear()
        pen2 = turtle.Turtle()
        pen2.speed(0)
        pen2.color("white")
        pen2.penup()
        pen2.hideturtle()
        pen2.goto(0, 40)
        pen2.write("Game Over", align="center", font=("Courier", 24, "normal"))
        pen1 = turtle.Turtle()
        pen1.speed(0)
        pen1.color("white")
        pen1.penup()
        pen1.hideturtle()
        pen1.goto(0, 0)
        pen1.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        while True:
            win1.update()
    win=turtle.Screen()
    win.bgcolor("black")
    win.setup(width=800,height=600)
    win.tracer(0)
    # Score
    score=0
    # Paddle
    a=turtle.Turtle()
    a.speed(0)
    a.shape("square")
    a.color("white")
    a.shapesize(stretch_wid=1,stretch_len=5)
    a.penup()
    a.goto(0,-300)
    # Ball
    ball=turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0,0)
    ball.dx=0.125
    ball.dy=0.125
    # Pen
    pen=turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("Score: 0",align="center", font=("Courier",24,"normal"))
    # Function
    def paddle_right():
        x=a.xcor()
        x+=20
        a.setx(x)

    def paddle_left():
        x = a.xcor()
        x -= 20
        a.setx(x)
    # Input
    win.listen()
    win.onkeypress(paddle_right,"Right")
    win.onkeypress(paddle_left,"Left")
    # Game Loop
    while True:
        win.update()
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)
        # Check Border
        if (ball.ycor() > 300):
            ball.sety(300)
            ball.dy *= -1
        if (ball.ycor() < -300):
            ball.sety(-300)
            ball.dy *= -1
        if (ball.xcor() > 400):
            ball.setx(400)
            ball.dx *= -1

        if (ball.xcor() < - 400):
            ball.goto(0, 0)
            ball.dx *= -1
            # ball and paddle

        if (ball.ycor() < -290) and (ball.xcor() < a.xcor() + 40) and (ball.xcor() > a.xcor() - 40) and (ball.xcor() > -300):
            ball.sety(-290)
            ball.dy *= -1
            score += 1
            pen.clear()
            pen.write("Score: {}".format(score), align="center",font=("Courier", 24, "normal"))
        elif(ball.ycor()<-290)and(ball.ycor()>-300)and((ball.xcor()>a.xcor()+40)or(ball.xcor()<a.xcor()-40)):
            game_over()
win2=turtle.Screen()
win2.bgcolor("black")
win2.setup(width=800,height=600)
win2.tracer(0)
pen3=turtle.Turtle()
pen3.speed(0)
pen3.color("white")
pen3.penup()
pen3.hideturtle()
pen3.goto(0,0)
pen3.write("Press {} to start:".format('"shift + s"'),align="center", font=("Courier",24,"normal"))
win2.listen()
win2.onkeypress(main_game,"S")
while True:
    win2.update()







