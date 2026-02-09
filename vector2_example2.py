import pygame
from pygame.math import Vector2

# -----------------------------
# Initialization
# -----------------------------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Player with Forward Movement")

clock = pygame.time.Clock()
FPS = 60

# -----------------------------
# Colors
# -----------------------------
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
BLACK = (0, 0, 0)

# -----------------------------
# Player Class
# -----------------------------
class Player:
    def __init__(self, x, y):
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)

        self.speed = 0.3          # forward acceleration
        self.rotation_speed = 3   # degrees per frame
        self.angle = 0            # facing right

        self.radius = 20

    def handle_input(self):
        keys = pygame.key.get_pressed()

        # Rotate left / right
        if keys[pygame.K_a]:
            self.angle += self.rotation_speed
        if keys[pygame.K_d]:
            self.angle -= self.rotation_speed

        # Move forward
        if keys[pygame.K_w]:
            forward = Vector2(1, 0).rotate(-self.angle)
            self.vel += forward * self.speed

    def update(self):
        self.pos += self.vel

        # Optional friction (prevents infinite drifting)
        self.vel *= 0.98

        # Screen wrap
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT

    def draw(self, surface):
        # Draw player body
        pygame.draw.circle(surface, BLUE, self.pos, self.radius)

        # Draw facing direction
        forward = Vector2(1, 0).rotate(-self.angle)
        end_pos = self.pos + forward * self.radius

        pygame.draw.line(surface, BLACK, self.pos, end_pos, 3)

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_input()
    player.update()

    screen.fill(WHITE)
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
