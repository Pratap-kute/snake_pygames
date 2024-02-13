# SNAKE Game

## Table of Contents

1. [**Introduction**](#introduction)
2. [**Project Setup**](#project-setup)
   - [**Dependencies**](#dependencies)
   - [**Running the Game**](#running-the-game)
3. [**Game Objects**](#game-objects)

- [**SNAKE Class**](#snake-class)
- **Constructor (`__init__`)**
  - **Purpose:**
    - Initializes snake segments, direction, image assets, and sound effect.
  - **Key Lines:**
    - `self.direction = Vector2(0, 0)`: Sets the initial direction to stationary.
    - Image loading lines: Load necessary head, tail, and body images for visualization.
  - **Why:**
    - Establishes the starting state of the snake, allowing movement and visual representation.
- **`draw_snake` Function**
  - **Purpose:**
    - Draws the snake on the screen, handling dynamic head/tail graphics.
  - **Key Lines:**
    - `update_head_graphics()`: Selects the appropriate head image based on direction.
    - `update_tail_graphics()`: Selects the appropriate tail image based on direction.
    - `if index == 0:` ... `elif index == len(self.body) - 1:`: Draws head and tail using correct images.
    - Conditional blocks for body segments: Handle various corner and straight body segments using correct images.
  - **Why:**
    - Ensures the snake appears visually correct based on its movement direction.
      - Dynamic image selection enhances realism and clarity.
- **`move_snake` Function**
  - **Purpose:**
    - Updates the snake's position by modifying its `body` list.
  - **Key Lines:**
    - `if self.new_block:`: Handles snake growth after fruit consumption.
    - `body_copy = self.body[:]`: Creates a copy of the `body` list for safe modification.
    - `body_copy.insert(0, body_copy[0] + self.direction)`: Adds a new block in the current direction.
    - `else:`: Handles standard movement without growth.
  - **Why:**
    - Implements the core movement logic, ensuring the snake's position changes smoothly while maintaining game rules.
- **`add_block` Function**
  - **Purpose:**
    - Adds a new block to the snake's tail after fruit consumption.
  - **Key Lines:**
    - `self.body.append(self.body[-1] + self.direction)`: Appends a new block at the tail, extending the snake.
  - **Why:**
    - Represents growth after the snake eats fruit, rewarding the player and making the game more challenging.
- **Other Functions:**
  - `play_crunch_sound` plays the sound effect when the snake eats fruit.
  - `reset` resets the snake's position and direction (e.g., for game restarts).
- [**FRUIT Class**](#fruit-class)
  - **Constructor (`__init__`)**
    - **Purpose:**
      - Initializes the fruit with a random position and loads its image asset.
    - **Key Lines:**
      - `self.randomize()`: Calls the `randomize` function to set a random position.
      - `apple = pygame.image.load("graphics/apple.png").convert_alpha()`: Loads the apple image.
    - **Why:**
      - Creates the target for the snake, adding an element of randomness and visual representation.
  - **`draw_fruit` Function**
    - **Purpose:**
      - Draws the fruit on the screen at its current position.
    - **Key Lines:**
      - `fruit_rect = pygame.Rect( ... )`: Creates a rectangle representing the fruit's position and size.
      - `screen.blit(apple, fruit_rect)`: Draws the apple image onto the rectangle.
    - **Why:**
      - Visualizes the fruit on the screen, making it clear where the snake needs to go.
  - **`randomize` Function**
    - **Purpose:**
      - Moves the fruit to a new random position within the grid.
    - **Key Lines:**
      - `self.x = random.randint(0, cell_number - 1)`: Randomly chooses an X-coordinate.

4. **Gameplay Mechanics**
   - **Snake Movement**
   - **Fruit Consumption and Growth**
   - **Game Over Conditions**
5. **Deep Dive into Challenging Game Logic**
   - **Managing Snake Body Segments:**
     - Movement and Growth Explained
     - Visual Representation and Corner Handling
   - **Efficient Collision Detection:**
     - Fruit Consumption Detection
     - Self-Collision Detection

## Introduction

This Python code for a classic Snake game, providing detailed descriptions of each function, class, and gameplay mechanic.

## Project Setup

**Dependencies:**

- Python 3.x
- Pygame library (install with `pip install pygame`)

**Running the Game:**

1. Save the code as `snake.py`.
2. Open a terminal in the same directory.
3. Run the game using `python snake.py`.

## Game Objects

**SNAKE Class:**

- **`__init__`:**
  - Initializes the snake's initial position, direction, and body segments.
  - Loads visual assets for snake head, tail, and body segments.
  - Tracks snake length and a flag for adding a new block after fruit consumption.
- **`draw_snake`:**
  - Iterates through snake segments, selecting appropriate image assets based on segment position and direction.
  - Updates head and tail graphics dynamically to reflect changing directions.
- **`move_snake`:**
  - Appends a new head segment in the current direction, effectively moving the snake.
  - Removes the last tail segment if the `new_block` flag is not set (no growth after fruit).
  - Handles edge cases (e.g., snake wrapping around the screen) as needed.
- **`add_block`:**
  - Appends a new block to the snake's tail, implementing growth after fruit consumption.
- **`play_crunch_sound`:**
  - Plays a sound effect when the snake eats fruit, enhancing the immersive experience.
- **`reset`:**
  - Resets the snake's position, direction, and length to start values.

**FRUIT Class:**

- **`__init__`:**
  - Randomly initializes the fruit's position within the game grid.
  - Loads the fruit's image asset.
- **`draw_fruit`:**
  - Draws the fruit image at its current position on the screen.
- **`randomize`:**
  - Chooses a new random position for the fruit within the grid, ensuring it doesn't overlap with the snake.

**MAIN Class:**

- **`__init__`:**
  - Creates instances of the `SNAKE` and `FRUIT` classes, setting up the game objects.
- **`update`:**
  - Calls `move_snake` to update the snake's position.
  - Calls `check_collision` to detect collisions with the fruit or the snake's body.
  - Calls `check_fail` to assess game over conditions.
  - Updates the score if the snake eats fruit.
- **`draw_elements`:**
  - Calls `draw_grass` to draw the background.
  - Calls `draw_fruit` to draw the fruit.
  - Calls `draw_snake` to draw the snake.
  - Calls `draw_score` to display the current score.
- **`check_collision`:**
  - Detects collisions between the snake's head and the fruit (growth trigger).
  - Detects collisions between the snake's head and its own body (game over).
- **`check_fail`:**
  - Determines if the game should end based on specific conditions (e.g., reaching edge of screen).
- **`game_over`:**
  - Displays a game over message and handles any necessary end-of-game actions.
- **`draw_grass`:**
  - Draws the grassy background for visual appeal.

## Deep Dive into Challenging Game Logic

### 5.1 Managing Snake Body Segments

- **Movement and Growth:**
  - Each segment's position relies on the **previous** segment, creating a "follow-the-leader" system.
  - When moving, the head segment updates first based on the direction, then all others follow suit.
  - Growth after fruit consumption adds a new segment at the head, extending the snake smoothly.
- **Visual Representation:**
  - Segments need dynamic graphics based on their relative positions.
  - Straight segments, corner segments, and tail require different images for a realistic look.
  - Conditional logic checks neighboring segments to determine the correct image for each.

### 5.2 Efficient Collision Detection

- **Fruit Consumption:**
  - Checking if the snake's head overlaps with the fruit's position indicates consumption.
- **Self-Collision:**
  - Iterating through body segments and comparing their positions with the head's position is necessary.
  - Any overlap signifies a collision, leading to game over.
