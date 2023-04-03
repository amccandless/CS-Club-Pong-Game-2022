# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle
from ball import Ball
from goal import Goal
from enemy import Enemy
import time
pygame.init()

# Define some colors
EASY = (102, 161, 80)  # Agreed upon color
WHITE = (255, 255, 255)
GOLD = (255, 200, 0)
# DEFINE SCREEN SIZE
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Open a new window

#pygame.mixer.music.load("price-of-freedom-33106.mp3")
#pygame.mixer.music.play(-1)


#

def menu():
    """Outputs and handles text based menu"""
    menu = True
    while menu:

        print("""Welcome to CS Club Pong Game
To Play - Enter 1
Copyright 2022 CS Club""")
        answer = input(":")
        if answer == '1':

            menu = False
        else:

            pass


def pauseGame():
    """Pauses the game essentially.
    Returns False when exit tried in pause mode.
    Returns True if no exit attempted.
    Basics from Pause function https://pythonprogramming.net/pause-game-pygame/"""
    global screen

    pause = True
    pygame.mixer.music.pause()
    while pause:

        text = font.render(str("P A U S E"), 1, WHITE)
        screen.blit(text, (200, 200))
        pygame.display.flip()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                goal = False
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:

                    pause = False
                    return False
                if event.key == pygame.K_p:
                    pause = False
                    return True
                # if event.key == pygame.K_r:

            clock.tick(10)
    pygame.mixer.music.unpause()


def scoredGoal():
    """Pauses the game essentially.
    Returns False when exit tried in goal time.
    Returns True if no exit attempted.
    Basics from Pause function https://pythonprogramming.net/pause-game-pygame/"""
    global screen

    goal = True
    while goal:
        text = font.render(str("G O A L !"), 1, GOLD)
        screen.blit(text, (SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2-150))
        pygame.display.flip()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                goal = False
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                    goal = False
                    return False
                else:
                    goal = False
                    return True
            clock.tick(10)


# Create ball
ball = Ball(WHITE, 10, 10, 10, 345, 195, 4)

# Create paddles
paddleA = Paddle(WHITE, 10, 100, 20, 200, 1)
# Start variables moved to constructor
#paddleA.startX = 20
#paddleA.startY = 200

paddleB = Enemy(WHITE, 10, 100, 670, 200, "blue", ball, 'easy')
#paddleB.startX = 670
#paddleB.startY = 200


# 1 PLAYER MODE IS 1. 2 PLAYER MODE IS 2

gameMode = 1

# Create Goals
goal_L = Goal(WHITE, 10, SCREEN_HEIGHT)
goal_L.rect.x = 0
goal_L.rect.y = 0

goal_R = Goal(WHITE, 10, SCREEN_HEIGHT)
goal_R.rect.x = SCREEN_WIDTH - goal_R.width
goal_R.rect.y = 0


# Set font
font = pygame.font.Font(None, 74)

fontTitle = pygame.font.Font(None, 90)
fontSub = pygame.font.Font(None, 60)
# Sprite list
all_sprites_list = pygame.sprite.Group()

# Add the sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
all_sprites_list.add(goal_L)
all_sprites_list.add(goal_R)
paddleA.moveGen
# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = False
carryOn2 = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


