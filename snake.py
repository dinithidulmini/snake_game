from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
right = 0
left = 180

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for por in positions:
            self.new_segment(por)

    def new_segment(self,por):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(por)
        self.turtles.append(tim)

    def extend(self):
        index = len(self.turtles)-1
        new_position = self.turtles[index].position()
        self.new_segment(new_position)

    def move(self):
        for number in range((len(self.turtles)-1),0,-1):
             new_x = self.turtles[number-1].xcor()
             new_y = self.turtles[number-1].ycor()
             self.turtles[number].goto(new_x,new_y)
        self.turtles[0].forward(move_distance)

    def m_up(self):
        if self.turtles[0].heading() != down:
            self.turtles[0].setheading(up)

    def m_down(self):
        if self.turtles[0].heading() != up:
            self.turtles[0].setheading(down)

    def m_right(self):
        if self.turtles[0].heading() != left:
            self.turtles[0].setheading(right)

    def m_left(self):
        if self.turtles[0].heading() != right:
            self.turtles[0].setheading(left)