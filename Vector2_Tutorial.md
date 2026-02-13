# Pygame - Vector2 Tutorial
## Why Use Vector2?

In games, we constantly work with:

* Positions `(x, y)`
* Velocities `(vx, vy)`
* Directions
* Movement
* Distance between objects
* Angles and rotation

Instead of manually managing x and y separately, `Vector2` lets us treat them as a **single mathematical object**.
Without Vector2:

* Movement is messy
* Diagonal speed is wrong
* Rotation is painful

With Vector2:

* Math becomes clean
* Code becomes readable
* Physics becomes manageable
---

# Importing and Creating a Vector

```python
import pygame

vec = pygame.math.Vector2
```

Now you can create vectors:

```python
position = vec(100, 200)
velocity = vec(3, -2)
```

You can access components:

```python
print(position.x)
print(position.y)
```

Or treat it like a list:

```python
print(position[0])  # x
print(position[1])  # y
```

---

# Vector Addition (Movement Made Easy)

Instead of:

```python
x += vx
y += vy
```

You can do:

```python
position += velocity
```

That’s it. Both x and y update automatically.

---

# Basic Example: Moving Circle

```python
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

vec = pygame.math.Vector2

position = vec(400, 300)
velocity = vec(4, 2)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    position += velocity

    screen.fill("black")
    pygame.draw.circle(screen, "white", position, 20)
    pygame.display.flip()

pygame.quit()
```

---

# Magnitude 

The magnitude tells you **how long** the vector is.

```python
velocity = vec(3, 4)
print(velocity.length())  # 5
```

This uses the Pythagorean theorem.

---

# Normalizing a Vector (Direction Only)

Sometimes we want **direction without speed**.

```python
direction = vec(3, 4)
direction = direction.normalize()
```

Now the vector has:

```
length = 1
```

This is extremely important for consistent movement speed.

---

# Player Movement Example 

Without normalization, diagonal movement is faster.

Correct way:

```python
keys = pygame.key.get_pressed()

direction = vec(0, 0)

if keys[pygame.K_w]:
    direction.y = -1
if keys[pygame.K_s]:
    direction.y = 1
if keys[pygame.K_a]:
    direction.x = -1
if keys[pygame.K_d]:
    direction.x = 1

if direction.length() > 0:
    direction = direction.normalize()

speed = 5
position += direction * speed
```

Now movement speed is consistent in all directions.

---

# Multiplying Vectors (Scaling Speed)

```python
velocity = vec(1, 0)
velocity *= 10
```

Now it moves 10 pixels per frame instead of 1.

---

# Distance Between Two Objects

```python
player = vec(100, 100)
enemy = vec(200, 150)

distance = player.distance_to(enemy)
print(distance)
```

Useful for:

* Collision detection
* Enemy AI
* Trigger zones

---

# Moving Toward a Target (Very Important!)

This is used in:

* Homing missiles
* Enemy chasing player
* Smooth camera following

```python
direction = target - position
direction = direction.normalize()
position += direction * speed
```

Explanation:

```
target - position → gives direction vector
normalize()       → makes length 1
* speed           → controls how fast we move
```

---

# Dot Product (Advanced but Powerful)

```python
v1 = vec(1, 0)
v2 = vec(0, 1)

print(v1.dot(v2))  # 0
```

Dot product tells you:

* If vectors point same direction (positive)
* Opposite direction (negative)
* Perpendicular (0)

Used in:

* Vision cones
* Lighting
* Physics

---

# Rotating a Vector

```python
velocity = vec(5, 0)
velocity = velocity.rotate(90)
```

Now the vector points upward.

This is extremely useful for:

* Spaceship games
* Bullets
* Rotation-based movement

---

# Complete Example: Player Class with Vector2

```python
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

vec = pygame.math.Vector2

class Player:
    def __init__(self):
        self.pos = vec(WIDTH // 2, HEIGHT // 2)
        self.speed = 5
        self.radius = 20

    def update(self):
        keys = pygame.key.get_pressed()
        direction = vec(0, 0)

        if keys[pygame.K_w]:
            direction.y = -1
        if keys[pygame.K_s]:
            direction.y = 1
        if keys[pygame.K_a]:
            direction.x = -1
        if keys[pygame.K_d]:
            direction.x = 1

        if direction.length() > 0:
            direction = direction.normalize()

        self.pos += direction * self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.pos, self.radius)

player = Player()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    screen.fill("black")
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
```