menu()
while carryOn2:
    # Initialise player scores
    scoreA = 0
    scoreB = 0
    # Title Screen
    screen.fill(EASY)

    cscClub = fontTitle.render("CSC CLUB PING PONG", 1, GOLD)
    screen.blit(cscClub, (SCREEN_WIDTH/2-340, SCREEN_HEIGHT/2-150))
    text = fontSub.render(str("Press A for VS Cpu"), 1, WHITE)
    screen.blit(text, (SCREEN_WIDTH/2-200, SCREEN_HEIGHT/2))
    text = fontSub.render(str("Press B for 2 Players"), 1, WHITE)
    screen.blit(text, (SCREEN_WIDTH/2-200, SCREEN_HEIGHT/2+50))
    pygame.display.flip()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            carryOn2 = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:

                carryOn = True
                gameMode = 1
            if event.key == pygame.K_b:
                carryOn = True
                gameMode = 2
            # if event.key == pygame.K_r:

        clock.tick(10)

    while carryOn:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.exit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_x:
                    carryOn = False
                if event.key == pygame.K_p:
                    carryOn = pauseGame()

        # Update velocity
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:

            paddleA.velUp(2)

        elif keys[pygame.K_s]:

            paddleA.velDown(2)

        else:

            paddleA.idle()

        # PLAYER 2 COMPARISON HERE
        if gameMode == 2:
            if keys[pygame.K_UP]:

                paddleB.velUp(2)
            elif keys[pygame.K_DOWN]:
                paddleB.velDown(2)
            else:
                paddleB.idle()
            paddleB.moveGen()
        else:
            paddleB.act()
            # Note. remove idle to make it old way
        # Move generally by changing the paddles by .moveGen
        paddleA.moveGen()

        # Do Computer Player actions if going against computer
        #paddleB.act()
        paddleB.moveGen()
        # --- Game logic should go here
        all_sprites_list.update()

        # TO DO:LET THE SCREEN BE DEFINED SOMEWHERE
        # Check if the ball is bouncing against any of the 4 walls:
        # If it is, reflect the velocity for a *bounce*
        if ball.rect.x >= 690:

            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            scoreB += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        # Check for the ball to be touching a paddle
        # and not already touching a paddle
        if (pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB)) and (ball.getPaddleCollide() == False):
            # Bounce and set paddle collide to true
            print(f"Paddle A Vel: {paddleA.getVelocity()}"
                  + f"Paddle B Vel: {paddleB.getVelocity()}")

            # pygame.mixer.Sound.play(bounce_sound)
            if paddleA.paddleType == 0:

                if paddleA.getVelocity() == 0:
                    ball.bounce(0)
                elif paddleA.getVelocity() > 0:
                    ball.bounce(1)

                else:
                    ball.bounce(2)
                    # CHECK COMPARED TO BALL SIZE
            elif paddleA.paddleType == 1:

                # Range 1. y + 20 height-20 to Height
                tempY = paddleA.getY()
                if (ball.getY() > tempY and ball.getY() < tempY+40) or (ball.getY() < tempY + paddleA.height - 40 and ball.getY() > tempY + paddleA.height):
                    ball.bounce(4)
                else:
                    ball.bounce(5)

            ball.setPaddleCollide(True)
        # elif paddleA.paddleType == 1:

            #    if paddleA.getVelocity() == 0:
            #
            #        ball.bounce()
            #   elif paddleA.getVelocity() >0:
            #       ball.bounce(1)

            #   else:
            #      ball.bounce(2)

            # ball.setPaddleCollide(True)

        else:
            # Else, check to see if it is still colliding,
            # if so, keep ball moving with no change.
            # If not, set PaddleCollide to false
            if (pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB)):
                pass
            else:

                ball.setPaddleCollide(False)

        # When the ball collides with the goal,
        # Increase score
        # Pause for half a second
        # Reset positions of ball and paddles
        # Call scoredGoal() function to display goal text and to
        # pause game till user input.
        # Idea: Keep objectsi n a list in order to keep track better.
        if pygame.sprite.collide_mask(ball, goal_L):
            scoreB += 1
            time.sleep(.5)
            ball.reset()
            paddleA.reset()
            paddleB.reset()
            # Scored Goal returns False if exit/x wasnt pressed and True if it was
            carryOn = scoredGoal()
        if pygame.sprite.collide_mask(ball, goal_R):
            scoreA += 1
            time.sleep(.5)
            ball.reset()
            paddleA.reset()
            paddleB.reset()
            # Scored Goal returns False if exit/x wasnt pressed and True if it was
            carryOn = scoredGoal()

        # --- Drawing code should go here
        # First, clear the screen to black.
        screen.fill(EASY)

        # AGAIN please make a scrren class or defined in game class for this
        # Draw the net
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        # Display scores:

        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (250, 10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (420, 10))

        # print("Enemy Paddle Y: "  + str(paddleB.getY()))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

        if scoreA == 5:
            text = font.render(str("PLAYER 1 WINS !"), 1, GOLD)
            screen.blit(text, (SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2-150))
            pygame.display.flip()
            time.sleep(2)
            carryOn = False
        elif scoreB == 5:
            text = font.render(str("PLAYER 2 WINS !"), 1, WHITE)
            screen.blit(text, (SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2-150))
            pygame.display.flip()
            time.sleep(2)
            carryOn = False
# Stop the game. Afterwards can run code to save things to file or something
pygame.quit()