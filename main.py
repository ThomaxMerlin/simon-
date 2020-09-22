import pygame
from colors import *

pygame.init()

# Screen size
WIDTH = 600

# Game constants
BOX_SIZE = 200

def draw(surface, colors_):
    """ Draws the screen """
    surface.fill((0, 0, 0))

    for color in colors_:
        color.draw(surface)

    pygame.display.update()

def main(surface):
    """ Main function """
    red = Red(BOX_SIZE // 2, BOX_SIZE // 2, BOX_SIZE)
    green = Green(red.x + BOX_SIZE, BOX_SIZE // 2, BOX_SIZE)
    blue = Blue(BOX_SIZE // 2, red.y + BOX_SIZE, BOX_SIZE)
    yellow = Yellow(red.x + BOX_SIZE, red.y + BOX_SIZE, BOX_SIZE)

    # Game variables
    colors_ = [red, green, blue, yellow]
    run = True

    while run:
        draw(surface, colors_)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

# Screen
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Simon Says!")

if __name__ == '__main__':
    main(win)