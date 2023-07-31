from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        random_y = random.randint(-250, 250)
        self.goto(x=300, y=random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backwards(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT





