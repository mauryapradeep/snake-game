from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):

        for position in STARTING_POSITION:
            self.add_segments(position)

    def add_segments(self,position):

            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


    def extend(self):
        self.add_segments(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def move_down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

