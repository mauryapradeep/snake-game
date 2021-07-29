from turtle import Turtle
import random
#food_interaction = 0
class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        # self.shapesize(0.5)
        self.food_interaction = 0
        self.shapesize(self.food_size())
        self.color("yellow")
        self.penup()
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)




    def food_size(self):
        if self.food_interaction % 2 ==0 & self.food_interaction >0:

            return 1
        else:
            return 0.5


