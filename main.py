from snakeclass import Snake
from turtle import Turtle, Screen
import time
from food import Food
from score import Score

GAME_STATUS = True
screen = Screen()
# def setup_game()
def game():
    screen = Screen()
    level = screen.textinput(title="difficulty level", prompt="Choose difficulty level: easy/medium/hard").lower()
    if level == "easy":
        sleep_time = 0.2

    elif level == "medium":
        sleep_time = 0.1

    elif level == "hard":
        sleep_time = 0.05

    else:
        sleep_time = 0.1


    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("MY SNAKE")
    screen.tracer(0)

    snake = Snake(speed=sleep_time)
    food = Food()
    scoreboard = Score()

    screen.listen()
    screen.onkey(key="Up", fun= snake.up)
    screen.onkey(key="w", fun= snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="s", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="a", fun=snake.left)
    screen.onkey(key="Right", fun= snake.right)
    screen.onkey(key="d", fun= snake.right)
    
    
    global GAME_STATUS
    GAME_STATUS = True
    while GAME_STATUS:
        screen.update()
        time.sleep(snake.speed)
        snake.move()

        if snake.segments[0].distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.scoreboard()

        if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -295 or snake.segments[0].ycor() < -295 or snake.segments[0].ycor() > 295:
            GAME_STATUS = False
            scoreboard.gameover()
            # time.sleep(2)
            scoreboard.reset()
            # time.sleep(2)
            play_again = screen.textinput(title="play again", prompt="Wanna play again, yes or no").lower()
            if play_again == "yes":
                screen.clear()
                game()
            else:
                exit()

        for segment in snake.segments[1:]:
            if snake.segments[0].distance(segment) < 5:
                scoreboard.gameover()
                # time.sleep(2)
                scoreboard.reset()

                play_again = screen.textinput(title="play again", prompt="Wanna play again, yes or no").lower()
                if play_again == "yes":
                    GAME_STATUS = True
                    screen.clear()
                    game()
                else:
                    exit()

game()
screen.exitonclick()