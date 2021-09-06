from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

turtle=Turtle()
screen = Screen()
ball = Ball()
scoreboard = Scoreboard()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))


screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")





game_is_on = True
amount = 0.08
while game_is_on:
    
    time.sleep(amount)
    screen.update()
    ball.move()
    
    #detecting collision with the wall
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        amount *= 0.9
    # detects misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        amount += 0.009
        
        
        
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        amount += 0.009
        
    if scoreboard.l_score >= 5 or scoreboard.r_score >= 5:
        
        game_is_on = False
        scoreboard.game_over()
        
        







screen.exitonclick()