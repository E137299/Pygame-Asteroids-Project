import pygame
from pygame.math import Vector2

# -----------------------------
# Initialization
# -----------------------------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vector2 Player Class Template")

clock = pygame.time.Clock()
FPS = 60

# -----------------------------
# Colors
# -----------------------------
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)





# -----------------------------
# Main Game Loop
# -----------------------------
running = True
while running:
    clock.tick(FPS)

    # -------------------------
    # Events
    # -------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # -------------------------
    # Draw
    # -------------------------
    screen.fill(WHITE)
    
    pygame.display.flip()

# -----------------------------
# Cleanup
# -----------------------------
pygame.quit()
