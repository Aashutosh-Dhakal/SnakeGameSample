from turtle import Turtle
move_distance = 20
Up = 90
Down = 270
Left = 180
Right = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for each in range(3):
            snake = Turtle('square')
            snake.color('white')
            snake.penup()
            snake.goto((each * -20), 0)
            self.segments.append(snake)

    def add_segment(self):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(self.segments[-1].position())
        self.segments.append(snake)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def right(self):
        if self.segments[0].heading() != Left:
            self.segments[0].setheading(Right)
