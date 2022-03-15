from turtle import Turtle
import random
CARS = 15
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        for new_car in range(CARS):
            self.car_set()

    def car_set(self):
        car = Turtle("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        car.setheading(180)
        car.color(random.choice(COLORS))
        y_axis = random.randint(-230, 230)
        x_axis = random.randint(300, 700)
        car.goto(x_axis, y_axis)
        self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def move_increase(self):
        self.move_distance += MOVE_INCREMENT

