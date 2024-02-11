import sys

import pygame  # Import the pygame library

pygame.init()  # Initialize the game engine

screen = pygame.display.set_mode(
    (400, 500)
)  # Create a window with a resolution of 800x600 pixels

clock = pygame.time.Clock()  # Create a clock object to control the frame rate
test_surface = pygame.Surface((100, 200))  # Surface object
test_surface.fill(pygame.Color("blue"))

# creating rectangle Rect(left, top, width, height)
test_rect = pygame.Rect(100, 200, 100, 100)
while True:  # Infinite loop
    # The loop that will keep the game running
    for event in pygame.event.get():
        # This loop will keep the game running and will close the game if the user quits
        if event.type == pygame.QUIT:
            # If the user quits
            pygame.quit()
            # the above line sometime cause an issue so we will use the below line
            sys.exit()
    # filling colour to screen
    # screen.fill(pygame.Color("gold"))

    # using RGB colour scheme to screen
    screen.fill((175, 215, 70))

    # drawing rectangle on screen
    pygame.draw.rect(screen, (255, 0, 0), test_rect)  # drawing rectangle on screen
    # drawing Surface on screen which whole screen assign to game
    screen.blit(test_surface, (200, 250))
    pygame.display.update()  # Update the window
    clock.tick(60)  # Limit the frame rate to 60 frames per second
