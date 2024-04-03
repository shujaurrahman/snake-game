from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))

    def increaseScore(self):
        self.score+=1
        self.clear()
        self.updateScoreboard()

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER.",align="center",font=("Arial",24,"normal"))
        
    def tail_msg(self):
        self.goto(30,30)
        self.write(f"Head collided with body! BOOM.",align="center",font=("Arial",24,"normal"))
