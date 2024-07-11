from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP_DIRECTION = 90
DOWN_DIRECTION = 270
LEFT_DIRECTION = 180
RIGHT_DIRECTION = 0

class Snake:
    def __init__(self, speed):
        self.segments = []
        self.speed = speed
        self.create_snake()
        # self.head = self.segments[0]
        # self.head.shape("circle")

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(stretch_wid=0.5, stretch_len= 0.5)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.segments[0].heading() != RIGHT_DIRECTION:
            self.segments[0].setheading(LEFT_DIRECTION)

    def right(self):
        if self.segments[0].heading() != LEFT_DIRECTION:
            self.segments[0].setheading(RIGHT_DIRECTION)

    def up(self):
        if self.segments[0].heading() != DOWN_DIRECTION:
            self.segments[0].setheading(UP_DIRECTION)

    def down(self):
        if self.segments[0].heading() != UP_DIRECTION:
            self.segments[0].setheading(DOWN_DIRECTION)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        # self.head = self.segments[0]


