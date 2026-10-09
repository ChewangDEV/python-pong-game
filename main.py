from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.tracer(0)   # Turn off the screen updates for smoother animation

ball = Ball()
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0) ) # Create the right paddle at position (350, 0)
l_paddle = Paddle((-350, 0)) # Create the left paddle at position (-350, 0)



screen.setup(width=800, height=600)  # Set the width and height of the screen
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")  # Bind the up arrow key to move the paddle up
screen.onkeypress(r_paddle.move_down, "Down")  # Bind the down arrow key to move the paddle down

screen.onkeypress(l_paddle.move_up, "w")  # Bind the 'w' key to move the second paddle up
screen.onkeypress(l_paddle.move_down, "s")  # Bind the 's' key to move the second paddle down

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)  # Add a small delay to control the game speed
    screen.update()  # Update the screen to reflect any changes
    ball.move()

    #Collision with the top and bottom wall change direction
    if ball.ycor() > 280 or ball.ycor() < -280:  # Check if the ball has gone beyond the screen boundaries
        ball.bounce_y()  # Bounce the ball back if it hits the top or bottom of the screen

    #Collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()  # Bounce the ball back if it hits the right paddle

    # Out of boundry then restart and move opposite directions r_paddle
    if ball.xcor() > 380: # Check if the ball has gone beyond the left or right boundaries
        ball.restart()  # Restart the ball to the center if it goes out of bounds
        scoreboard.l_point()

    # Out of boundry then restart and move opposite directions r_paddle
    if ball.xcor() < -380: # Check if the ball has gone beyond the left or right boundaries
        ball.restart()  # Restart the ball to the center if it goes out of bounds
        scoreboard.r_point()


screen.exitonclick()  # Keep the window open until clicked