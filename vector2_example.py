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
# Player Class
# -----------------------------
class Player:
    def __init__(self, x, y):
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)
        self.speed = 5
        self.radius = 20
        self.color = BLUE

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.vel.update(0, 0)

        if keys[pygame.K_a]:
            self.vel.x = -1
        if keys[pygame.K_d]:
            self.vel.x = 1
        if keys[pygame.K_w]:
            self.vel.y = -1
        if keys[pygame.K_s]:
            self.vel.y = 1

        # Normalize diagonal movement
        if self.vel.length() > 0:
            self.vel = self.vel.normalize() * self.speed

    def update(self):
        self.pos += self.vel

        # Keep player on screen
        self.pos.x = max(self.radius, min(WIDTH - self.radius, self.pos.x))
        self.pos.y = max(self.radius, min(HEIGHT - self.radius, self.pos.y))

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

# -----------------------------
# Create Player
# -----------------------------
player = Player(WIDTH // 2, HEIGHT // 2)

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
    # Update
    # -------------------------
    player.handle_input()
    player.update()

    # -------------------------
    # Draw
    # -------------------------
    screen.fill(WHITE)
    player.draw(screen)
    pygame.display.flip()

# -----------------------------
# Cleanup
# -----------------------------
pygame.quit()
