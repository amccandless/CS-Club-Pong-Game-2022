# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:29:31 2022
@author: wooki/Michelle
"""
import random
from paddle import Paddle
# IGNORE ERROR MESSAGE. THIS MODULE IS NEEDED
from ball import Ball


class Enemy(Paddle):
    """The class for the enemy. Extends Paddle Class
    Attributes:
    color: Current color of the Goal
    width: Width of the Enemy
    height: Height of the Enemy
    startX: Starting x of the Enemy
    staryY: Starting y of the Enemy
    paddleType: Paddle mode chosen by integer value
    ball: Ball the enemy should focus on
    difficulty: Difficulty setting of the Enemy
    health: Health of the Enemy. Integer or double values
    teleport: Ability to teleport boolean
    accuracy: value that helps define how the paddle looks for the ball
    """

    def __init__(self, color, width, height, startX, startY, paddleType, ball, difficulty='easy', health=0, teleport=False):
        super().__init__(color, width, height, startX, startY, paddleType, teleport)
        self.difficulty = difficulty
        self.paddleType = paddleType
        self.health = health
        self.ball = ball
        self.accuracy = 5

    def act(self):
        """Run logic for enemy movement.
        """
        if self.difficulty == 'easy':
            # Picks a number in the range 1-10.
            # If it is above 3, the enemy acts intelligently
            # If it is below, the enemy makes a mistake to mimic a Player
            # Making a mistake.
            if random.randrange(1, 10) > 3:

                # Looks for ball's Y to be in the paddle's Height
                # Minus 20 on both sides.
                # Self.accuracy gives the ball a bit
                if self.getY()+20 > self.ball.getY():
                    self.velUp(2)

                elif self.getY()+self.height-20 < self.ball.getY():
                    self.velDown(2)
                else:
                    self.idle()
            else:
                rand = random.randrange(0, 2)
                if rand == 1:

                    self.velUp(2)

                else:
                    self.velDown(2)
        self.moveGen()