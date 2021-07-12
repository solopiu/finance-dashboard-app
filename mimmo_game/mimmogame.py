# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:38:48 2021

@author: arianna.parisi
"""

import turtle
import os
import random
import time
import urllib.request
from PIL import Image

apple_path_image = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/green-apple_1f34f.png"
cat_path_image = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/cat-face_1f431.png"
yarn_path_image = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/yarn_1f9f6.png"

# if only background is in the folder save images from urls
if len([f for f in os.listdir(".") if f.endswith(".gif")]) == 1:

    for p in [cat_path_image, yarn_path_image, apple_path_image]:
        new_path = p.split("/")[-1].split(".")[-2] + ".gif"
        urllib.request.urlretrieve(
          p,
           "gifs/" + new_path)
    
        im1 = Image.open("gifs/" + new_path).resize((40,40)).convert('RGBA')
        info = im1.info
        im1.save(p.split("/")[-1], **info)
        
    png_files = [f for f in os.listdir(".") if f.endswith(".png")]
    for f in png_files:
        os.rename(f, f.split(".")[-2]+".gif")

screen = turtle.Screen()
screen.title("Mimmo likes yarn and hates fruits")
screen.bgcolor("black")
screen.bgpic("bg.gif")
screen.setup(width=800, height=600)
screen.tracer(0)

L = cat_path_image.split("/")[-1].split(".")[-2] + ".gif"
R = cat_path_image.split("/")[-1].split(".")[-2] + ".gif"
BAD = apple_path_image.split("/")[-1].split(".")[-2] + ".gif"
GOOD = yarn_path_image.split("/")[-1].split(".")[-2] + ".gif"
LIVES = 3
SCORE = 0

screen.register_shape(L)
screen.register_shape(R)
screen.register_shape(BAD)
screen.register_shape(GOOD)

score = SCORE
lives = LIVES

player = turtle.Turtle()
player.speed(0)
player.shape(L)
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Good
goods = []

for _ in range(20):
    good_thing = turtle.Turtle()
    good_thing.speed(0)
    good_thing.shape(GOOD)
    good_thing.color("green")
    good_thing.penup()
    good_thing.goto(-100, 250)
    good_thing.speed = random.randint(1, 2)

    goods.append(good_thing)

# Bad
bads = []

for _ in range(20):
    bad_thing = turtle.Turtle()
    bad_thing.speed(0)
    bad_thing.shape(BAD)
    bad_thing.color("red")
    bad_thing.penup()
    bad_thing.goto(100, 250)
    bad_thing.speed = random.randint(1, 2)

    bads.append(bad_thing)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {}  Lives: {}".format(SCORE, LIVES),\
          align="center", font=("Arial", 16, "normal"))

# Functions
def left():
    player.direction = "left"
    player.shape(L)
    
def right():
    player.direction = "right"
    player.shape(R)

    
screen.listen()
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

# initial score and lives
score = SCORE
lives = LIVES

while True:
    screen.update()
    
    # Move the player
    if player.direction == "left":
        player.setx(player.xcor() - 1)
    
    if player.direction == "right":
        player.setx(player.xcor() + 1)
        
    # Check for border collisions
    if player.xcor() < -390:
        player.setx(-390)
        
    elif player.xcor() > 390:
        player.setx(390)
        
    for good_thing in goods:
        # Move the good things
        good_thing.sety(good_thing.ycor() - good_thing.speed)
    
        # Check if good things are off the screen
        if good_thing.ycor() < -300:
            good_thing.goto(random.randint(-300, 300), random.randint(400, 800))

        # Check for collisions
        if player.distance(good_thing) < 40:
            # Score increases
            score += 10
        
            # Show the score
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
        
            # Move the good thing back to the top
            good_thing.goto(random.randint(-300, 300), random.randint(400, 800))



    for bad_thing in bads:    
        # Move the bad things
        bad_thing.sety(bad_thing.ycor() - bad_thing.speed)
    
        if bad_thing.ycor() < -300:
            bad_thing.goto(random.randint(-300, 300), random.randint(400, 800))
    
        
        if player.distance(bad_thing) < 40:
            # Score increases
            score -= 10
            lives -= 1
        
            # Show the score
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
            
            time.sleep(1)
            # Move the bad things back to the top
            for bad_thing in bads:
                bad_thing.goto(random.randint(-300, 300), random.randint(400, 800))
        
        
    # if game over
    if lives == 0:
        pen.clear()
        pen.write("Game Over! Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        screen.update()
        time.sleep(10)
        # reset score and lives
        score = SCORE
        lives = LIVES
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
        
        
        
        
        
        
        
