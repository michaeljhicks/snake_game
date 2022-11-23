from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

    # for seg_num in range(start=2, stop=0, step=-1):
    # segments[seg_num] = goto.xcor()
    # segments[seg_num] = goto


screen.exitonclick()

# TODO: 1. Create a snake body
# segment_1 = Turtle('square')
# segment_1.color('white')
# segment_2 = Turtle('square')
# segment_2.color('white')
# segment_2.goto(-20, 0)
# segment_3 = Turtle('square')
# segment_3.color('white')
# segment_3.goto(-40, 0)

# easier way to generate squares
# these are tuples
# TODO: 2.1. Move the snake


# TODO: 2.2. while loop to move the snake

# TODO: 3. Create Snake Food

# TODO: 4. Detect collision with food
# TODO: 5. Create a scoreboard
# TODO: 6. Detect collision with wall
# TODO: 7. Detect collision with tail
