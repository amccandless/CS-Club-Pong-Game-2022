import pygame
BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    """Paddle class for paddle objects.


    Attributes:
    color: Current color of the Goal
    width: Width of the Enemy
    height: Height of the Enemy
    startX: Starting x of the Enemy
    staryY: Starting y of the Enemy
    paddleType: Paddle mode chosen by integer value
    ball: Ball the enemy should focus on
    teleport: Ability to teleport boolean
    """

    def __init__(self, color, width, height, startX, startY, paddleType=0, teleport=False):
        super().__init__()

        self.color = color
        self.width = width
        self.height = height
        self.velocity = 0
        self.startX = startX
        self.startY = startY
        self.teleport = teleport
        self.paddleType = paddleType
        # Draw the paddle
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.reset()

    def getVelocity(self):
        """Returns velocity"""
        return self.velocity

    def velUp(self, amount=1, max_vel=10):
        """Increase velocity

        ParametersL
        amount: Amount to increase by
        max_vel: maximum allowed velocity"""
        if self.velocity <= max_vel:

            self.velocity += amount
        #self.moveUp(abs(self.velocity))

    def velDown(self, amount=1, max_vel=10):
        """Decrease velocity

        ParametersL
        amount: Amount to decrease by
        max_vel: maximum allowed velocity"""
        if self.velocity >= -max_vel:

            self.velocity -= amount
        #self.moveDown(abs(self.velocity))

    def moveGen(self):
        """Move paddle by new velocity way as opposed to the moveUp/Down funcs
        """

        self.rect.y -= self.velocity
        if self.teleport:

            if self.rect.y > 400:  # Change these to screen size variables later
                self.rect.y = 0
            if self.rect.y < 0:
                self.rect.y = 400
        if self.rect.y < 0:

            self.rect.y = 0
        if self.rect.y > 500-self.height:

            self.rect.y = 500-self.height
        ##if self.velocity > 1 or self.velocity < -1:
           ## self.velocity = self.velocity/2
        ##else:
           ## self.velocity = 0

    def idle(self):
        """Decrease paddle's velocity over time"""
        if self.velocity != 0 and self.velocity > 0:
            self.velocity -= 2
        elif self.velocity != 0 and self.velocity < 0:
            self.velocity += 2

    def getX(self):
        """Returns X value"""
        return self.rect.x

    def getY(self):
        """Returns Y value"""
        return self.rect.y

    def moveUp(self, pixels):
        """Move paddle object up.

        Parameter:
        pixels: Amount of pixels to move up."""
        self.rect.y -= pixels
        # Check that you are not going too far (off the screen)
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        """Move paddle object down.

        Parameter:
        pixels: Amount of pixels to move down."""
        self.rect.y += pixels
        # Check that you are not going too far (off the screen)
        print("I should be checking")
        if self.rect.y > 500-self.height:

            self.rect.y = 500-self.height

    def reset(self):
        """Resets paddle to start position"""
        self.rect.y = self.startY
        self.rect.x = self.startX
        self.velocity = 0
