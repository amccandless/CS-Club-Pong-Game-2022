import pygame
from random import randint

BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Ball(pygame.sprite.Sprite):
    """
    The class for the ball
    Attributes:
    color: Current color of the Ball
    width: Width of the Ball
    height: Height of the Ball
    max_vel: Fastest speed the Ball can go
    startX: Starting x position of the Ball
    startY: Starting y position of the Ball
    startVel: Starting velocity of the Ball
    """

    def __init__(self, color, width, height, max_vel, startX, startY, startVel):

        # Sprite instructure
        super().__init__()

        # For easy accessibility
        self.bounces = 0
        self.color = color
        self.width = width
        self.height = height
        self.max_vel = max_vel
        self.startX = startX
        self.startY = startY
        self.startVel = startVel
        self.paddleCollide = False

        # Create ball's image
        # Fill the image
        self.image = pygame.Surface([width, height])
        self.image.fill(self.color)
        self.image.set_colorkey(BLACK)

        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, self.color, [0, 0, width, height])
        #pygame.draw.circle(self.image, self.color, [width, height], 20)
        self.velocity = [randint(1, 3), randint(-3, 3)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.reset()

    def getDir(self):
        """Get direction of ball.
        Returns:
        up if ball moving up
        down if ball moving down
        neutral if moving horizontally
        """
        if self.velocity[1] < 0:
            return "up"
        elif self.velocity[1] > 0:
            return "down"
        else:
            return "neutral"

    def getPaddleCollide(self):
        """Find out if ball is colliding with PaddleCollide
        Returns:
        True if the ball is colliding with the paddle
        False if not
        """
        return self.paddleCollide

    def setPaddleCollide(self, tF):
        """Set a boolean value for if the ball is colliding with the paddle
        """
        self.paddleCollide = tF

    def reset(self):
        """Reset ball to start position
        """
        print(str(self.startX))
        self.rect.x = self.startX
        self.rect.y = self.startY
        self.paddleCollide = False
        # randNum = randint(1,3)
        randNum2 = randint(0, 2)
        if randNum2 == 0:
            self.velocity = [-self.startVel, -self.startVel]
        else:
            self.velocity = [self.startVel, self.startVel]

    def update(self):
        """Simply update position of the ball
        """
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def getX(self):
        """Return x.
        """
        return self.rect.x

    def getY(self):
        """Return y.
        """
        return self.rect.y

    def bounce(self, mode=0):
        """Bounce the ball
        mode 0 (stationary paddle): Like normal except if ball hits the paddle
        straight on there is only a random chance for a speed change and dir
        change.
        mode 1 and 2: If the ball's direction matches that of the paddle,
        speed is increased. If it does not match, ball slows down
        """

        ##if self.velocity[1] < self.max_vel and self.velocity[1] >0:
        # multiplier = 1
        # if self.velocity[1] < 0:
        #     self.velocity[1] = -self.velocity[1]
        #     self.velocity[2] = -self.velocity[2]
        #     multiplier = -1
        if mode == 0:
            if self.getDir() == "up":

                self.velocity[1] += .5
                self.velocity[0] += .5
            elif self.getDir() == "down":

                self.velocity[1] += .5
                self.velocity[0] += .5
            else:
                if randint(0, 10) > 2:
                    self.velocity[1] = self.startVel
                    self.velocity[0] = self.startVel

        elif mode == 1:
            if self.getDir() == "up":
                self.velocity[1] += .5
                self.velocity[0] += .5
            elif self.getDir() == "down":
                self.velocity[1] -= .5
                self.velocity[0] -= .5
            else:
                self.velocity[1] += .5
                self.velocity[0] += .5
        elif mode == 3:
            if self.getDir() == "up":
                self.velocity[1] -= .5
                self.velocity[0] -= .5
            elif self.getDir() == "down":
                self.velocity[1] += .5
                self.velocity[0] += .5
            else:
                self.velocity[1] += .5
                self.velocity[0] += .5
        elif mode == 4:
            print("Mode 4 should be used now-")
            if self.velocity[0] > 0:
                self.velocity[0] += 1
            elif self.velocity[0] < 0:
                self.velocity[0] -= 1
            else:
                self.velocity[0] += 1
            if self.velocity[1] > 0:
                self.velocity[1] += 1
            elif self.velocity[1] < 0:
                self.velocity[1] -= 1
            else:
                if randint(0, 10) > 2:
                    self.velocity[1] = self.startVel
                    self.velocity[0] = self.startVel
        else:
            if self.velocity[0] > 0:
                self.velocity[0] += .5
            elif self.velocity[0] < 0:
                self.velocity[0] -= .5
            else:
                self.velocity[0] += .5
            if self.velocity[1] > 0:
                self.velocity[1] += .5
            elif self.velocity[1] < 0:
                self.velocity[1] -= .5
            else:
                if randint(0, 10) > 2:
                    self.velocity[1] = self.startVel
                    self.velocity[0] = self.startVel

        print(f"Ball's Direction: {self.getDir()}")
        print(f"Ball Velocity x:{self.velocity[0]} y:{self.velocity[1]} after"
              + f"bounce {self.bounces}")

        # # Fix back to ball's actual velocity directions
        # self.velocity[1] = -self.velocity[1]
        # self.velocity[2] = -self.velocity[2]
        # Cause ball to go the opposite way it was going on the x axis
        self.velocity[0] = -self.velocity[0]

        # Add to the bounce count. Could be used for endurance or fake ones
        self.bounces += 1