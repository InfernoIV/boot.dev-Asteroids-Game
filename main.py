# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from the module
# database.py into the current file
from constants import *

def main():
    # init the game
    pygame.init()
    # check if started
    if pygame.get_init() == False: 
        print(f"pygame failed to init!")
        # stop the script
        return
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # set the size and get the screen
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # infinite loop
    while True:
        #set surface to black
        #screen.fill(BLACK)
        pygame.Surface.fill(screen, BLACK)

        if False:
            break

        # lastly: refresh the screen
        pygame.display.flip()

    return

if __name__ == "__main__":
    main()
