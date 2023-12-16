from turtle import Turtle

TURTLE_STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# DIRECTIONS TO MOVE ON, THEY ARE IN DEGREES TO BE CONSIDERED LOGICALLY
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle_instance_list = []
        self.create_instance()
        self.head = self.turtle_instance_list[0]

    def create_instance(self):
        for position in TURTLE_STARTING_POSITION:
            new_turtle_instance = Turtle(shape="square")
            new_turtle_instance.color("white")
            new_turtle_instance.penup()
            new_turtle_instance.goto(position)
            self.turtle_instance_list.append(new_turtle_instance)

    def move(self):
        """
        Here in the below for loop, we take the x & y coordinates of the previous instance
        After that we move the next instance towards the position of the next instance
        if instance_2 is at pos(20, 20), than instance_3 shall be moved to that position
        instance_2 shall be moved to the previous position of the instance_1 and the instance_1 is
        moved forward to the new position.
        """

        for instance_num in range(len(self.turtle_instance_list) - 1, 0, -1):
            print(f"\n\t Index -> {instance_num}")
            new_x = self.turtle_instance_list[instance_num - 1].xcor()
            new_y = self.turtle_instance_list[instance_num - 1].ycor()
            self.turtle_instance_list[instance_num].goto(new_x, new_y)

        self.turtle_instance_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)
