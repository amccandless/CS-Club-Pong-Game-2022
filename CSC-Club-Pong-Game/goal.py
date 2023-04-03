import pygame
BLACK = (0, 0, 0)


class Goal(pygame.sprite.Sprite):
    """The class for the ball
    Attributes:
    color: Current color of the Goal
    width: Width of the Goal
    height: Height of the Goal
    """

    def __init__(self, color, width, height):

        # Call sprite initiator
        super().__init__()

        # Set up things needed
        self.color = color
        self.width = width
        self.height = height

        # Draw goal
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        """Move goal object up.
        Parameter:
        pixels: Amount of pixels to move up."""
        self.rect.y -= pixels

    def moveDown(self, pixels):
        """Move goal object down.
        Parameter:
        pixels: Amount of pixels to move down."""
        self.rect.y += pixels