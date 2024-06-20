from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
import subprocess
import sys

def run():
    
    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    def import_or_install(package):
        try:
            __import__(package)
        except ImportError:
            install(package)
            __import__(package)

    required_packages = ['pygame']

    for package in required_packages:
        import_or_install(package)

    print("All packages are installed and imported successfully.")


def game_on():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(.1)
        snake.move()

        if snake.head.distance(food) < 15:
            pygame.mixer.music.load('biteSound.mp3')
            pygame.mixer.music.play()
            snake.add_segment()
            food.refresh()
            scoreboard.score_updater()

        if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            pygame.mixer.music.load('deathSound.mp3')
            pygame.mixer.music.play()
            game_is_on = False

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                pygame.mixer.music.load('deathSound.mp3')
                pygame.mixer.music.play()
                game_is_on = False

run()
import pygame

screen = Screen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

pygame.mixer.init()
game_on()

screen.exitonclick()
