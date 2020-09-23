import pygame
import random
from colors import *

pygame.init()

# Screen size
WIDTH = 600

# Game constants
BOX_SIZE = 200

# Loss font
loss_font = pygame.font.SysFont('Arial', 60)
loss_text = loss_font.render("You lost!", 1, (255, 255, 255))

def draw(surface, colors_):
    """ Draws the screen """
    surface.fill((0, 0, 0))

    for color in colors_:
        color.draw(surface)

    pygame.display.update()

def is_clicked(pos, color):
    """ If the box is clicked """
    m_x, m_y = pos

    # Checking for the mouse coordinates
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

def display_message(surface, text):
    """ Displays a centered text """
    surface.fill((0, 0, 0))
    surface.blit(text, ((WIDTH - text.get_width()) // 2, (WIDTH - text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(500)

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
        # Drawing the screen
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

                        # Checking if the user entered the wrong pattern
                        for i in range(len(pattern)):
                            if pattern[i] != player_pattern[i]:
                                display_message(surface, loss_text)
                                pygame.quit()

        # If the user has completed the pattern
        if len(pattern) == len(player_pattern):
            pygame.time.delay(500)
            pattern.append(random.choice(colors_))
            player_pattern = []
            computers_turn = True

        # Showing the pattern
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
