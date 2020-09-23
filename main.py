import pygame
import random

from pygame.mixer import fadeout
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

def is_clicked(pos, color):
    """ If the box is clicked """
    m_x, m_y = pos

    if color.x < m_x < color.x + color.box_size and color.y < m_y < color.y + color.box_size:
        return True
    
    return False

def play_clicked(surface, color):
    """ Plays on clicked """
    color.play()
    pygame.draw.rect(surface, (150, 150, 150), (color.x, color.y, BOX_SIZE, BOX_SIZE))
    pygame.display.update()
    pygame.time.delay(250)
    pygame.draw.rect(surface, color.color, (color.x, color.y, BOX_SIZE, BOX_SIZE))

def main(surface):
    """ Main function """
    red = Red(BOX_SIZE // 2, BOX_SIZE // 2, BOX_SIZE)
    green = Green(red.x + BOX_SIZE, BOX_SIZE // 2, BOX_SIZE)
    blue = Blue(BOX_SIZE // 2, red.y + BOX_SIZE, BOX_SIZE)
    yellow = Yellow(red.x + BOX_SIZE, red.y + BOX_SIZE, BOX_SIZE)

    # Game variables
    colors_ = [red, green, blue, yellow]
    run = True
    computers_turn = True

    # Patterns
    pattern = [random.choice(colors_)]
    player_pattern = []

    while run:
        draw(surface, colors_)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                for color in colors_:
                    if is_clicked(pos, color) and not computers_turn:
                        player_pattern.append(color)
                        play_clicked(surface, color)

                        if pattern[pattern.index(color)] != player_pattern[player_pattern.index(color)]:
                            run = False

        if len(pattern) == len(player_pattern):
            pygame.time.delay(500)
            pattern.append(random.choice(colors_))
            player_pattern = []
            computers_turn = True

        if computers_turn:
            pygame.time.delay(500)

            for color in pattern:
                pygame.time.delay(500)
                play_clicked(surface, color)
            
            computers_turn = False

    pygame.quit()

# Screen
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Simon Says!")

if __name__ == '__main__':
    main(win)