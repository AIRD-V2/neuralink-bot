import pygame
import time
import random

# Start pygame ;-)
pygame.init()

# Set the window size
display_width = 800
display_height = 800
game_display = pygame.display.set_mode((display_width, display_height))

# Set window title
pygame.display.set_caption("Neuralink Surgery Game")

# Game colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (155, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 155)


####################
"""GAME VARIABLES"""
####################
FPS = 15
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 25)

# Size of the neural lace on screen
lace_size = 10
lace_max = 9
# List of laces
lace_list = []

#list of fractal coordinates:
vessel_list = []

### N0TE: ALL THESE FUNCTIONS ARE JUST A GUESS AT WHAT THE STRUCTURE OF THE PROGRAM WILL BE... ###
def vessels():
    """Create pygame representation of blood vessels"""
    #TODO: > create a list of coordinate pairs similar to the lace_list
    #      > create a recursive function
    #      > render the list of coordinates into the game screen (see line 56)
    
"""Recursively generate a list of coordinates"""    
def recurse():
    # base case: fractal goes off screen
    # take the previous coordinate, and either go down, left, right, or up, 
    #   but don't go in the same direction as the previous pixel.
    
    # later, I will implement the random function



"""### RE ADD LACE FUNCTION???"""
def lace(x, y, lace_list):
    """SHOW LACE COUNTER IN TOP LEFT"""
    remaining_laces = str(10 - len(lace_list))
    message_to_screen(remaining_laces, red, -50)

    #ADD: Checker to ensure a lace can't be placed on the same spot as a previous lace

    """### RENDER ALL THE LACES ###"""
    # RENDER THE CURRENT LACE
    pygame.draw.rect(game_display, blue, [x, y, lace_size, lace_size])
    for x_y in lace_list:
        pygame.draw.rect(game_display, green, [x_y[0], x_y[1], lace_size, lace_size])


def score():
    """
    Haven't decided how this is going to be implemented. 
    """

    #SUGGESTION: Maximise distance from the blood vessels throughout all 2D frames of blood vessels
    #SUGGESTION: Have AI place threads and calculate score, baisically implement AI for this portion...

    pass


def lose_condition(lace_list):
    if len(lace_list) >= 10:    #if more than 9 laces,
        return True             #player loses


def text_objects(text, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_to_screen(msg, color, y_displace=0, size='small'):
    """Display a message on the screen!"""
    # surface object and the rectangle "shape"
    text_surface, text_rect = text_objects(msg, red)
    
    # get center of the textbox surface
    text_rect.center = (display_width / 2, display_height / 2 + y_displace)
    game_display.blit(text_surface, text_rect)


def game_loop():
    """The main loop of the neuralink surgery simulator"""
    game_exit = False
    game_over = False

    # Current lace we are rendering
    current_lace = 0


    # X AND Y COORDS OF THE LACE
    x = display_width / 2
    y = display_height / 2
    # Change in direction of lace at each timestep
    x_change = 0
    y_change = 0
    

    while not game_exit:
        # Basically just check if we have placed all the laces
        if lose_condition(lace_list) == True:
            game_over = True
        while game_over == True:
            game_display.fill(white)
            message_to_screen("Game Over!", red)
            message_to_screen("Press C to play again or Q to quit", black, y_displace=50)
            # Reset lace_list (otherwise it will render laces placed during the last run)
            del lace_list[:]
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()


        """Main Game Section"""
        for event in pygame.event.get():
            # If you forget this line you can't close the game window... LOL
            if event.type == pygame.QUIT:
                game_exit = True 
            

            """### MOVEMENT ###"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -lace_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = lace_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -lace_size # negative y = up in pygame
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = lace_size # positive y = down
                    x_change = 0
                elif event.key == pygame.K_BACKSPACE:
                    """### TURN THIS INTO A FUNCTION??? ###"""
                    # Get current coordinates
                    x += x_change
                    y += y_change
                    # Place in list
                    placed_lace = [x, y]
                    # Add to lace_list
                    lace_list.append(placed_lace)
                    # Increment current_lace
                    current_lace += 1
                    # PRINT LINE FOR TESTING
                    print(lace_list)


            """### STOP MOVING WHEN KEY IS RELEASED ###"""
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 0
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = 0 # negative y = up in pygame
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = 0 # positive y = down
                    x_change = 0
                

            """GAME BOUNDARIES"""
            if x >= display_width or x < 0 or y >= display_height or y < 0:
                game_over = True
            

        """UPDATE POSISTION OF LACE BASED OFF PLAYER INPUT"""
        # Set posistion based on velocity
        x += x_change
        y += y_change

        # We have to render the background first since layers are in order from furthest to closest
        game_display.fill(white)

        """### RENDER ALL THE LACES ###"""
        lace(x, y, lace_list)

        """MAIN GAME ITEMS"""
        pygame.display.update()

        """Render at the framerate ^^^"""
        clock.tick(FPS)


    pygame.quit()
    quit


# Start the game!
game_loop()
