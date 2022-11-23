from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

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
