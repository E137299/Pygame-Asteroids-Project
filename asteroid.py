import pygame
import random

# Initialize engine and setup display constants
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()  # Controls frame rate
font = pygame.font.SysFont("Arial", 48)

class Spaceship:
    def __init__(self):
        pass

    def rotate(self, dir):
        pass

    def accelerate(self):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass

def main():
    # Game State Objects
    running = True
    game_over = False

    while running:
        screen.fill((0, 0, 0)) # Clear frame

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        pygame.display.flip() # Update the full display
        clock.tick(60)        # Maintain 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
