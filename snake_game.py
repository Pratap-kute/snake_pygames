import random
import sys

import pygame
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    # create a rectangle for the snake
    # draw the rectangle
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), snake_rect)

    # move tehe snake
    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            # slice the list and create a new list
            body_copy = self.body[:-1]
            # create a new head and add it to the list
            body_copy.insert(0, body_copy[0] + self.direction)
            # update the snake body
            self.body = body_copy[:]

    def add_block(self):
        # add a block to the snake
        self.body.append(self.body[-1] + self.direction)


class FRUIT:
    # create an x and y position for the fruit
    # draw a square at that position
    def __init__(self):
        self.randomize()

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

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if (
            self.fruit.position.x == self.snake.body[0].x
            and self.fruit.position.y == self.snake.body[0].y
        ):
            # reposition the fruit
            self.fruit.randomize()
            # add a new block to the snake
            self.snake.add_block()


pygame.init()
cell_size = 40
cell_number = 20

# create a grid system in which the snake will move
# currently the grid is 40x20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

main_game = MAIN()

# capture the event when the user presses the arrow keys
SCREEN_UPDATE = pygame.USEREVENT
# time in milliseconds
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
