from turtle import Turtle 
import random 

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("RED")
        self.speed("fastest")
        self.goto(x=random.randint(-280,280),y=random.randint(-280,280))
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-280,280),y=random.randint(-280,280))