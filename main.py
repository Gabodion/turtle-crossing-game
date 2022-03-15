import time
import random
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move()

    #create new random cars
    if car_manager.all_cars[-5].xcor() < 150:
        car_manager.create_car()

    #finish line
    if player.ycor() > 280:
        car_manager.move_increase()
        scoreboard.increase_level()
        player.goto(0, -280)

    #collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()