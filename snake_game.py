import random
import sys

import pygame
from pygame.math import Vector2


class FRUIT:
    # create an x and y position for the fruit
    # draw a square at that position
    def __init__(self):
        # create a random position for the fruit
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)

    # create a rectangle for the fruit
    # draw the rectangle
    def draw_fruit(self):
        # for Rect we need : x, y, width, height
        fruit_rect = pygame.Rect(
            int(self.position.x * cell_size),
            int(self.position.y * cell_size),
            cell_size,
            cell_size,
        )
        # draw the rectangle on the screen
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


pygame.init()
cell_size = 40
cell_number = 20

# create a grid system in which the snake will move
# currently the grid is 40x20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
fruit = FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)
