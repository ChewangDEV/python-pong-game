from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # Make the paddle taller
        self.penup()
        self.goto(position)  # Position the paddle on the right side of the screen

    def move_up(self):
        new_y = self.ycor() + 20 # Same position but add 20 paces
        self.goto(x=self.xcor(), y=new_y) # and change the y position to the new position (upwards)

    def move_down(self):
            new_y = self.ycor() - 20 # Same position but subtract 20 paces
            self.goto(x=self.xcor(), y=new_y) # and change the y position to the new position (downwards)


