from turtle import Turtle
allin = 'center'
score_font = ('Courier', 18, 'normal')
gameOver_font = ('Courier', 34, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.score_updater()
        self.hideturtle()

    def score_updater(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score = {self.score}', move=False, align=allin, font=score_font)

    def game_over(self):
        self.goto(0,0)
        self.write(arg='Game Over', move=False, align=allin, font=gameOver_font)
